class NasGameConfig:
    def __init__(self, width=640, height=640, fps=30):
        self.isStarted = False
        self.isDes = False
        self.model_path = "csgo/best.pt"
        self.isRed = True
        self.ads = 0.95
        self.width = width
        self.height = height
        self.fps = fps

    def start(self):
        print("NasGameConfig start")
        self.isStarted = True

    def pause(self):
        print("NasGameConfig pause")
        self.isStarted = False

    def destroy(self):
        print("NasGameConfig destroy")
        self.isStarted = False
        self.isDes = True

    def setRed(self):
        print("NasGameConfig setRed")
        self.isRed = True

    def setBlue(self):
        print("NasGameConfig setBlue")
        self.isRed = False
