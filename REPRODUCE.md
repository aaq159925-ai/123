# BiCS-YOLO reproducibility bundle

This directory contains the files needed to reproduce inference and continue
fine-tuning the 9-class CoordAtt + BiFPN YOLOv8 tree-species detector.

## Directory layout

- `project/`: modified Ultralytics source and project entry scripts
- `datasets/new-wuhan/`: original train, validation, and test data
- `experiments/9leibie-0.753/`: best experiment weights, arguments, and metrics
- `pretrained/`: original YOLOv8n and YOLOv8s initialization weights
- `SHA256SUMS`: integrity checksums for all files in this bundle

## Important files

- Best checkpoint: `experiments/9leibie-0.753/weights/best.pt`
- Last checkpoint: `experiments/9leibie-0.753/weights/last.pt`
- Original arguments: `experiments/9leibie-0.753/args.yaml`
- Model architecture: `project/ultralytics/cfg/models/v8/yolov8-CoordAtt-BiFPN.yaml`
- Dataset config used by the experiment: `project/ultralytics/cfg/datasets/WuHanl.yaml`
- Custom BiFPN: `project/ultralytics/nn/BiFPN.py`
- Custom CoordAtt: `project/ultralytics/nn/modules/coordattention.py`
- Custom model parser: `project/ultralytics/nn/tasks.py`

## Classes

The best model has 9 classes. Preserve this exact ID order when adding data:

0. albi
1. cedr
2. cinn
3. gink
4. koel
5. magn
6. plat
7. sali
8. sapi

The `meta` class was excluded from this experiment. Adding it changes the task
to 10 classes and requires updating the dataset config and detection head.

## Dataset format

Each image must have a same-stem `.txt` label. Every label row uses YOLO object
detection format:

`class_id x_center y_center width height`

Coordinates are normalized to the range 0 to 1.

The bundled processed dataset contains 1,935 training, 541 validation, and 279
test images. Use `project/ultralytics/cfg/datasets/WuHanl.yaml` as the reference;
the dataset-root `data.yaml` contains older paths.

## Fine-tuning guidance

Start from `experiments/9leibie-0.753/weights/best.pt`, mix new data with the
original training data to reduce catastrophic forgetting, and keep validation
and test locations separate from training locations. Use a smaller initial
learning rate such as 0.001 for fine-tuning.

Install this bundled modified project rather than a stock Ultralytics release,
because the checkpoint depends on the custom CoordAtt and BiFPN modules.

For strict environment reproduction, record the original Python, PyTorch,
CUDA, and GPU driver versions. The bundled `requirements.txt` and
`pyproject.toml` do not constitute a fully locked environment.

## Added provenance and audit records

- `datasets/upstream/HanYang+wuhan_10_2755/`: upstream 10-class Roboflow export
- `evidence/original-my-train.py`: preserved historical training-script evidence
- `TRAINING_COMMAND.md`: historical evidence and reconstructed launcher
- `project/train_reproduce.py`: runnable reconstructed training entry point
- `DATA_PROVENANCE.md`: Roboflow preprocessing and 10-to-9-class derivation
- `environment/ENVIRONMENT_AUDIT.md`: confirmed gaps and candidate package versions
- `environment/candidate-conda-history.txt`: preserved candidate Conda history
