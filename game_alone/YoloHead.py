import cv2
import numpy as np
import torch

from models.common import DetectMultiBackend
from utils.general import non_max_suppression, Profile
from utils.torch_utils import select_device


class YoloHead:
    def __init__(self, model_path, img_size):
        """
        初始化 YoloHead 模型
        :param model_path: YOLO 模型的权重路径
        """
        self.model_path = model_path
        self.img_size = img_size
        self.device = select_device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = DetectMultiBackend(self.model_path, device=self.device, dnn=False, data=r"C:\Users\12700\PycharmProjects\yolov5\mask\data.yaml",
                                        fp16=False)
        self.model.eval()
        self.names = self.model.names

    def preprocess(self, frame):
        """
        预处理图像，将其转换为模型输入格式
        :param frame: 输入的单帧图像 (H, W, C)
        :return: 预处理后的图像张量
        """
        frame_resized = cv2.resize(frame, self.img_size)  # 调整大小到模型输入大小
        image = frame_resized.astype(np.float32) / 255.0  # 归一化
        image = np.transpose(image, (2, 0, 1))  # HWC -> CHW
        image = np.expand_dims(image, axis=0)  # 增加 batch 维度
        return torch.from_numpy(image).to(self.device)

    def call(self, frame):
        """
        运行 YOLO 模型并返回处理后的帧
        :param frame: 输入的单帧图像
        :return: 带有检测框的帧
        """
        image = self.preprocess(frame)
        self.model.warmup(imgsz=(1, 3, self.img_size[0],self.img_size[1]))  # 预热模型

        with Profile(device=self.device):
            pred = self.model(image, augment=False, visualize=False)

        return self.deal(pred, frame)

    def deal(self, pred, frame):
        """
        处理 YOLO 模型的预测结果，并在图像上绘制边界框
        :param pred: 模型的原始预测结果
        :param frame: 原始输入帧
        :return: 带有检测框和标签的帧
        """
        pred = non_max_suppression(pred, conf_thres=0.25, iou_thres=0.45, classes=None, agnostic=False, max_det=1000)
        det = pred[0]
        if det is not None and len(det):
            det[:, :4] = det[:, :4].round()  # 将框的坐标转换为整数
            for *xyxy, conf, cls in reversed(det):
                x1, y1, x2, y2 = map(int, xyxy)
                confidence = float(conf)
                class_id = int(cls)

                # 打印调试信息
                print(f"Class: {self.names[class_id]}, Confidence: {confidence:.2f}, Coordinates: {x1, y1, x2, y2}")

                # 绘制边界框
                label = f"{self.names[class_id]} {confidence:.2f}"
                color = (0, 255, 0)  # 绿色
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                # 绘制标签
                text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
                text_origin = (x1, y1 - 10 if y1 - 10 > 10 else y1 + 10)
                cv2.rectangle(frame, (x1, y1 - text_size[1] - 10), (x1 + text_size[0], y1), color, -1)
                cv2.putText(frame, label, text_origin, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return frame


if __name__ == '__main__':
    model = YoloHead(r'C:\Users\12700\PycharmProjects\yolov5\runs\train\exp7\weights\last.pt', (640, 640))
    frame = cv2.imread(
        r"C:\Users\12700\PycharmProjects\yolov5\mask\train\images\1133x768_20200130000023_jpg.rf.e8a099312aa174af48c5914c4986f91a.jpg")
    if frame is None:
        print("Error: Unable to read the input image.")
        exit(1)

    frame_with_detections = model.call(frame)
    cv2.imshow('Detections', frame_with_detections)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
