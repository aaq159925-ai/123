from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n-seg.yaml').load('yolov8n-seg.pt')  # 从YAML构建并转移权重

if __name__ == '__main__':
    # 训练模型
    results = model.train(data='coco128-seg.yaml', epochs=10, imgsz=512)

    metrics = model.val()