"""Input scaffolding for later lessons; no models or engineered spatial features.

Run notebooks from the repository root. Early sessions deliberately load and
reshape raw tables themselves. This module keeps later sessions independent of
previous learner answers. Missing cells stay NaN until a training-only transform.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "ci_telemetry"
NUMERIC = [
    "diag_mean_kohm", "diag_sd_kohm", "near_mean_kohm", "far_mean_kohm",
    "n_diag_valid", "age_at_implant_years", "months_since_implant",
    "planned_horizon_months",
]
CATEGORICAL = ["array_type", "protocol", "site"]


def load_problem(data_dir=DATA_DIR):
    """Return aligned current-visit tables and raw (N,12,12) matrices.

    IDs, future audit fields, and outcomes never enter X. The outcome is the next
    scheduled visit's observed diagonal mean. No missing visit is interpolated.
    Matrix axes retain contact labels 1..12, rows stimulate, columns record.
    """
    data_dir = Path(data_dir)
    pairs = pd.read_csv(data_dir / "prediction_pairs.csv").reset_index(drop=True)
    visits = pd.read_csv(data_dir / "visits.csv")
    cells = pd.read_csv(data_dir / "matrix_cells.csv")
    assert pairs["visit_id"].is_unique and visits["visit_id"].is_unique
    assert not cells.duplicated(["visit_id", "stim_contact", "record_contact"]).any()
    assert cells.groupby("visit_id").size().eq(144).all()
    assert cells[["stim_contact", "record_contact"]].isin(range(1, 13)).all().all()
    assert set(pairs["visit_id"]).issubset(set(visits["visit_id"]))
    observed = cells.merge(
        visits[["visit_id", "stim_current_ua"]], on="visit_id",
        validate="many_to_one", indicator=True,
    )
    assert observed["_merge"].eq("both").all()
    assert observed["stim_current_ua"].gt(0).all()
    valid = observed["qc_status"].eq("ok") & np.isfinite(observed["voltage_mv"])
    observed["value"] = (observed["voltage_mv"] / observed["stim_current_ua"]).where(valid)
    wide = observed.pivot(index="visit_id", columns=["stim_contact", "record_contact"], values="value")
    ordered_cells = pd.MultiIndex.from_product(
        [range(1, 13), range(1, 13)], names=["stim_contact", "record_contact"]
    )
    wide = wide.reindex(index=pairs["visit_id"], columns=ordered_cells)
    matrices = wide.to_numpy(dtype=np.float32).reshape(len(pairs), 12, 12)
    assert np.isfinite(matrices).any(axis=(1, 2)).all()
    return {
        "pairs": pairs,
        "X": pairs[NUMERIC + CATEGORICAL].copy(),
        "y": pairs["target_diag_mean_kohm"].to_numpy(dtype=np.float32),
        "groups": pairs["patient_id"].to_numpy(),
        "matrices": matrices,
        "mask": np.isfinite(matrices),
    }


def patient_partitions(problem):
    """Fixed positional train/validation/test indices: 54/18/24 patients.

    Split seed 42 reserves 24 test patients; seed 43 separates the remaining
    72 into 54 training and 18 validation patients. No outcomes are inspected.
    For CV, use concatenated train+validation indices and GroupKFold internally.
    Never use the test for early stopping, preprocessing, or model selection.
    """
    groups = problem["groups"]
    positions = np.arange(len(groups))
    dev, test = next(GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
                     .split(positions, groups=groups))
    train_local, val_local = next(
        GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=43)
        .split(dev, groups=groups[dev])
    )
    result = {"train": dev[train_local], "val": dev[val_local], "test": test}
    sets = {name: set(groups[idx]) for name, idx in result.items()}
    assert not (sets["train"] & sets["val"] or sets["train"] & sets["test"] or sets["val"] & sets["test"])
    assert set(np.concatenate(list(result.values()))) == set(positions)
    return result
