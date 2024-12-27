import cv2
import numpy as np
import torch

from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes
from utils.plots import colors


class YoloHead():
    def __init__(self, model_path):
        self.model_path = model_path
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = DetectMultiBackend(self.model_path, device=self.device, dnn=False, data="csgo/data.yaml",
                                        fp16=False)
        self.model.eval()
        self.names = self.model.names

    def call(self, frame):
        image = np.array([frame])
        image = torch.from_numpy(image).float()
        image = image.permute(0, 3, 1, 2, )
        image = image.to(self.device)
        b, c, x, y = image.size()
        imgsz = (b, c, x, y)
        self.model.warmup(imgsz=imgsz)

        pred = self.model(image, augment=False, visualize=False)
        return self.deal(pred, frame)

    def deal(self, pred, frame):
        pred = non_max_suppression(pred, conf_thres=0.5)
        result = {}
        det = pred[0]
        if len(det):
            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                print(self.names[int(c)])
                confidence = float(conf)
                confidence_str = f"{confidence:.2f}"
                print(confidence_str)

        return result


if __name__ == '__main__':
    model = YoloHead(r'C:\Users\12700\PycharmProjects\yolov5\runs\train\last.pt')
    frame = cv2.imread(
        r"C:\Users\12700\PycharmProjects\yolov5\csgo\train\images\15_jpg.rf.c26d6ae52d2cf864f27003fedc1d6ae4.jpg")
    result = model.call(frame)
    print(result)
