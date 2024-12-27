import cv2
import numpy as np
import torch

from models.common import DetectMultiBackend


class YoloHead():
    def __init__(self, model_path):
        self.model_path = model_path
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = DetectMultiBackend(self.model_path, device=self.device, dnn=False, data="csgo/data.yaml",
                                        fp16=False)
        self.model.eval()

    def call(self, frame):
        image = np.array([frame])
        image = torch.from_numpy(image).float()
        image = image.permute(0, 3, 1, 2, )
        image = image.to(self.device)
        b, c, x, y = image.size()
        imgsz = (b, c, x, y)
        print(imgsz)
        self.model.warmup(imgsz=imgsz)

        pred = self.model(image, augment=False, visualize=False).unsqueeze(0)
        return self.deal(pred)

    def deal(self, pred):
        pass


if __name__ == '__main__':
    model = YoloHead(r'C:\Users\12700\PycharmProjects\yolov5\runs\train\last.pt')
    frame = cv2.imread(
        r"C:\Users\12700\PycharmProjects\yolov5\csgo\train\images\15_jpg.rf.c26d6ae52d2cf864f27003fedc1d6ae4.jpg")
    result = model.call(frame)
    print(result)
