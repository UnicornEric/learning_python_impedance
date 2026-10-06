# Learning progress

## Current position

- Active track: General Data Science Track
- Current focus: MED-EL research preparation, requested 2026-09-21; start Session 04 (matrix EDA) or Session 05 for immediate statistical-modeling practice.
- Last completed: Day 1 / Phase 1.1 (learner confirmed 2026-09-15)
- Next sequence: Sessions 04–07 (matrix exploration → OLS → mixed models → patient-grouped prediction), all generated and independently runnable; completion unconfirmed.
- Day 3 remains partially attempted. Task 4 timezone conversion reviewed; Task 5 grouped differences were correct, with assignment and assertions still to complete at review. No whole-lesson completion inferred.
- Day 2 completion remains unconfirmed; requesting Day 3 does not mark it complete.
- Naming: from Day 3 onward, new notebook prefixes match the official task number (learner request, 2026-09-17).
- Default lesson length: 60 minutes
- Track reset: 2026-09-08, after the interview-focused goal ended

## Active-track lessons

| Notebook | Curriculum ID | Generated | Completed | Confidence | Notes |
|---|---|---|---|---|---|
| `archive/General Learning/01_data_wrangling_and_cleaning.ipynb` | GDS Day 1 / Phase 1.1 | 2026-09-08 | Yes (confirmed 2026-09-15) | — | Previously recorded as `06_data_wrangling_and_cleaning.ipynb`; now located in archive. Learner: "finished this one last. this is essentially day one." |
| `archive/07_systematic_cleaning_and_validation.ipynb` | GDS Day 2 / Phase 1.2 | 2026-09-15 | No | — | 60 minutes: selection/indexing, safe assignment, strings, categories, missing/invalid ages, duplicate conflicts, assertions, and completeness reporting. Uses a fixed synthetic import. Archived with learner attempts preserved; prefix reflects the earlier sequence, conceptual day remains 2. |
| `03_dates_and_longitudinal_data.ipynb` | GDS Day 3 / Phase 1.3 | 2026-09-17 | No | — | 60 minutes: audited date parsing, explicit observation windows, UTC/Vienna time conversion, customer purchase gaps and recency, daily calendars, trailing windows, and plotnine interpretation. Uses existing transactions plus an inline synthetic timestamp probe. Numbered 03 rather than 08 at learner request. |
| `04_ci_matrix_exploration.ipynb` | GDS 04 / adapted Phases 1.4, 2.1–2, 4 structured matrices | 2026-09-21 | No | — | 60 minutes: synthetic 12×12 telemetry, hierarchy, QC, voltage/current units, heatmaps, profiles, diagonal versus off-diagonal summaries, patient context, exploratory research note. |
| `05_ci_linear_models.ipynb` | GDS 05 / adapted Phase 2.4 | 2026-09-21 | No | — | 60 minutes: baseline patient sample, plotnine EDA, statsmodels OLS, coefficient intervals, residual/influence diagnostics, HC3 sensitivity, adjusted mean plots. |
| `06_ci_longitudinal_mixed_models.ipynb` | GDS 06 / adapted Phase 2.7 | 2026-09-21 | No | — | 60 minutes: individual trajectories, protocol/time confounding, pooled versus patient random-intercept models, ICC, population versus conditional predictions. |
| `07_ci_prediction_without_patient_leakage.ipynb` | GDS 07 / adapted Phase 3.1–3 | 2026-09-21 | No | — | 60 minutes: next-visit telemetry target, persistence baseline, patient holdout, preprocessing/ridge pipeline, grouped CV, pair- versus patient-weighted MAE. |

## Concepts to repeat

- Constructing pandas operations fluently: selection, assignment, groupby,
  aggregation, and merging.
- Making row granularity explicit before aggregation, joins, or modeling.
- Checking missingness and deciding whether a value is absent, unknown, or truly
  zero.
- Validating key uniqueness and join cardinality with explicit checks.
- Reading object types, shapes, and fitted object structure without guessing.
- Reconstructing leakage-safe modeling workflows in later ML lessons.

- Day 2 deliberately revisits selection/sorting, object types, and explicit assertions from Day 1. No mastery or confidence inferred; Day 1 attempts preserved.
- Day 3 revisits Series versus DataFrame shapes, missingness audits, grouping, sorting, and assertions. Generation does not establish completion or mastery.
- Learner requested a more research-focused direction on 2026-09-21: imminent MED-EL role, 12×12 telemetry matrices plus patient information; wants statistical modeling, visualization, and exploratory analysis. Real matrix semantics and repeated-measurement structure remain unconfirmed; the synthetic assumptions are documented explicitly.
- Author validation for Sessions 04–07 (2026-09-21): notebook schemas and empty exercise cells checked; fixture regeneration matched saved tables; QC/feature reconciliation, OLS/HC3, warning-free converged random-intercept fit, and patient-separated holdout/CV pipeline exercised successfully. Representative heatmap, adjusted-mean, and trajectory plots rendered and inspected. This validates lesson setup, not learner completion. Registered `learning-python` inside the existing `.venv` for local Jupyter use.
- Day 3 review suggests continuing to reinforce assigning a computed Series back to a column, grouped differencing, and expressing checks as assertions in the scientific exercises.

## Data-modality coverage

- Relational tabular data: current
- Longitudinal/time series: Day 3 partially attempted; CI trajectories/mixed models in Session 06 generated, not completed
- Structured scientific matrices: CI telemetry Session 04 generated, not completed
- Statistical modeling: CI OLS and mixed-model Sessions 05–06 generated; learner has strong R background
- Classical machine learning: prior exposure; patient-grouped CI prediction Session 07 generated, not completed
- Unsupervised learning: planned
- Text: planned
- Images: planned
- Geospatial/network or event data: planned
- Neural networks: planned
- Experiments/causal reasoning: planned

## Earlier interview-sprint history

These notebooks are retained as completed or optional learning history. The two
unfinished sprint notebooks are not prerequisites for the active track.

| Notebook | Curriculum ID | Generated | Completed | Confidence | Notes |
|---|---|---|---|---|---|
| `01_python_to_ml_baseline.ipynb` | Sprint 1A + 1B | 2026-08-25 | Yes (2026-08-25) | 2/5 | Took roughly 3–4 hours including breaks; metrics became clearer, while preprocessing pipelines and fitted-model syntax needed repetition. |
| `02_confusion_matrices_and_thresholds.ipynb` | Sprint 1C | 2026-08-25 | Yes (2026-08-28) | — | Learner confirmed completion. |
| `03_cross_validation_and_tuning.ipynb` | Sprint 2A + 2B | 2026-08-26 | Yes (2026-08-28) | — | Focused on rerunning the ML pipeline and cross-validation; learner requested repetition. |
| `04_trees_ensembles_and_xgboost.ipynb` | Sprint 3A | 2026-08-28 | No | — | Optional 60-minute classification/model-comparison lesson. |
| `05_regression_workflow_with_xgboost.ipynb` | Sprint 3B | 2026-08-28 | No | — | Optional 60-minute regression workflow. |
