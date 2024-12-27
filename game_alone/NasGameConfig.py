class NasGameConfig:
    def __init__(self):
        self.isStarted = False
        self.frame = None
        self.isDes = False

    def start(self):
        self.isStarted = True

    def pause(self):
        self.isStarted = False

    def destroy(self):
        self.isStarted = False
        self.frame = None
        self.isDes = True
