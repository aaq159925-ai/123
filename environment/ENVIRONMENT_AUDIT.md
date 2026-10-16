# Environment audit

No fully locked historical environment was found: there is no verified `environment.yml`, `conda-lock.yml`, `pip-freeze.txt`, container digest, or CUDA/cuDNN/GPU record. `project/requirements.txt` and `project/pyproject.toml` are useful but do not fully pin the historical environment.

## Candidate environment — not proven

A source-server Conda environment named `yolov10` was found. Its creation history is preserved as `candidate-conda-history.txt`. Package metadata reports:

```text
Python       3.9.19
PyTorch      2.0.1
torchvision  0.15.2
Ultralytics  8.1.34
NumPy        1.26.4
OpenCV       4.9.0.80
Pillow       10.3.0
Pandas       2.2.2
SciPy        1.13.0
```

It was created before the saved experiment and Python 3.9 bytecode exists in the project. However, no shell history links it to this run and its name refers to YOLOv10. Treat it as a compatibility lead, not confirmed ground truth.

Strict reproduction still requires the actual training GPU, driver, CUDA, cuDNN, Python, PyTorch, and package lock if the original machine state remains available.
