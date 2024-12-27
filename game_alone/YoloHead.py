import torch

from models.common import DetectMultiBackend


class YoloHead():
    def __init__(self, model_path):
        self.model_path = model_path
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = DetectMultiBackend(self.model_path, device=self.device, dnn=False, data="csgo/data.yaml",
                                        fp16=False)

    def call(self, frame):
        pred = self.model(frame, augment=False, visualize=False).unsqueeze(0)
        return pred
