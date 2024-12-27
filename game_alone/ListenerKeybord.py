from pynput.keyboard import Listener, Key

class ListenerKeybord:
    def __init__(self, config):
        self.config = config
        self.call()

    def release(self, key):
        if key == Key.shift:
            self.config["config"].pause()
            self.config["config"] = self.config["config"]  # 回写

    def press(self, key):
        if key == Key.shift:
            self.config["config"].start()
            self.config["config"] = self.config["config"]  # 回写
        elif key == Key.end:
            self.config["config"].destroy()
            self.config["config"] = self.config["config"]  # 回写
        elif key == Key.f2:
            self.config["config"].setRed()
            self.config["config"] = self.config["config"]  # 回写
        elif key == Key.f1:
            self.config["config"].setBlue()
            self.config["config"] = self.config["config"]  # 回写

    def call(self):
        with Listener(on_release=self.release, on_press=self.press) as k:
            k.join()
