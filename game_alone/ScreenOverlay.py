import tkinter as tk
from tkinter import Canvas
from threading import Thread

class ScreenOverlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = None
        self.canvas = None
        self.is_running = False  # 控制框的状态

    def create_overlay_window(self):
        """创建透明窗口"""
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)  # 设置窗口全屏
        self.root.attributes('-topmost', True)  # 窗口置顶
        self.root.attributes('-transparentcolor', 'black')  # 设置透明背景
        self.canvas = Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_center_box(self):
        """在屏幕中心绘制一个矩形"""
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

    def start(self):
        """启动绘制框"""
        if not self.is_running:
            self.is_running = True
            Thread(target=self.run, daemon=True).start()

    def stop(self):
        """销毁框并停止窗口"""
        if self.is_running:
            self.is_running = False
            if self.root:
                self.root.destroy()

    def run(self):
        """运行透明窗口"""
        self.create_overlay_window()
        self.draw_center_box()
        self.root.mainloop()

# 示例使用
if __name__ == "__main__":
    import time

    overlay = ScreenOverlay(width=200, height=200)

    # 启动画框
    print("启动画框")
    overlay.start()
    time.sleep(5)

    # 停止画框
    print("销毁画框")
    overlay.stop()
