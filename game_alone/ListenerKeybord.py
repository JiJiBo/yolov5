from pynput.keyboard import Listener, Key


class ListenerKeybord:
    def __init__(self, config):
        self.config = config
        self.call()

    def release(self, key):
        if key == Key.shift:
            self.config .pause()

    def press(self, key):
        if key == Key.shift:
            self.config .start()
        elif key == Key.end:
            self.config .destroy()
        elif key == Key.f2:
            self.config .setRed()
        elif key == Key.f1:
            self.config .setBlue()
    def call(self):
        with Listener(on_release=self.release, on_press=self.press) as k:
            k.join()
