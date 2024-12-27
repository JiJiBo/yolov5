from pynput.keyboard import Listener, Key


class ListenerKeybord:
    def __init__(self, config):
        self.config = config
        self.call()

    def release(self, key):
        if key == Key.shift:
            self.config.instance.pause()

    def press(self, key):
        if key == Key.shift:
            self.config.instance.start()
        elif key == Key.end:
            self.config.instance.destroy()
        elif key == Key.f2:
            self.config.instance.setRed()
        elif key == Key.f1:
            self.config.instance.setBlue()

    def call(self):
        with Listener(on_release=self.release, on_press=self.press) as k:
            k.join()
