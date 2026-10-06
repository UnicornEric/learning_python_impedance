# Synthetic cochlear-implant telemetry teaching bundle

Every person, implant, measurement, group label, protocol, and effect is fictional.
This is an IFT-shaped coding fixture, not MED-EL data or a validated biophysical
simulation. Do not interpret its numerical patterns as clinical evidence. No
real patient records or external datasets are required.

## What the matrix means here

A visit has 12 stimulating contacts × 12 recording contacts: **rows stimulate,
columns record**, with contact labels 1–12. Labels are ordered contact indices,
not millimetres or an asserted apical/basal direction. The diagonal is recorded
on the stimulating contact; the other 132 directed entries describe recordings
on other contacts. A square matrix is not automatically symmetric and is not a
covariance matrix. Do not discard a triangle or invert it by default.

`voltage_mv / stim_current_ua` has units kΩ. We name this a **synthetic V/I proxy**;
that calculation alone does not reproduce a manufacturer's clinical impedance
algorithm. Current is positive, constant across contacts within a visit, and
stored in µA. Voltages are stored in mV. These are fixture conventions to verify
against the real export, including reference electrode, pulse timing, polarity,
compliance limits, units, and channel order.

Published IFT work describes recording voltages across 12 contacts, while clinical
electrode impedance and off-diagonal field measurements need distinct treatment.
See [the intracochlear electrical-field study (2022)](https://www.sciencedirect.com/science/article/pii/S2405844022032583)
and [electrode impedance and longitudinal modeling (2022)](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2022.886171/full).
The papers motivate the structure, not this generator's values or effects.

## Files and observation units

| File | Rows | One row represents | Unique key |
|---|---:|---|---|
| `patients.csv` | 96 | patient, with exactly one implant | `patient_id` (also `implant_id`) |
| `visits.csv` | 360 | implant measurement session | `visit_id` |
| `matrix_cells.csv` | 51,840 | directed contact pair at a visit | `visit_id`, `stim_contact`, `record_contact` |
| `visit_features.csv` | 360 | observed matrix summaries plus visit/patient metadata | `visit_id` |
| `prediction_pairs.csv` | 264 | current visit paired with its next observed scheduled visit | current `visit_id` |

Patients have scheduled windows at months 0, 1, 3, and 6. All have the first three;
24 lack month 6 due to simulated administrative truncation chosen independently
of measurements. Exact follow-up dates have small jitter. Month 0 means the
fixture's implantation-day baseline, not activation. Each patient has one implant;
bilateral implants would add another nesting level in real work.

### Patient fields

- `patient_id`, `implant_id`: synthetic identifiers, never model predictors.
- `age_at_implant_years`: six patients have missing age.
- `array_type`: fictional `array_A` / `array_B`, not actual product names.
- `site`: fictional `site_1`, `site_2`, `site_3`.
- `implant_side`: `left` or `right`; no side-specific mechanism is simulated.

### Visit fields

- `visit_id`, `patient_id`, `implant_id`: keys.
- `visit_month`: scheduled window 0 / 1 / 3 / 6.
- `days_since_implant`: actual elapsed days; `visit_date`: ISO calendar date.
- `protocol`: fictional v1/v2 measurement setting. Both occur at every window,
  with v2 more common later. There is an invented measurement offset for v2;
  dividing by current does not remove it.
- `stim_current_ua`: current used for this visit, either 100 or 150 µA.

### Matrix fields and QC

- `stim_contact`, `record_contact`: integers 1–12.
- `voltage_mv`: numeric recorded voltage, possibly missing or flagged invalid.
- `qc_status`: `ok`, `not_recorded`, or `saturated`.
- Exactly 144 cell records exist at every visit, even when voltage is unknown.
- `not_recorded` has missing voltage. `saturated` retains a finite placeholder
  voltage that must **not** enter summaries. Usable means status `ok` and finite
  voltage; unknown is never replaced by zero. No clinical threshold is taught.
- There is one deliberately unflagged local perturbation for exploratory review.
  An unusual pattern alone is not a disease/device-failure label.

### Ready-made features

These let the active modeling lessons run without finishing earlier exercises.
The active **Impedance ML Engineering** course restarted at Session 01 on
2026-10-05; see [the curriculum](../../agent/LEARNING_PLAN.md). They are deterministic
summaries of observed, QC-valid cells, not latent generator parameters or learned
features. No cross-patient fitting or future visits enter a current-visit feature.

- `diag_mean_kohm`, `diag_sd_kohm`: mean and sample SD (`ddof=1`) of valid diagonal
  V/I entries. `n_diag_valid`: contributing contacts (10–12).
- `near_mean_kohm`: mean of valid directed entries with index distance 1.
- `far_mean_kohm`: mean of valid directed entries with index distance ≥6.
- `months_since_implant`: actual elapsed days / 30, not exact calendar months.
- Every feature row also contains visit and patient fields. All 360 diagonal
  means are observed; missing age remains missing.

These summaries deliberately discard much spatial information. Their usefulness
is an exercise question, not an assertion that they are established biomarkers.

### Prediction table

Current-visit columns are copied from `visit_features.csv`. Added columns:

- `planned_horizon_months`: known scheduled interval, 1, 2, or 3 months.
- `target_visit_id`, `target_visit_month`: future identifiers for audit only.
- `target_diag_mean_kohm`: outcome observed at the next scheduled visit.

Pairs are only 0→1, 1→3, and 3→6 when both visits exist. No missing visit is
interpolated and no gap is skipped. Thus 96 + 96 + 72 = 264 pairs. This is a
retrospective benchmark among observed pairs; absence of the future visit cannot
be known at prediction time. Future protocol and exact future visit day are not
predictors. Correlated/overlapping pairs from one patient must stay together in
training, validation, and test allocation. The target is telemetry, not hearing
performance, complications, or a clinical decision.

## Reproducibility

From the repository root, using Python in `.venv`:

```bash
.venv/bin/python agent/generate_learning_data.py --dataset ci-telemetry
```

Default seed: 42, using an independent RNG. The command refuses to overwrite an
existing CI bundle. `--force` intentionally regenerates only this bundle; the
default general course datasets are a separate generator mode. Checked with
NumPy 2.5.2 and pandas 3.0.5.
