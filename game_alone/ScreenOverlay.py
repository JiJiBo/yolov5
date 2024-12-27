import tkinter as tk
from tkinter import Canvas
from threading import Thread, Lock


class ScreenOverlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = None
        self.canvas = None
        self.is_running = False  # 控制框的状态
        self.lock = Lock()  # 用于线程安全的锁

    def create_overlay_window(self):
        """创建透明窗口"""
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)  # 设置窗口全屏
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.attributes('-transparentcolor', 'black')  # 设置透明背景
        self.canvas = Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_center_box(self, x=None, y=None):
        """在屏幕中心绘制一个矩形，并绘制相对于中心的点"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        center_x = screen_width // 2
        center_y = screen_height // 2
        left = center_x - self.width // 2
        top = center_y - self.height // 2
        right = center_x + self.width // 2
        bottom = center_y + self.height // 2

        # 绘制红色边框矩形
        self.canvas.create_rectangle(left, top, right, bottom, outline="red", width=2)

        # 如果提供了点的坐标，绘制该点
        if x is not None and y is not None:
            # 将点的相对坐标转换为绝对坐标
            point_x = center_x + x
            point_y = center_y + y
            self.canvas.create_oval(
                point_x - 3, point_y - 3, point_x + 3, point_y + 3, fill="blue"
            )

    def start(self, x=0, y=0):
        """启动绘制框并绘制相对于中心的点"""
        with self.lock:
            if not self.is_running:
                self.is_running = True
                Thread(target=self.run, args=(x, y), daemon=True).start()

    def stop(self):
        """销毁框并停止窗口"""
        with self.lock:
            if self.is_running:
                self.is_running = False
                if self.root:
                    self.root.quit()  # 停止 Tkinter 主循环
                    self.root = None  # 释放资源

    def run(self, x, y):
        """运行透明窗口"""
        self.create_overlay_window()
        self.draw_center_box(x, y)
        self.root.mainloop()
        # 主循环结束后设置状态为停止
        with self.lock:
            self.is_running = False


# 示例使用
if __name__ == "__main__":
    import time

    overlay = ScreenOverlay(width=200, height=200)

    # 连续调用 start 和 stop
    print("启动画框并绘制点 (50, -50)")
    overlay.start(x=50, y=-50)
    time.sleep(2)

    print("销毁画框")
    overlay.stop()
    time.sleep(1)

    print("再次启动画框并绘制点 (-30, 30)")
    overlay.start(x=-30, y=30)
    time.sleep(2)

    print("再次销毁画框")
    overlay.stop()
