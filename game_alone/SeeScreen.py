import time

import winsound
from PIL import ImageGrab
import numpy as np
import cv2

from game_alone.MouseUtils import MouseUtils
from game_alone.ScreenOverlay import ScreenOverlay
from game_alone.YoloHead import YoloHead


class SeeScreen:
    def __init__(self, config):
        self.config = config
        self.width = self.config.width
        self.height = self.config.height
        self.fps = self.config.fps
        self.screen_center = None
        self.overlay = ScreenOverlay(width=self.width, height=self.height)
        if not self.screen_center:
            self.get_screen_center()
        self.yolo = YoloHead(self.config.model_path, (self.width, self.height), self.config)
        self.mouse = MouseUtils(self.config.ads)
        self.start_monitoring()

    def get_screen_center(self):
        """获取屏幕中心的坐标"""
        screen = ImageGrab.grab()
        screen_width, screen_height = screen.size
        center_x = screen_width // 2
        center_y = screen_height // 2
        self.screen_center = (center_x, center_y)

    def capture_center_area(self):
        """捕获屏幕中心指定宽度和高度的区域"""
        if not self.screen_center:
            self.get_screen_center()
        center_x, center_y = self.screen_center
        left = center_x - self.width // 2
        top = center_y - self.height // 2
        right = center_x + self.width // 2
        bottom = center_y + self.height // 2
        # 截取屏幕中心区域
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        return screenshot

    def start_monitoring(self):
        """实时监视屏幕中央区域"""
        delay = 1 / self.fps
        while not self.config.isDes:
            start_time = time.time()
            screenshot = self.capture_center_area()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
            if self.config.isStarted:
                pre = self.yolo.call(frame)
                self.overlay.start(pre["x"], pre["y"])
                if pre["shoot"]:
                    winsound.Beep(800, 200)
                    self.mouse.move(pre["x"], pre["y"])
            else:
                self.overlay.stop()
            elapsed_time = time.time() - start_time
            time.sleep(max(0, delay - elapsed_time))


# 使用示例
if __name__ == "__main__":
    monitor = SeeScreen(width=200, height=200, fps=30)
    monitor.start_monitoring()
