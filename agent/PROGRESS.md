# Progress: Impedance ML Engineering

Reset: **2026-10-05**, at the learner’s explicit request.

- Active track: impedance-focused ML engineering, classical ML and neural networks.
- Current position / next session: **01 — Impedance audit and exploration**.
- Generated: 20 notebooks. Completed in this track: **0**. Confidence: unreported.
- Default core duration: about 60 minutes; repeat/split based on learner feedback.
- No deadlines or fixed calendar schedule. Prior course completion does not imply
  new-track completion; the reset does not erase learning history.

## Active lessons

| Session | Notebook | Generated | Completed | Confidence |
|---|---|---|---|---|
| 01 | [01_impedance_audit_and_exploration.ipynb](../01_impedance_audit_and_exploration.ipynb) | 2026-10-05 | No | — |
| 02 | [02_first_patient_safe_ml_baseline.ipynb](../02_first_patient_safe_ml_baseline.ipynb) | 2026-10-05 | No | — |
| 03 | [03_spatial_feature_engineering.ipynb](../03_spatial_feature_engineering.ipynb) | 2026-10-05 | No | — |
| 04 | [04_statistical_associations_and_uncertainty.ipynb](../04_statistical_associations_and_uncertainty.ipynb) | 2026-10-05 | No | — |
| 05 | [05_longitudinal_mixed_models.ipynb](../05_longitudinal_mixed_models.ipynb) | 2026-10-05 | No | — |
| 06 | [06_trees_grouped_cv_and_model_selection.ipynb](../06_trees_grouped_cv_and_model_selection.ipynb) | 2026-10-05 | No | — |
| 07 | [07_pca_and_anomaly_exploration.ipynb](../07_pca_and_anomaly_exploration.ipynb) | 2026-10-05 | No | — |
| 08 | [08_tensors_autograd_and_optimization.ipynb](../08_tensors_autograd_and_optimization.ipynb) | 2026-10-05 | No | — |
| 09 | [09_pytorch_mlp_training_loop.ipynb](../09_pytorch_mlp_training_loop.ipynb) | 2026-10-05 | No | — |
| 10 | [10_neural_regularization_and_debugging.ipynb](../10_neural_regularization_and_debugging.ipynb) | 2026-10-05 | No | — |
| 11 | [11_cnn_for_impedance_matrices.ipynb](../11_cnn_for_impedance_matrices.ipynb) | 2026-10-05 | No | — |
| 12 | [12_matrix_metadata_fusion_and_ablation.ipynb](../12_matrix_metadata_fusion_and_ablation.ipynb) | 2026-10-05 | No | — |
| 13 | [13_autoencoders_and_masked_reconstruction.ipynb](../13_autoencoders_and_masked_reconstruction.ipynb) | 2026-10-05 | No | — |
| 14 | [14_classification_and_logistic_baselines.ipynb](../14_classification_and_logistic_baselines.ipynb) | 2026-10-05 | No | — |
| 15 | [15_calibration_thresholds_and_decisions.ipynb](../15_calibration_thresholds_and_decisions.ipynb) | 2026-10-05 | No | — |
| 16 | [16_temporal_forecasting_and_history_features.ipynb](../16_temporal_forecasting_and_history_features.ipynb) | 2026-10-05 | No | — |
| 17 | [17_uncertainty_shift_and_robustness.ipynb](../17_uncertainty_shift_and_robustness.ipynb) | 2026-10-05 | No | — |
| 18 | [18_reproducible_inference_and_model_artifacts.ipynb](../18_reproducible_inference_and_model_artifacts.ipynb) | 2026-10-05 | No | — |
| 19 | [19_capstone_development_benchmark.ipynb](../19_capstone_development_benchmark.ipynb) | 2026-10-05 | No | — |
| 20 | [20_capstone_final_evaluation_and_report.ipynb](../20_capstone_final_evaluation_and_report.ipynb) | 2026-10-05 | No | — |

## Concepts to revisit

Carried from prior review evidence, without inferring new-track mastery:

- pandas selection/assignment/groupby and saving computed Series into columns.
- Row grain, join keys/cardinality, assertions, missingness versus zero.
- Shape/type prediction, fitted objects, and readable intermediate variables.
- Leakage-safe preprocessing, grouped validation, metrics, and interpreting plots.

New priorities explicitly requested at reset: spatial feature engineering,
classical ML, neural networks/CNNs, statistical refreshers, and practical ML
engineering. Record confidence and difficulties after actual lesson feedback.

## Historical learning

All 12 prior notebooks, including existing archives, are preserved in
[`pre_employment_learning/`](../pre_employment_learning/README.md). Original
progress and plans are copied to `course_instructions/`. Their recorded
completion/partial-attempt status remains historical; do not mark unfinished
legacy lessons complete or make them prerequisites. See the manifest for paths
and SHA-256 hashes. Current course numbering starts at 01 independently.

## Author validation

Validated on 2026-10-05 in the existing `.venv`:

- All 12 archived notebook hashes and four former instruction-file hashes match.
- All 20 notebooks pass nbformat validation; numbering, section order, eight core
  tasks, 12 empty code cells, clear counts/outputs, and Python reminder syntax checked.
- Active Markdown links and the registered `learning-python` kernel checked.
- Directed matrix reconstruction, QC masks, supplied feature reconciliation,
  and 54/18/24 patient partitions (146/51/67 pairs) checked.
- Ridge/grouped CV, forest/boosting, PCA, OLS/HC3, warning-free converged mixed
  model, clustered binomial GLM, grouped OOF calibration, and temporal outcome
  availability exercised using temporary author scripts.
- Tensor/autograd checks, decreasing MLP training loss, CNN shapes/gradients,
  metadata fusion, masked autoencoder loss, and BCE logits checked.
- Representative heatmap/prediction plots rendered and visually inspected;
  saved sklearn pipeline reload reproduces predictions.

No full exercise solutions were added to learner notebooks. These are author
setup/sanity checks, not exhaustive execution of every proposed experiment,
and not learner completion or mastery.
