"""Reconstructed from original-my-train.py and saved args.yaml."""
from ultralytics import YOLO


def main():
    model = YOLO("ultralytics/cfg/models/v8/yolov8-CoordAtt-BiFPN.yaml").load("../pretrained/yolov8n.pt")
    model.train(
        data="ultralytics/cfg/datasets/WuHanl.yaml",
        epochs=500,
        imgsz=640,
        batch=16,
        patience=50,
        optimizer="auto",
        seed=0,
        deterministic=True,
        amp=False,
        workers=8,
        name="reproduced_9class",
    )


if __name__ == "__main__":
    main()
