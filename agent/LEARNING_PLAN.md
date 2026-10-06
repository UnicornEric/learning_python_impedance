# Learning plan: Impedance ML Engineering

## Active purpose — reset 2026-10-05

The learner wants to relearn statistics, machine learning, and neural networks
for an ML engineering role, using impedance matrices close to their work field.
This is the complete replacement of the former general/interview preparation
course. Numbering restarts at 01. The scientific context stays constant so the
learner can compare statistical and ML approaches rather than relearn a new
unrelated dataset every session.

Machine learning and neural networks are the main emphasis. Introduce a useful
ML workflow in Session 02, feature engineering in 03, neural mechanics in 08,
and CNNs in 11. Statistical refresher sessions 04–05 and statistical reasoning
throughout are part of the route, not a long prerequisite detour. The course
culminates in a controlled benchmark, reproducible inference, and a technical
report. Do not promise that a neural model will outperform a simpler model.

## Learner and teaching priorities

- Experienced R data scientist with prior linear/mixed-model experience and
  introductory Python/ML practice. Python fluency still needs repeated practice.
- The learner explicitly requested relearning statistical analysis: revisit
  estimands, sampling variation, assumptions, intervals, diagnostics, effect
  sizes, confounding, and dependence even when familiar in R.
- Strengthen both implementation and judgment: inspect AI-generated code,
  diagnose failures, challenge leakage, justify metrics, and communicate results.
- Use R bridges briefly, then reinforce NumPy/pandas/sklearn/PyTorch idioms.
- Teach arrays, shapes, vectorization, functions, imports, and readable code in
  service of impedance questions. Do not return to a customer-data syntax track.
- Emphasize small, understandable CPU models and interpretable baselines. No GPU,
  external account, or network dataset is necessary for any core lesson.

## Curriculum and observable deliverables

Every notebook has a roughly 60-minute core, eight focused tasks, retrieval,
reasoning, reflection, and a separate optional extension. Allow more time when
new syntax or debugging requires it. These are sessions, not fixed calendar days.
Twenty cores represent about 20 hours before repetition and extensions.

| Session | Notebook / topic | Emphasis | Connected question |
|---|---|---|---|
| 01 | [Understand and audit the impedance matrices](../01_impedance_audit_and_exploration.ipynb) | Foundations | What does a matrix contain, and which patterns are measurement artifacts versus plausible research questions? |
| 02 | [Build the first patient-safe ML baseline](../02_first_patient_safe_ml_baseline.ipynb) | Classical ML | Can a simple ridge model improve on persistence for next-visit telemetry in unseen patients? |
| 03 | [Engineer interpretable spatial matrix features](../03_spatial_feature_engineering.ipynb) | Classical ML | Which information is lost by a diagonal mean, and can engineered features improve prediction? |
| 04 | [Refresh statistical modeling and uncertainty](../04_statistical_associations_and_uncertainty.ipynb) | Statistics | How is baseline telemetry associated with age and array type, and how uncertain are those associations? |
| 05 | [Model repeated measurements and temporal change](../05_longitudinal_mixed_models.ipynb) | Statistics | How much variation is between patients versus within patients, and how does telemetry change over follow-up? |
| 06 | [Compare trees and select models with grouped CV](../06_trees_grouped_cv_and_model_selection.ipynb) | Classical ML | Can nonlinear tabular models outperform ridge without exploiting patient leakage or a large search budget? |
| 07 | [Explore latent matrix structure with PCA](../07_pca_and_anomaly_exploration.ipynb) | Classical ML | Can low-dimensional matrix representations reveal structure, and what does an unusual reconstruction mean? |
| 08 | [Understand tensors, gradients, and optimization](../08_tensors_autograd_and_optimization.ipynb) | Neural networks | What exactly does a neural network compute and learn from impedance features? |
| 09 | [Train a small neural network end to end](../09_pytorch_mlp_training_loop.ipynb) | Neural networks | Can an MLP learn a useful telemetry predictor, and can you audit every stage of training? |
| 10 | [Control overfitting and debug neural training](../10_neural_regularization_and_debugging.ipynb) | Neural networks | How can you distinguish capacity, optimization, preprocessing, and evaluation problems? |
| 11 | [Build a CNN for directed impedance matrices](../11_cnn_for_impedance_matrices.ipynb) | Neural networks | Does preserving local contact-pair structure help compared with summaries or flattening? |
| 12 | [Combine a CNN with metadata and test ablations](../12_matrix_metadata_fusion_and_ablation.ipynb) | Neural networks | Does a matrix encoder add information beyond current summaries and known follow-up horizon? |
| 13 | [Learn representations with masked autoencoders](../13_autoencoders_and_masked_reconstruction.ipynb) | Neural networks | Can unsupervised compression capture useful matrix structure without learning QC placeholders? |
| 14 | [Refresh classification with an explicit teaching endpoint](../14_classification_and_logistic_baselines.ipynb) | Classification | Can current matrices forecast whether the next synthetic diagonal mean exceeds a fixed teaching cutoff? |
| 15 | [Calibrate probabilities and choose a decision rule](../15_calibration_thresholds_and_decisions.ipynb) | Classification | Are predicted probabilities meaningful, and how does a chosen error cost affect the operating threshold? |
| 16 | [Use history without leaking the future](../16_temporal_forecasting_and_history_features.ipynb) | Temporal modeling | How does forecasting later visits for known patients differ from generalizing to entirely new patients? |
| 17 | [Quantify model uncertainty and inspect shift](../17_uncertainty_shift_and_robustness.ipynb) | ML evaluation | How stable is a model advantage, and how might measurement or population shift break it? |
| 18 | [Turn a notebook model into a reproducible inference artifact](../18_reproducible_inference_and_model_artifacts.ipynb) | ML engineering | Can a colleague reproduce predictions from raw current-visit inputs without your notebook state? |
| 19 | [Capstone: design and run a controlled development benchmark](../19_capstone_development_benchmark.ipynb) | Capstone | Which representation and model would you choose for next-visit prediction, given accuracy, evidence, and engineering cost? |
| 20 | [Capstone: final evaluation, robustness, and technical handoff](../20_capstone_final_evaluation_and_report.ipynb) | Capstone | What does one final patient-holdout evaluation support, and what would still be needed at work? |

Deliverables by stage:

- 01–03: a matrix/QC report, leakage-safe baseline, feature specification, and
  validation prediction table.
- 04–07: effect estimates with uncertainty/diagnostics, longitudinal model,
  bounded grouped-CV comparison, and PCA/loading/reconstruction plots.
- 08–13: shape/gradient reasoning, audited training loop, regularization log,
  CNN-versus-flattening comparison, modality ablations, and masked autoencoder.
- 14–17: explicit teaching classification endpoint, calibration/decision record,
  historical-feature availability contract, and patient-bootstrap/shift analysis.
- 18–20: reproducible local inference artifact, frozen benchmark selection, and
  final report/model card with a defensible patient-holdout evaluation.

Default route is sequential, but use reflections to repeat or split difficult
sessions. Advanced architecture extensions (1D CNN, GRU, denoising, grouped nested
CV) are optional. There are only three or four visits per patient: a sequence
model is a shape/implementation exercise until denser data justify it. A graph
model or larger attention model needs a confirmed physical topology and a
scientific question; do not add it just to expand a framework checklist.

## Data and scientific contract

Use the existing local bundle `data/ci_telemetry/` and its README as the source of
truth. It is entirely synthetic: 96 patients, one implant per patient, 360 visits,
51,840 cells, and 264 adjacent-window prediction pairs. All labels/effects are
fictional; no actual workplace export, hearing outcome, or clinical diagnosis is
available. Keep raw CSV files unchanged.

- Matrix shape: 12 stimulation rows × 12 recording columns; ordered contact
  labels 1–12. Directed cells are not assumed symmetric. Contact-index distance
  is not physical distance; the matrix is not a covariance matrix by default.
- Voltage mV divided by current µA gives a synthetic kΩ V/I proxy. Confirm real
  manufacturer definitions before applying this transform at work.
- Validity: `qc_status == "ok"` AND finite voltage. Finite saturated readings are
  invalid. Preserve masks; missing is not measured zero.
- Hierarchy: patient → implant → visit → directed cell. The fixture has one
  implant per patient. Bilateral implants/technical repeats need extra keys.
- Scheduled visits: months 0,1,3,6 with actual timing jitter; 24 patients lack the
  last visit due to synthetic administrative truncation independent of values.
- Supplied visit features are deterministic summaries of current observed cells,
  with no cross-patient learning or future observations.
- Shared regression target: next scheduled visit's observed diagonal mean from
  current-visit matrix/metadata and known planned horizon, for unseen patients.
  Pairs are 0→1,1→3,3→6 only; no interpolation or skipped window.
- Classification sessions define `target_diag_mean_kohm > 7.0` purely as a fixed
  coding endpoint. It is not a clinical threshold or failure label. Probability
  thresholds in Session 15 are separate from this outcome-definition cutoff.
- Session 16 deliberately changes the estimand to later-time forecasting for
  known development patients; it must not be compared as the same benchmark.

Keep generic older datasets and the existing data generator available for
history, but do not make them prerequisites or alternate the active course back
to unrelated modalities. The generator protects existing data unless `--force`
is requested. To generate a missing CI bundle only:

```bash
.venv/bin/python agent/generate_learning_data.py --dataset ci-telemetry
```

## Evaluation discipline

Use a fixed patient allocation derived from prediction pairs:

1. GroupShuffleSplit test_size=0.25, seed 42 reserves 24 test patients.
2. Split the remaining 72 patients with test_size=0.25, seed 43: 54 train and
   18 validation patients. Pair counts are 146 train, 51 validation, 67 test.
3. Inspect IDs/shapes for structural assertions. Test outcomes and model scores
   stay reserved until Session 20; never use test for feature selection, scaler
   fitting, calibration, early stopping, architecture choice, or seed choice.
4. For grouped CV, use train+validation as development and learn transformations
   separately in each training fold. Pass groups explicitly to splitters/search.
5. Earlier validation is repeatedly reused for learning: label it exploratory.
   Do not portray reused validation as independent scientific evidence. Full-data
   descriptive EDA in Session 01 also means this is a teaching benchmark, not a
   prospectively pristine external study.
6. Compare models on the same rows, patient allocation, target, information
   available at prediction time, metric, and a recorded tuning/computing budget.
   Distinguish representation gains from simply adding metadata or horizon.
7. Report MAE in kΩ, lower is better. Primary capstone metric is patient-average
   MAE; also report pair-average MAE. Negative model-minus-persistence favors
   the model. Classification requires probability quality and decision metrics.
8. Bootstrap patients and retain repeated sampled clusters. Do not treat visit
   pairs or cells as independent. State what uncertainty is conditional on.
9. Early stopping uses patient-separated validation; save a deep copy of the
   best state and restore it. Disable implicit row-based early stopping in
   estimators for grouped experiments unless safely configured.
10. Freeze the final candidate before revealing test. If refitting on all 72
    development patients, freeze the epoch count from development experiments.
    After test inspection, new model changes are future exploratory experiments.

## Notebook teaching specification

Lesson filenames use two-digit numbering and snake_case; new notebooks live in
the root. All 20 initial lessons were generated at reset but none is completed.

Each notebook includes:

1. Track/session title and core duration.
2. A connected question and why it matters.
3. Three to five observable objectives.
4. A short R-to-Python/prerequisite bridge and practical API/concept reminders.
5. Pacing, data contract, and explicit input/target availability.
6. Eight tasks in increasing difficulty, each followed by an empty code cell.
7. Retrieval with reduced scaffolding.
8. Two to four professional reasoning questions, including what could go wrong.
9. Confidence 1–5, hardest point, what is explainable, repetition needs, workload.
10. An optional extension outside the core hour and official API references.

Exercise cells are genuinely empty: no pass, placeholders, pseudo-solutions,
outputs, or execution counts. Put tiny examples and API reminders in markdown;
worked examples use unrelated data. Later setup scaffolding can supply input
representations so previous answers are not execution dependencies. The helper
`agent/course_data.py` loads/aligns current data and fixed indices only; it does
not fit preprocessing, build learned features, or train models.

First exposure: define inputs, expected output, method/import, and one hint.
Second exposure: goal and a useful reminder. Later exposure: goal and acceptance
criteria unless review evidence shows a need for more scaffolding. Require a
predicted shape/type/count before execution at least once per session. Include
code auditing/debugging and plain-language interpretation regularly. Validate
join cardinality and unmatched keys; never let pivot_table silently hide duplicates.

Teach both statistical and neural concepts explicitly: the learner requested a
refresher, so explain assumptions and mechanics instead of only naming APIs.
Compare uncertainty about an association, an individual future observation,
and model performance. Revisit Python syntax through each scientific workflow.

## Adaptive interaction and review

When the learner asks for help, start with a conceptual nudge, then a concrete
hint/unrelated example. Give a full solution only when explicitly requested or
after repeated unsuccessful attempts with the learner asking for more help.
Follow revealed solutions with a near-transfer question. Do not solve all lesson
exercises or create solution notebooks preemptively.

When reviewing, state correct reasoning first, then correctness, QC/leakage,
evaluation/interpretation, and readability. Preserve attempts; review in chat or
new markdown comments when requested. AI audits should inspect input/output
shapes, mutation, fitted transformations, row order, availability, split groups,
loss/metric direction, and assertions that expose silent errors.

If asked "next lesson", consult progress and choose the next unfinished session,
not the next ungenerated file. Do not infer mastery from notebook creation or
author checks. Completion requires learner confirmation or review of substantive
attempted work; record confidence only when supplied. Carry repeated difficulties
into the next lesson. A request to jump ahead is allowed, with a short prerequisite
bridge rather than unrelated remedial notebooks.

## Repository and environment contract

- Active notebooks: root, starting `01_`; historical material:
  `pre_employment_learning/`, including old archive structure and instruction copies.
- Archive notebook bytes/answers/outputs are preserved. Its manifest records hashes.
  Do not renumber, solve, or apply its former curriculum as the active specification.
- Shared CSV data and `.venv` remain. No environment reset or unrelated upgrades.
- Active instructions/progress: `AGENTS.md`, `agent/LEARNING_PLAN.md`, and
  `agent/PROGRESS.md`. `agent/MED_EL_RESEARCH_PATH.md` points to the new course.
- Learner output: session-specific `artifacts/NN/`; engineering exercises may add
  `src/impedance_ml/`; capstone output: `artifacts/capstone/`.
- Use existing `.venv`: NumPy, pandas, SciPy, Matplotlib/plotnine, statsmodels,
  scikit-learn, optional XGBoost, PyTorch, and Jupyter. Add only needed dependencies.
- Check actual imports before introducing a package. No GPU is required. Prefer
  Matplotlib for matrix/learning-curve plots; plotnine remains an optional R bridge.
- Do not silently regenerate data, overwrite attempted notebooks, or install
  unrelated packages. Missing packages: `.venv/bin/python -m pip install -r requirements.txt`.

Launch the first session from the root:

```bash
.venv/bin/python -m jupyterlab 01_impedance_audit_and_exploration.ipynb
```

Choose **Python (learning-python)**. A fresh kernel should run attempted cells in
order. Later notebooks have input scaffolding independent of previous answers;
conceptual prerequisites are specified by the route.

## Author verification and future changes

Before handoff verify notebook schema, empty exercises/counts/outputs, section
order, numbering, relative paths, imports, data alignment/QC, split invariants,
and representative model/plot APIs. Run meaningful validation in temporary author
scripts; do not inject solutions into learner notebooks. Record author checks
separately from learner completion. Preserve old plan/progress snapshots if the
learner later requests another reset.
