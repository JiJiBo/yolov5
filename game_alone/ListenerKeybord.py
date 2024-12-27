from pynput.keyboard import Listener, Key


class ListenerKeybord:
    def __init__(self, config):
        self.config = config

    def release(self, key):
        if key == Key.shift:
            self.config.pause()

    def press(self, key):
        if key == Key.shift:
            self.config.start()

    def call(self):
        with Listener(on_release=self.release, on_press=self.press) as k:
            k.join()
