import ctypes


class MouseUtils:
    def __init__(self):
        try:

            import os
            root = os.path.abspath(os.path.dirname(__file__))
            self.driver = ctypes.CDLL(f'{root}/logitech.driver.dll')
            self.ok = self.driver.device_open() == 1
            if not self.ok:
                print('初始化失败, 未安装罗技驱动')
        except FileNotFoundError:
            print('初始化失败, 缺少文件')

    def move(self, x: int, y: int):
        if (x == 0) & (y == 0):
            return
        self.driver.moveR(x, y, True)

    def press(self, code):
        self.driver.mouse_down(code)

    def release(self, code):
        self.driver.mouse_up(code)
