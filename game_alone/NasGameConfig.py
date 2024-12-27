class NasGameConfig:
    def __init__(self, width=640, height=640, fps=30):
        self.isStarted = False
        self.isDes = False
        self.model_path = "runs/train/last.pt"
        self.isRed = True
        self.ads = 0.95
        self.width = width
        self.height = height
        self.fps = fps

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
