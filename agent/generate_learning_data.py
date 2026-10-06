"""Generate deterministic local datasets for the Python learning curriculum."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


DEFAULT_SEED = 42


def _logistic(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def _write_csv(frame: pd.DataFrame, path: Path, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite {path}. Re-run with --force if intentional."
        )
    frame.to_csv(path, index=False)
    print(f"wrote {path} ({len(frame):,} rows, {len(frame.columns)} columns)")


def make_customers(rng: np.random.Generator, n: int = 2_000) -> pd.DataFrame:
    signup_start = np.datetime64("2020-01-01")
    signup_offsets = rng.integers(0, 365 * 5, size=n).astype("timedelta64[D]")
    customers = pd.DataFrame(
        {
            "customer_id": [f"C{i:05d}" for i in range(1, n + 1)],
            "age": np.clip(rng.normal(43, 14, n).round(), 18, 85).astype(int),
            "region": rng.choice(
                ["north", "south", "east", "west"], n, p=[0.24, 0.27, 0.29, 0.20]
            ),
            "segment": rng.choice(
                ["consumer", "small_business", "enterprise"],
                n,
                p=[0.70, 0.24, 0.06],
            ),
            "signup_date": signup_start + signup_offsets,
            "marketing_opt_in": rng.choice([True, False], n, p=[0.58, 0.42]),
        }
    )
    missing_age = rng.random(n) < 0.025
    customers["age"] = customers["age"].astype("float")
    customers.loc[missing_age, "age"] = np.nan
    return customers


def make_transactions(
    rng: np.random.Generator, customers: pd.DataFrame
) -> pd.DataFrame:
    transaction_counts = rng.poisson(5, len(customers)) + 1
    customer_ids = np.repeat(customers["customer_id"].to_numpy(), transaction_counts)
    n = len(customer_ids)
    dates = np.datetime64("2024-01-01") + rng.integers(0, 730, n).astype(
        "timedelta64[D]"
    )
    category = rng.choice(
        ["software", "hardware", "services", "training"],
        n,
        p=[0.38, 0.27, 0.25, 0.10],
    )
    category_multiplier = pd.Series(category).map(
        {"software": 1.0, "hardware": 1.6, "services": 2.1, "training": 0.8}
    )
    amount = rng.lognormal(mean=4.1, sigma=0.75, size=n) * category_multiplier
    transactions = pd.DataFrame(
        {
            "transaction_id": [f"T{i:06d}" for i in range(1, n + 1)],
            "customer_id": customer_ids,
            "transaction_date": dates,
            "category": category,
            "amount_eur": amount.round(2),
            "discount_pct": np.where(
                rng.random(n) < 0.32, rng.choice([5, 10, 15, 20], n), 0
            ),
            "returned": rng.random(n) < 0.075,
        }
    )
    transactions.loc[rng.random(n) < 0.018, "discount_pct"] = np.nan
    return transactions


def make_churn(rng: np.random.Generator, n: int = 2_500) -> pd.DataFrame:
    tenure = rng.integers(1, 73, n)
    contract = rng.choice(
        ["monthly", "one_year", "two_year"], n, p=[0.56, 0.28, 0.16]
    )
    internet = rng.choice(["fiber", "dsl", "none"], n, p=[0.52, 0.38, 0.10])
    payment = rng.choice(
        ["bank_transfer", "card", "electronic_check"], n, p=[0.36, 0.39, 0.25]
    )
    support_calls = np.clip(rng.poisson(1.5, n), 0, 8)
    monthly_charge = np.clip(
        rng.normal(62, 18, n)
        + 18 * (internet == "fiber")
        - 22 * (internet == "none"),
        15,
        140,
    )
    usage_hours = np.clip(rng.gamma(4.0, 10.0, n), 1, 160)
    age = np.clip(rng.normal(45, 15, n), 18, 90)
    household_size = rng.choice([1, 2, 3, 4, 5], n, p=[0.22, 0.34, 0.21, 0.16, 0.07])
    late_payments = np.clip(rng.poisson(0.55, n), 0, 5)

    log_odds = (
        -2.0
        + 1.15 * (contract == "monthly")
        - 0.75 * (contract == "two_year")
        + 0.035 * (monthly_charge - 65)
        - 0.027 * tenure
        + 0.30 * support_calls
        + 0.43 * late_payments
        + 0.50 * (payment == "electronic_check")
        + 0.60 * ((internet == "fiber") & (support_calls >= 3))
        + 0.35 * (usage_hours < 15)
        + rng.normal(0, 0.35, n)
    )
    churned = rng.binomial(1, _logistic(log_odds))

    frame = pd.DataFrame(
        {
            "customer_id": [f"CH{i:05d}" for i in range(1, n + 1)],
            "age": age.round(0),
            "household_size": household_size,
            "tenure_months": tenure,
            "contract": contract,
            "internet_service": internet,
            "payment_method": payment,
            "monthly_charge_eur": monthly_charge.round(2),
            "monthly_usage_hours": usage_hours.round(1),
            "support_calls_6m": support_calls,
            "late_payments_12m": late_payments,
            "churned": churned,
        }
    )
    frame.loc[rng.random(n) < 0.045, "monthly_usage_hours"] = np.nan
    frame.loc[rng.random(n) < 0.030, "age"] = np.nan
    frame.loc[rng.random(n) < 0.018, "payment_method"] = np.nan
    return frame


def make_housing(rng: np.random.Generator, n: int = 1_800) -> pd.DataFrame:
    neighborhood = rng.choice(
        ["central", "north", "south", "east", "west"],
        n,
        p=[0.15, 0.22, 0.24, 0.23, 0.16],
    )
    living_area = np.clip(rng.lognormal(4.55, 0.38, n), 35, 320)
    bedrooms = np.clip(np.round(living_area / 38 + rng.normal(0, 0.8, n)), 1, 7)
    age = np.clip(rng.gamma(2.2, 18, n), 0, 140)
    distance = np.clip(rng.gamma(2.0, 3.0, n), 0.2, 30)
    renovated = rng.random(n) < _logistic(-1.6 + 0.025 * age)
    energy = np.clip(88 - 0.38 * age + 8 * renovated + rng.normal(0, 9, n), 15, 100)
    garden = rng.random(n) < _logistic(0.4 - 0.07 * living_area / 10 + 0.12 * distance)
    neighborhood_effect = pd.Series(neighborhood).map(
        {"central": 120_000, "north": 45_000, "south": 15_000, "east": 32_000, "west": 55_000}
    ).to_numpy()
    price = (
        70_000
        + 3_250 * living_area
        + neighborhood_effect
        - 2_500 * distance
        - 1_050 * age
        + 48_000 * renovated
        + 650 * energy
        + 24_000 * garden
        + 420 * living_area * renovated
        - 9.5 * np.maximum(living_area - 210, 0) ** 2
        + rng.normal(0, 42_000, n)
    )
    frame = pd.DataFrame(
        {
            "property_id": [f"H{i:05d}" for i in range(1, n + 1)],
            "living_area_m2": living_area.round(1),
            "bedrooms": bedrooms.astype(int),
            "building_age_years": age.round(1),
            "distance_to_center_km": distance.round(2),
            "neighborhood": neighborhood,
            "renovated": renovated,
            "energy_score": energy.round(1),
            "has_garden": garden,
            "price_eur": np.maximum(price, 85_000).round(0),
        }
    )
    frame.loc[rng.random(n) < 0.035, "energy_score"] = np.nan
    frame.loc[rng.random(n) < 0.020, "building_age_years"] = np.nan
    return frame


def make_clinical_longitudinal(
    rng: np.random.Generator, patients: int = 300
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for patient_number in range(1, patients + 1):
        treatment = rng.choice(["control", "treatment"])
        age = np.clip(rng.normal(56, 12), 25, 85)
        random_intercept = rng.normal(0, 5.5)
        visits = int(rng.integers(3, 8))
        for visit in range(visits):
            month = visit * 2
            outcome = (
                52
                + random_intercept
                - 0.12 * (age - 55)
                - 0.65 * month
                - 1.2 * (treatment == "treatment")
                - 0.72 * month * (treatment == "treatment")
                + rng.normal(0, 3.5)
            )
            rows.append(
                {
                    "patient_id": f"P{patient_number:04d}",
                    "treatment": treatment,
                    "age": round(float(age), 0),
                    "visit": visit + 1,
                    "month": month,
                    "outcome_score": round(float(outcome), 2),
                }
            )
    frame = pd.DataFrame(rows)
    frame.loc[rng.random(len(frame)) < 0.012, "outcome_score"] = np.nan
    return frame


def make_customer_import() -> pd.DataFrame:
    """Fixed messy import for GDS Day 2; IDs are independent of customers.csv."""
    frame = pd.DataFrame({
        "customer_id": [f"IMP{i:03d}" for i in range(1, 11)],
        "age_raw": ["34", "51", "", "unknown", "-4", "145", " 42 ", "29", "63", "38"],
        "region_raw": [" North ", "SOUTH", "east", " West", "north", "central", "EAST ", "south", "west", "north"],
        "segment_raw": [" Consumer ", "enterprise", "small business", "CONSUMER", "consumer", "enterprise", "small_business", "consumer", "enterprise", "consumer"],
        "marketing_opt_in": [True, False, True, False, True, False, True, False, True, False],
    })
    conflict = frame.iloc[[1]].copy()
    conflict["age_raw"] = "52"
    return pd.concat([frame, frame.iloc[[0]], conflict], ignore_index=True)


def make_ci_telemetry(seed: int = DEFAULT_SEED) -> dict[str, pd.DataFrame]:
    """Fictional IFT-shaped teaching data, not a simulator of MED-EL devices.

    One implant per patient; rows stimulate and columns record. All parameters,
    group labels, QC rules, and time effects are invented for coding practice.
    An independent RNG keeps the existing course fixtures unchanged.
    """
    rng = np.random.default_rng(seed)
    n = 96
    age = rng.integers(25, 81, n).astype(float)
    array = rng.choice(["array_A", "array_B"], n)
    site = rng.choice(["site_1", "site_2", "site_3"], n)
    patient_effect = rng.normal(0, 0.85, n)
    patient_slope = rng.normal(0, 0.035, n)
    patients = pd.DataFrame({
        "patient_id": [f"CI{i:03d}" for i in range(1, n + 1)],
        "implant_id": [f"IMP{i:03d}" for i in range(1, n + 1)],
        "age_at_implant_years": age,
        "array_type": array,
        "site": site,
        "implant_side": rng.choice(["left", "right"], n),
    })
    patients.loc[[3, 19, 35, 51, 67, 83], "age_at_implant_years"] = np.nan
    # Administrative truncation, deliberately independent of measurements.
    short_followup = set(rng.choice(n, 24, replace=False).tolist())
    visits, cells = [], []
    stim, rec = np.meshgrid(np.arange(1, 13), np.arange(1, 13), indexing="ij")
    distance = np.abs(stim - rec)
    diagonal = distance == 0
    for i in range(n):
        surgery = pd.Timestamp("2024-01-01") + pd.Timedelta(days=int(rng.integers(0, 180)))
        for month in [0, 1, 3, 6]:
            if month == 6 and i in short_followup:
                continue
            visit_id = f"CI{i + 1:03d}_M{month:02d}"
            day = 0 if month == 0 else month * 30 + int(rng.integers(-4, 5))
            # Later visits more often use v2, with overlap at every visit window.
            protocol = "v2" if rng.random() < 0.2 + 0.09 * month else "v1"
            current = float(rng.choice([100, 150]))
            visit_effect = rng.normal(0, 0.16)
            t = day / 30
            diag_level = (6 + patient_effect[i] + 0.018 * (age[i] - 50)
                          + 0.4 * (array[i] == "array_B")
                          + (0.10 + patient_slope[i]) * t
                          + 0.25 * (protocol == "v2") + visit_effect)
            field = (0.30 + 1.6 * np.exp(-distance / 2.2)
                     + 0.07 * patient_effect[i] + 0.02 * t
                     + 0.06 * (protocol == "v2")
                     + 0.008 * (stim - rec) + rng.normal(0, 0.035, (12, 12)))
            field[diagonal] = (diag_level + 0.035 * (np.arange(12) - 5.5)
                               + rng.normal(0, 0.14, 12))
            # An unflagged local perturbation to investigate, not a diagnosis.
            if i == 6 and month == 3:
                field[7:10, 7:10] += 1.4
            voltage = (field * current).round(4)
            status = np.full((12, 12), "ok", dtype=object)
            missing = rng.choice(np.flatnonzero(~diagonal), 2, replace=False)
            status.flat[missing] = "not_recorded"
            voltage.flat[missing] = np.nan
            # A finite invalid value forces QC masking beyond dropna().
            if (i + month) % 7 == 0:
                k = int(rng.integers(0, 12))
                status[k, k] = "saturated"
                voltage[k, k] = 2000.0
            if (i + month) % 11 == 0:
                k = int(rng.integers(0, 12))
                status[k, k] = "not_recorded"
                voltage[k, k] = np.nan
            visits.append({
                "visit_id": visit_id, "patient_id": f"CI{i + 1:03d}",
                "implant_id": f"IMP{i + 1:03d}", "visit_month": month,
                "days_since_implant": day, "visit_date": (surgery + pd.Timedelta(days=day)).date().isoformat(),
                "protocol": protocol, "stim_current_ua": current,
            })
            for s, r, v, q in zip(stim.flat, rec.flat, voltage.flat, status.flat):
                cells.append({"visit_id": visit_id, "stim_contact": int(s),
                              "record_contact": int(r), "voltage_mv": v, "qc_status": q})

    visits = pd.DataFrame(visits)
    cells = pd.DataFrame(cells)
    # Ready-made per-visit features let modeling lessons run independently.
    observed = cells.merge(visits[["visit_id", "stim_current_ua"]],
                           on="visit_id", validate="many_to_one")
    observed["z"] = (observed["voltage_mv"] / observed["stim_current_ua"]).where(
        observed["qc_status"].eq("ok"))
    gap = (observed["stim_contact"] - observed["record_contact"]).abs()
    diag = observed.loc[gap.eq(0)].groupby("visit_id").agg(
        diag_mean_kohm=("z", "mean"), diag_sd_kohm=("z", "std"),
        n_diag_valid=("z", "count"))
    near = observed.loc[gap.eq(1)].groupby("visit_id")["z"].mean().rename("near_mean_kohm")
    far = observed.loc[gap.ge(6)].groupby("visit_id")["z"].mean().rename("far_mean_kohm")
    summary = visits.merge(diag, on="visit_id", validate="one_to_one")
    summary = summary.merge(near, on="visit_id", validate="one_to_one")
    summary = summary.merge(far, on="visit_id", validate="one_to_one")
    summary = summary.merge(patients.drop(columns="implant_id"), on="patient_id", validate="many_to_one")
    summary["months_since_implant"] = summary["days_since_implant"] / 30

    # Only adjacent scheduled windows; no interpolation or skipping missing visits.
    pairs = []
    next_month = {0: 1, 1: 3, 3: 6}
    for _, group in summary.groupby("patient_id"):
        by_month = group.set_index("visit_month")
        for current_month, target_month in next_month.items():
            if current_month not in by_month.index or target_month not in by_month.index:
                continue
            current_row = by_month.loc[current_month]
            target_row = by_month.loc[target_month]
            row = current_row.to_dict()
            row.update({"visit_month": current_month,
                        "planned_horizon_months": target_month - current_month,
                        "target_visit_id": target_row["visit_id"],
                        "target_visit_month": target_month,
                        "target_diag_mean_kohm": target_row["diag_mean_kohm"]})
            pairs.append(row)
    return {"patients.csv": patients, "visits.csv": visits, "matrix_cells.csv": cells,
            "visit_features.csv": summary, "prediction_pairs.csv": pd.DataFrame(pairs)}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
        help="Output directory (default: repository data directory).",
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--dataset", choices=["general", "ci-telemetry"], default="general",
                        help="Generate existing general fixtures or the independent CI teaching bundle.")
    parser.add_argument(
        "--force", action="store_true", help="Overwrite existing generated CSV files."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.dataset == "ci-telemetry":
        output = args.output_dir / "ci_telemetry"
        datasets = make_ci_telemetry(args.seed)
        existing = [output / name for name in datasets if (output / name).exists()]
        if existing and not args.force:
            raise FileExistsError(f"Refusing to overwrite existing CI fixtures: {existing}")
        output.mkdir(parents=True, exist_ok=True)
        for filename, frame in datasets.items():
            _write_csv(frame, output / filename, args.force)
        return
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)

    customers = make_customers(rng)
    datasets = {
        "customers.csv": customers,
        "transactions.csv": make_transactions(rng, customers),
        "customer_churn.csv": make_churn(rng),
        "housing.csv": make_housing(rng),
        "clinical_longitudinal.csv": make_clinical_longitudinal(rng),
        "customer_import.csv": make_customer_import(),
    }
    for filename, frame in datasets.items():
        _write_csv(frame, args.output_dir / filename, args.force)


if __name__ == "__main__":
    main()
