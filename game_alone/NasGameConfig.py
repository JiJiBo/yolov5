class NasGameConfig:
    def __init__(self):
        self.isStarted = False
        self.isDes = False
        self.model_path = "runs/train/last.pt"

    def start(self):
        self.isStarted = True

    def pause(self):
        self.isStarted = False

    def destroy(self):
        self.isStarted = False
        self.isDes = True
