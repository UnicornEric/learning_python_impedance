# Impedance ML Engineering

A fresh, exercise-first course for relearning machine learning, neural networks,
and statistics around cochlear-implant-shaped impedance matrices. Restarted on
2026-10-05. The main goal is practical ML engineering fluency.

Start with [Session 01 — Impedance audit and exploration](01_impedance_audit_and_exploration.ipynb).
From this project directory:

```bash
.venv/bin/python -m jupyterlab 01_impedance_audit_and_exploration.ipynb
```

Choose **Python (learning-python)**. Exercises are empty on purpose; write your
own code and ask for hints or review. All core data are local and synthetic.
A CPU is sufficient. Start from a fresh kernel and run your attempted cells in order.

## The course

Twenty roughly 60-minute cores, plus optional extensions and repetition. The
route is flexible for free-time study; generated does not mean completed.

| Sessions | Focus | What you build |
|---|---|---|
| 01–03 | Matrix/QC exploration, first ML baseline, spatial features | A data contract and patient-safe predictor |
| 04–07 | Statistical refreshers, mixed models, trees/CV, PCA | Estimates with uncertainty and fair model comparisons |
| 08–10 | Tensors/autograd, MLP training, regularization/debugging | An audited PyTorch training loop |
| 11–13 | CNNs, matrix/metadata fusion, autoencoders | Learned spatial representations and controlled ablations |
| 14–17 | Classification, calibration, temporal prediction, uncertainty/shift | Probability decisions and robust evaluation |
| 18–20 | Inference artifacts and integrated capstone | Reproducible predictions and a technical report |

The shared question is whether current matrix/metadata can predict the next
scheduled visit’s diagonal V/I proxy for an unseen patient. Persistence, ridge,
trees, MLPs, and CNNs are compared under matching conditions; a more complex
model is allowed to lose. Statistical lessons revisit assumptions, effect sizes,
confidence intervals, bootstrap, confounding, and repeated measurements.

The fixed patient split is 54 training / 18 validation / 24 test patients.
Test outcomes stay reserved until Session 20. Reused validation is exploratory.
Classification uses a fixed synthetic teaching cutoff with no clinical meaning.
No real hearing/diagnostic labels exist in this dataset.

- [Full curriculum and teaching rules](agent/LEARNING_PLAN.md)
- [Current progress](agent/PROGRESS.md)
- [Data dictionary: matrix axes, units, QC, and provenance](data/ci_telemetry/README.md)
- [Previous course — preserved notebooks and attempts](pre_employment_learning/README.md)

New numbered notebooks live here in the main folder. The old notebooks and
previous instructions are in `pre_employment_learning/`; shared data and the
existing environment were retained. Later sessions include input scaffolding,
so they do not require variables or files produced by earlier exercise answers.

Dependencies are declared in `requirements.txt`; use the existing `.venv`. If a
needed package is missing, install with `.venv/bin/python -m pip install -r requirements.txt`.
Core lessons need no downloads beyond package installation.
