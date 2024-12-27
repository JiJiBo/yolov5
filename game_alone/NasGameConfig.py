class NasGameConfig:
    def __init__(self):
        self.isStarted = False

    def start(self):
        self.isStarted = True

    def pause(self):
        self.isStarted = False
