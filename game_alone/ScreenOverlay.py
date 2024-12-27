import tkinter as tk

class TransparentOverlay:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)  # 全屏
        self.root.attributes("-transparentcolor", "black")  # 设置透明色
        self.root.attributes("-topmost", True)  # 窗口置顶
        self.root.attributes("-alpha", 0.5)  # 设置透明度
        self.root.configure(bg="black")  # 背景透明

        # 创建画布
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 窗口宽高
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # 矩形参数
        self.rect_width = width
        self.rect_height = height
        self.rect_x1 = (self.screen_width - self.rect_width) // 2
        self.rect_y1 = (self.screen_height - self.rect_height) // 2
        self.rect_x2 = self.rect_x1 + self.rect_width
        self.rect_y2 = self.rect_y1 + self.rect_height

        # 绘制矩形框
        self.canvas.create_rectangle(
            self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2, outline="red", width=5
        )

        # 点击穿透功能
        self.root.attributes("-transparentcolor", "black")

    def open_overlay(self):
        """打开窗口"""
        self.root.after(0, self._non_blocking_loop)

    def _non_blocking_loop(self):
        """非阻塞主循环"""
        try:
            self.root.update()
            self.root.after(10, self._non_blocking_loop)  # 循环调用
        except tk.TclError:  # 窗口关闭时防止报错
            pass

    def close_overlay(self):
        """关闭窗口"""
        self.root.destroy()

if __name__ == "__main__":
    overlay = TransparentOverlay(100,200)
    overlay.open_overlay()
    print("Overlay is running in the main thread.")
