# Codex learning plan: General data science in Python

## Purpose

This file is the durable specification for an adaptive, notebook-based Python
course for an experienced R data scientist. The active goal is broad, practical
data-science fluency rather than preparation for a particular interview. The
course covers acquiring, validating, cleaning, transforming, visualizing, and
modeling many kinds of data; statistical inference; classical machine learning;
neural networks; evaluation; communication; and reproducible workflows.

The course is exercise-first. Each notebook should make the learner write, read,
explain, debug, and evaluate Python. Lessons should build the judgment needed to
inspect, adapt, and challenge AI-generated work, not merely reproduce syntax.

## Immediate priority — MED-EL research preparation (2026-09-21)

The learner is starting as a research engineer at MED-EL soon and expects to work
with cochlear-implant field/impedance telemetry in 12×12 matrices plus patient
information. They requested that upcoming notebooks move closer to exploratory
research, visualization, basic statistical modeling, and ML. This practical
priority supersedes the generic curriculum order below; the wider curriculum
remains background, not a prerequisite checklist.

- Use a connected scientific question and realistic observation hierarchy, with
  clearly labeled synthetic data until the actual export is understood.
- Confirm matrix axes, units, diagonal meaning, channel order, measurement
  protocol, QC, and repeated patient/implant/session structure. Do not imply
  knowledge of MED-EL's internal schema or derive clinical thresholds from toys.
- Revisit Python syntax while doing EDA and models, rather than requiring more
  unrelated customer/transaction exercises first.
- Emphasize plot interpretation, effect sizes/uncertainty, OLS diagnostics,
  mixed-effects models, patient-aware validation, and useful baselines.
- Start with sessions 04–07: matrix exploration; baseline linear models;
  longitudinal mixed models; next-visit prediction without patient leakage.
  Each is independently runnable with the local CI teaching bundle. Sessions
  05–07 include ready-made observed features so prior wrangling is not a blocker.
- Keep eight focused core tasks, retrieval, and reflection per 60-minute session.
  First-exposure model and plotting syntax belongs in short markdown reminders;
  executable exercise cells remain empty.
- Do not mark earlier unfinished notebooks complete when changing direction.
- After these sessions, use learner feedback to choose deeper matrix features,
  PCA, functional/spatial modeling, patient outcomes, or another research question.

The route and data-owner questions are in `agent/MED_EL_RESEARCH_PATH.md`.

## Learner profile

- Experienced data scientist coming from R.
- Strong in data wrangling and statistical reasoning.
- Comfortable with linear models, generalized linear models, and mixed-effects
  models in R.
- Python coding confidence began around 2/10 and is still developing.
- Has completed introductory practice with pandas, plotnine, scikit-learn
  pipelines, classification metrics, cross-validation, and tuning, but wants the
  full workflow repeated until it feels natural.
- Python visualization is rusty; use `plotnine` first when its grammar provides a
  helpful bridge from `ggplot2`, while gradually introducing Matplotlib where it
  is the clearer or more standard tool.
- Has basic conceptual machine-learning knowledge and limited neural-network
  implementation experience.
- Expects AI to write substantial production code, but wants enough fluency to
  inspect, explain, debug, adapt, test, and challenge it.

Do not reteach statistical theory the learner already knows unless the Python
translation, computational implementation, or predictive interpretation differs.
Use R as a bridge, then deliberately strengthen Python-native habits.

## Learning principles

- Start with a real question and data object, then introduce syntax in service of
  the analysis.
- Treat data quality, validation, provenance, and leakage prevention as part of
  every workflow rather than a preliminary chore.
- Revisit core operations through spaced retrieval and different data contexts.
- Alternate statistical explanation with predictive evaluation; make clear when
  the goal is inference, description, forecasting, or decision support.
- Compare sophisticated models with simple, credible baselines.
- Require plots and metrics to be interpreted in plain language.
- Use varied modalities progressively: relational tables, longitudinal and time
  series data, text, images, and, when useful, geospatial or network-shaped data.
- Prefer small local or package-bundled datasets so notebooks remain reproducible
  and CPU-friendly. Avoid credentials and downloads in core exercises.
- End major modules with an integrated analysis or mini-project rather than a
  syntax quiz.

## Standard technical stack

Use a coherent stack and add libraries only when the lesson needs them:

- Python 3.12+ and Jupyter notebooks
- NumPy for arrays, simulation, vectorization, and numerical foundations
- pandas for tabular, relational, and time-indexed data
- plotnine for grammar-of-graphics work; Matplotlib for lower-level control,
  image displays, and plots plotnine does not handle well
- SciPy for distributions, tests, sparse matrices, optimization, and scientific
  utilities when appropriate
- statsmodels for formula-oriented inference, linear models, GLMs, time-series
  models, and mixed models
- scikit-learn for preprocessing, classical ML, pipelines, validation, tuning,
  metrics, unsupervised learning, text features, and bundled datasets
- XGBoost for focused boosted-tree comparisons after tree fundamentals and
  leakage-safe evaluation are established
- PyTorch for neural networks, tensors, autograd, image models, and embeddings
- pathlib and standard-library modules for reproducible file and workflow code

Use Pillow or another lightweight specialist library only when a later data
modality requires it. Do not turn the course into a framework tour. Prefer
transferable mental models and readable intermediate variables.

## Repository contract

- Lesson notebooks live in the repository root.
- Name new active-track notebooks with the two-digit task/session number and a
  concise snake_case subject, for example `03_dates_and_longitudinal_data.ipynb`
  for Day 3. Per learner request on 2026-09-17, active-track numbering follows
  the official task number rather than continuing the legacy sprint sequence.
- Never overwrite an existing lesson notebook or renumber archived learner work
  unless explicitly requested. Archived prefixes may reflect the old sequence.
- The earlier interview-sprint notebooks remain as learning history. They do not
  need to be completed before lessons in the active general data-science track.
- Generated datasets live in `data/` and are created by
  `agent/generate_learning_data.py`.
- Durable instructions and progress records live in `agent/`.
- Record generated and completed lessons separately in `agent/PROGRESS.md`.
- A notebook is only completed after the learner says it is complete or asks for
  review of attempted answers. Generation or cell execution alone is not
  completion.
- Never modify learner attempts unless explicitly asked. Give review comments in
  chat or in new markdown cells only when requested.
- Do not create solution notebooks preemptively. If explicitly requested, use a
  clearly marked path such as
  `solutions/06_data_wrangling_and_cleaning_solution.ipynb` and preserve the
  learner notebook.

## Environment bootstrap

The repository virtual environment is `.venv` and dependencies are declared in
`requirements.txt`. Before a lesson first uses a package, check that it imports
with `.venv/bin/python`. Do not replace the environment or upgrade unrelated
packages.

If dependencies are missing, name them and use:

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name learning-python --display-name "Python (learning-python)"
```

Installing packages or a kernel may require network access or approval. Request
it when needed. Do not pin arbitrary old versions; add a constraint only to fix a
demonstrated compatibility problem.

## How to interpret routine requests

The active track is the General Data Science Track. When asked for "Day N", the
"next lesson", or "another lesson", inspect existing notebooks and
`agent/PROGRESS.md`, then choose the next unfinished or requested session in this
track. Do not route back to the old interview sprint unless explicitly asked.

The default lesson length is 60 minutes:

- 15 minutes: 2–3 tightly scoped tasks plus one retrieval question.
- 30 minutes: 4–6 tasks, normally 5–8 empty code cells.
- 60 minutes: 8–12 focused tasks that form one coherent analysis.
- More than 60 minutes: create multiple numbered notebooks unless the learner
  explicitly requests a workshop in one file.

If the learner names a topic, adapt the next lesson to it while preserving needed
prerequisites. If it is advanced, include a concise prerequisite bridge in the
same notebook rather than blocking progress. The curriculum map is a route, not a
calendar: repeat, combine, or split topics in response to demonstrated progress.

## Notebook teaching specification

Every lesson notebook must contain, in this order:

1. A title with General Data Science Track day/session, topic, and estimated time.
2. A short "Why this matters" paragraph tied to real data-science work.
3. Three to five observable learning objectives.
4. A compact "R to Python bridge" when relevant.
5. A suggested pacing guide for lessons of 30 minutes or longer.
6. Tasks in increasing difficulty, each followed immediately by one or more empty
   executable code cells.
7. A retrieval-practice section revisiting an earlier operation with less
   guidance.
8. Two to four professional reasoning questions, including at least one "explain
   why" or "what could go wrong" question.
9. A self-check: confidence 1–5, hardest point, one thing now explainable, and what
   deserves repetition.
10. An optional extension clearly outside the estimated core duration.

Code-cell rules:

- Exercise cells are genuinely empty: no solution, pseudocode, placeholder,
  ellipsis, or `pass`.
- Outputs and execution counts are empty.
- Put API reminders, signatures, and tiny worked examples in markdown fenced
  blocks, not executable cells.
- A worked example must use different data from the learner's task.
- On first exposure, provide inputs, desired output, relevant methods, and one
  hint. On second exposure, state the goal and perhaps one method. On later
  exposure, state the goal and acceptance criteria unless progress shows
  difficulty.
- Never hide essential instructions in code comments.

Task-design rules:

- Prefer purposeful tasks over prompts such as "explore the data".
- Include shapes, key names, metric direction, invariants, or qualitative plot
  descriptions so answers can be checked without a solution.
- Ask for a type, shape, row-count, or model-output prediction before execution at
  least once per lesson.
- Include code reading or debugging frequently.
- Keep boilerplate low but do not prefill imports during early practice. Later
  lessons may supply a compact import/setup cell when setup is not the objective.
- Use fixed seeds and fixed analysis reference dates where reproducibility matters.
- Make row granularity explicit before joins, aggregation, statistical modeling,
  or evaluation.
- Validate join cardinality with `validate=` and inspect unmatched keys when
  relational data is used.
- Avoid leakage: split before learned preprocessing, put preprocessing inside
  pipelines, and keep the final test set untouched until selection is finished.
- Require both a quantitative result and a plain-language interpretation.
- Regularly ask what conclusion is not justified by the analysis.

## Adaptive teaching and AI interaction

The learner should struggle productively without getting stuck indefinitely.

When asked for help:

1. Offer a conceptual nudge or point to the relevant object or method.
2. If still stuck, give a concrete hint or a minimal unrelated example.
3. Show the full solution only after an explicit request or repeated failed
   attempts.
4. Explain non-obvious lines, alternatives, expected shapes/types, and failure
   modes when revealing a solution.
5. Follow a revealed solution with a short near-transfer exercise.

When reviewing code, report what is correct first, then correctness bugs, data
quality/leakage/evaluation issues, readability, and an idiomatic alternative.
Favor readable intermediate variables over cleverness while confidence is low.

Regularly require an audit of AI-generated code:

- What are the input/output types, shapes, and row granularity?
- Which operations mutate data, discard observations, or learn from data?
- Are keys unique where assumed, and does a join multiply rows?
- Could validation/test or future information leak into the result?
- Which defaults materially affect the answer?
- Does the metric or estimand match the scientific/business question?
- What simple baseline should this beat?
- What assertions would reveal a silent error?

## High-value R-to-Python bridges

| R / tidyverse idea | Python equivalent to teach |
|---|---|
| `<-` | `=` assignment |
| vector | list, NumPy `ndarray`, or pandas `Series` by purpose |
| `data.frame` / tibble | pandas `DataFrame` |
| `df$column` | `df["column"]`; attribute access only when safe |
| `%>%` / `|>` | readable method chains and intermediate variables |
| `select()` | column list, `.loc[:, columns]`, `.filter()` |
| `filter()` | boolean masks, `.loc[...]`, `.query()` |
| `mutate()` | assignment or `.assign()` |
| `summarise()` | `.agg()` |
| `group_by()` | `.groupby()` plus aggregation or transformation |
| joins | `.merge(..., validate=...)` |
| `pivot_longer()` | `.melt()` |
| `pivot_wider()` | `.pivot()` / `.pivot_table()` |
| factors | categorical dtype and explicit category order |
| `NA` handling | `isna`, `dropna`, `fillna`, sklearn imputers |
| lubridate | pandas `.dt` accessors, offsets, and periods |
| ggplot2 | plotnine; Matplotlib for lower-level or specialist plots |
| `lm()` / formulas | statsmodels formula API; sklearn for prediction |
| `glm()` | statsmodels GLM for inference; sklearn estimators for prediction |
| mixed-effects model | statsmodels `mixedlm` |

Repeat Python-specific ideas that do not map cleanly from R: indentation,
zero-based indexing, mutability, views versus copies, truth-value ambiguity,
methods versus attributes, imports/namespaces, iterables, functions, exceptions,
classes at a reading level, and object shapes.

## General Data Science Track curriculum

The phases below establish prerequisite order. Each numbered item is usually one
60-minute lesson, but it may be split or repeated. Integrated projects should use
reduced scaffolding and combine skills from several earlier lessons.

### Phase 1 — Python, data wrangling, and data quality

1. Audit, clean, transform, aggregate, and validate a relational customer and
   transaction dataset; communicate one defensible descriptive finding.
2. Selection, indexing, assignment, missingness, duplicates, invalid values,
   strings, categories, and systematic validation assertions.
3. Dates, times, time zones, durations, rolling windows, and longitudinal shape.
4. Safe joins, key/cardinality diagnosis, reshape, groupby versus transform, and
   feature engineering at explicit observation grains.
5. Functions, reusable cleaning helpers, exceptions, type hints, and small tests.
6. Files, pathlib, CSV/JSON/parquet concepts, reproducible inputs/outputs, and a
   wrangling mini-project.

### Phase 2 — Visualization, exploration, and statistical modeling

1. Grammar of graphics: distributions, relationships, groups, facets, scales, and
   perceptual choices.
2. Exploratory data analysis that separates hypotheses from post-hoc discoveries;
   robust summaries and missingness patterns.
3. Simulation, probability distributions, sampling variation, bootstrap, and
   randomization in NumPy/SciPy.
4. statsmodels formulas, linear-model fit, contrasts, predictions, intervals, and
   diagnostic plots.
5. Interactions, transformations, splines, and categorical reference levels.
6. GLMs, family/link choice, interpretation, diagnostics, and prediction.
7. Repeated and hierarchical data with `clinical_longitudinal.csv` and
   `mixedlm`.
8. Integrated statistical analysis with a concise written report and limitations.

### Phase 3 — Classical machine learning and decision workflows

1. Define a predictive target, observation unit, split strategy, naive baseline,
   and decision-relevant metrics.
2. Missing-value and categorical preprocessing with `ColumnTransformer` and
   `Pipeline`; audit transformed shapes and features.
3. Cross-validation, regularization, tuning, and honest final evaluation.
4. Regression and classification model families; bias/variance and scaling.
5. Trees, random forests, gradient boosting, XGBoost, and controlled comparison.
6. Imbalance, thresholds, calibration, asymmetric costs, and decision curves.
7. Interpretation and error analysis: permutation importance, partial dependence,
   subgroup errors, uncertainty, and caveats.
8. Unsupervised learning: PCA, clustering, anomaly detection, and validation.
9. End-to-end tabular ML project with reproducible experiment reporting.

### Phase 4 — Structured and unstructured data modalities

1. Time series: indexing, resampling, lags, temporal splits, baselines, trend and
   seasonality, and leakage-safe forecasting evaluation.
2. Text: normalization choices, tokens, sparse matrices, TF-IDF, linear
   classifiers, evaluation, and interpretation.
3. Images: arrays, channels, transforms, augmentation concepts, display, and
   classical versus learned features using a bundled small dataset.
4. Geospatial data: coordinate systems, joins, aggregation, and mapping concepts;
   use a local lightweight dataset and add a specialist library only if needed.
5. Network or event data: nodes/edges, relational summaries, sequences, and when
   standard tabular assumptions fail.
6. Multimodal integration mini-project emphasizing alignment, granularity, and
   evaluation.

### Phase 5 — Neural networks with PyTorch

1. Tensors, shapes, broadcasting, affine layers, activations, logits, and parameter
   counts.
2. Losses, gradients, chain rule intuition, gradient descent, and a small NumPy
   implementation with a numerical gradient check.
3. PyTorch autograd, `nn.Module`, optimizers, datasets/loaders, and a complete
   training loop.
4. Tabular binary and multiclass models compared fairly with classical baselines.
5. Optimization, initialization, normalization, dropout, weight decay, early
   stopping, and controlled experiments.
6. CNNs for images: convolution, receptive fields, padding, pooling, and error
   analysis.
7. Embeddings and a small text or high-cardinality categorical model.
8. Transfer learning concepts, model persistence, inference, reproducibility, and
   device handling.
9. Neural-network project with a model card and comparison to a simpler approach.

### Phase 6 — Applied practice and professional workflow

1. Experimental design, A/B analysis, power through simulation, multiplicity, and
   practical versus statistical significance.
2. Causal questions versus predictive questions; confounding, DAG concepts,
   matching/weighting intuition, and sensitivity limitations.
3. Reproducible projects: modules, environments, configuration, logging, tests,
   versioned data/model artifacts, and documentation.
4. Data and model monitoring: schema drift, distribution shift, performance drift,
   fairness checks, and alert design.
5. Capstone: frame a question, audit data, analyze, model, evaluate, visualize,
   communicate, and document limitations with reduced scaffolding.

## Dataset catalog

`agent/generate_learning_data.py` deterministically creates:

- `data/customers.csv`: customer demographics, region, segment, signup date, and
  marketing status; primary key `customer_id`.
- `data/transactions.csv`: repeated purchases; useful for joins, aggregation,
  dates, missingness, returns, and feature engineering.
- `data/customer_import.csv`: fixed synthetic Day 2 import fixture, independent of
  the customer/transaction tables. Twelve import rows, ten intended customer keys
  (`customer_id`), five columns; one exact duplicate and one conflicting key,
  inconsistent string labels, and missing/unparseable/out-of-range ages. Created
  without randomness by `make_customer_import()` in the generator. To create only
  this fixture when other datasets already exist, run from the repository root:
  `.venv/bin/python -c 'from pathlib import Path; from agent.generate_learning_data import make_customer_import, _write_csv; _write_csv(make_customer_import(), Path("data/customer_import.csv"), force=False)'`.
- `data/customer_churn.csv`: mixed-type binary classification with missingness,
  imbalance, nonlinear effects, and interactions.
- `data/housing.csv`: mixed-type regression with nonlinear effects, missingness,
  and a right-tailed outcome.
- `data/clinical_longitudinal.csv`: repeated measurements nested in patients.
- `data/ci_telemetry/`: independent synthetic cochlear-implant telemetry bundle
  for research-preparation sessions 04–07. Seed 42; 96 fictional patients, one
  implant per patient, 360 visits, and 51,840 directed matrix cells. Includes
  `patients.csv`, `visits.csv`, `matrix_cells.csv`, `visit_features.csv`, and
  `prediction_pairs.csv`. Rows stimulate and columns record; observed voltage
  and current produce a teaching V/I proxy. This is not real MED-EL data or a
  validated device model. See `data/ci_telemetry/README.md` for keys, units, QC,
  provenance, and current versus future fields. Generate only this bundle with
  `.venv/bin/python agent/generate_learning_data.py --dataset ci-telemetry`;
  existing bundle files are protected unless `--force` is explicit. Existing
  general datasets are unaffected by this mode.

Before using local data, verify the file exists. If any are absent, run:

```bash
.venv/bin/python agent/generate_learning_data.py
```

Do not silently regenerate existing data with a different seed. The script
refuses overwrite unless `--force` is explicitly supplied. New locally generated
datasets may be added for text, time series, geospatial, network, or experiment
modules; document their grain, keys, provenance, and generation process here.

External teaching datasets may be used only when bundled with an installed
library and requiring no credentials or network download. Suitable examples
include sklearn iris, breast cancer, wine, digits, and 20-newsgroups only if
already cached (never make a core lesson depend on a network fetch). Explain why
an external dataset is used.

## Progress-file structure

`agent/PROGRESS.md` should contain:

- Active track, current position, next session, and default duration.
- A lesson table containing notebook, curriculum ID, generation date, completion,
  confidence, and notes.
- Concepts to repeat based on reflections or review evidence.
- A legacy-history section for superseded tracks.
- Modality coverage so broad aspirations do not silently narrow back to tabular
  classification.

Update conservatively. Preserve learner wording. Do not infer mastery from an
executed cell or from notebook generation.

## Notebook creation checklist

Before handoff, verify:

- Filename uses the requested active-track task/session number and matches the topic.
- Active-track day/session and duration are stated.
- Core workload plausibly fits the requested time.
- Every exercise prompt is immediately followed by an empty code cell.
- Exercise outputs and execution counts are cleared.
- New material has more scaffolding than repeated material.
- Retrieval practice uses less guidance.
- At least one task asks for a predicted shape/type/output.
- At least one task requires interpretation and one challenges an unjustified
  conclusion.
- Data grain, keys, and join cardinality are explicit where relevant.
- Data paths are relative and portable.
- Required imports succeed in `.venv`; otherwise give the exact install command.
- Notebook JSON is valid and opens successfully.
- `agent/PROGRESS.md` records generation, not completion.

Finish by stating the notebook, estimated duration, main concepts, and exact
command/environment needed to open it. Keep the handoff short; the notebook is
the lesson.
