class NasGameConfig:
    def __init__(self):
        self.isStarted = False
        self.isDes = False
        self.model_path = "runs/train/last.pt"
        self.isRed = True

    def start(self):
        self.isStarted = True

    def pause(self):
        self.isStarted = False

    def destroy(self):
        self.isStarted = False
        self.isDes = True

    def setRed(self):
        self.isRed = True

    def setBlue(self):
        self.isRed = False
