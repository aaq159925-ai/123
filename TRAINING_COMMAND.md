# Training command record

## Historical evidence

The preserved historical entry point is `evidence/original-my-train.py`. Its effective calls are:

```python
model = YOLO("yolov8-CoordAtt-BiFPN.yaml").load("yolov8n.pt")
results = model.train(data=".../WuHanl.yaml ", epochs=500)
result = model.val()
```

The likely launcher was:

```bash
cd /data1/lhb/object-detection-model/ultralytics-main/ultralytics-main
python my-train.py
```

No matching shell-history entry was found, so this is evidence-based but not proven to be the exact terminal command. The historical script also does not explicitly set the saved run name `9leibie-0.753`; the directory may have been renamed or a missing wrapper may have supplied it.

## Reconstructed launcher

```bash
cd project
python train_reproduce.py
```

`project/train_reproduce.py` combines the historical script with effective settings from `experiments/9leibie-0.753/args.yaml`.

For fine-tuning, initialize from `experiments/9leibie-0.753/weights/best.pt`, use a smaller learning rate such as 0.001, and mix new samples with the bundled original training data.

## Randomness

The saved arguments explicitly contain:

```yaml
seed: 0
deterministic: true
amp: false
workers: 8
```

This improves repeatability but does not guarantee bit-identical results across different GPUs, CUDA/cuDNN releases, PyTorch builds, or data-loader behavior.
