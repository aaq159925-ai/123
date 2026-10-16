from ultralytics import YOLO
# 加载一个模型
model = YOLO('/data1/lhb/object-detection-model/ultralytics-main/ultralytics-main/ultralytics/cfg/models/v8/yolov8-CoordAtt-BiFPN.yaml')  # 从YAML建立一个新模型
model = YOLO('/data1/lhb/object-detection-model/ultralytics-main/ultralytics-main/yolov8n.pt')  # 加载预训练模型（推荐用于训练）
model = YOLO('yolov8-CoordAtt-BiFPN.yaml').load('yolov8n.pt')  # 从YAML建立并转移权重
# 训练模型
# if __name__ == '__main__':
results = model.train(data='/data1/lhb/object-detection-model/ultralytics-main/ultralytics-main/ultralytics/cfg/datasets/WuHanl.yaml ', epochs=500)
result = model.val()