from ultralytics import YOLO
import pandas as pd

# 读取模型，这里传入训练好的模型
model = YOLO('/data1/lhb/object-detection-model/ultralytics-main/ultralytics-main/runs/detect/500-n-0.756/weights/best.pt')

# 模型预测，save=True 的时候表示直接保 存yolov8的预测结果
metrics = model.predict(r'/data2/lhb/wuhan_640_3', save=True,save_conf=False,save_txt=True,conf=0.32)

# import os
#
#
# def check_file_in_folder(folder_path, filename):
#     """
#     检查文件夹中是否存在指定文件
#
#     参数:
#         folder_path (str): 文件夹路径
#         filename (str): 要检查的文件名
#
#     返回:
#         bool: 文件是否存在
#         str: 文件的完整路径（如果存在），否则返回错误信息
#     """
#     # 拼接完整文件路径
#     file_path = os.path.join(folder_path, filename)
#
#     # 检查文件是否存在
#     if os.path.exists(file_path):
#         if os.path.isfile(file_path):  # 确保是文件而不是目录
#             return True, file_path
#         else:
#             return False, f"路径存在但不是文件: {file_path}"
#     else:
#         return False, f"文件不存在: {file_path}"
#
#
# # 示例用法
# if __name__ == "__main__":
#     folder_A = "/data2/lhb/wuhan_640_2/"  # 替换为你的文件夹A路径
#     target_file = "114.2728921_30.55704164_270_0.png"  # 替换为你要检查的文件名
#
#     exists, result = check_file_in_folder(folder_A, target_file)
#
#     if exists:
#         print(f"✅ 文件存在: {result}")
#     else:
#         print(f"❌ 错误: {result}")

