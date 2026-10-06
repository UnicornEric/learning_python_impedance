# Pre-employment learning history

Archived on 2026-10-05 when the learner requested a complete course reset.
All 12 previous notebooks retain their original bytes, names, attempts, and
outputs. Root notebooks are here directly; previously archived notebooks retain
their former `archive/` subfolders. `manifest.json` records original paths and
SHA-256 hashes. `course_instructions/` preserves the former plan and progress;
these instructions are historical.

These lessons are optional history, not prerequisites for the new course.
Original numbering and completion records were preserved rather than inferred.

Old notebooks still reference `data/` relative to the original repository root.
To revisit them without altering their contents, launch Jupyter from the project
root, open the desired archived notebook, and make the first cell you run:

```python
from pathlib import Path
import os
root = next(p for p in [Path.cwd(), *Path.cwd().parents]
            if (p / "data/ci_telemetry").is_dir())
os.chdir(root)
```

Select the existing **Python (learning-python)** kernel. Restarting the kernel
can restore the notebook-directory working directory; rerun the setup above.
