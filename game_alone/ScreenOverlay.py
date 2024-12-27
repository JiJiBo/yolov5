import tkinter as tk

class TransparentOverlay:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.overrideredirect(True)  # 去除窗口装饰（边框、标题栏）
        self.root.attributes("-topmost", True)  # 窗口置顶
        self.root.attributes("-transparentcolor", "black")  # 设置黑色为透明
        self.root.configure(bg="black")  # 背景透明

        # 创建画布
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 计算矩形位置
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.rect_x1 = (screen_width - width) // 2
        self.rect_y1 = (screen_height - height) // 2
        self.rect_x2 = self.rect_x1 + width
        self.rect_y2 = self.rect_y1 + height

        # 绘制矩形
        self.canvas.create_rectangle(
            self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2, outline="red", width=5
        )

    def open_overlay(self):
        """显示透明窗口（非阻塞模式）"""
        self.root.after(10, self._non_blocking_loop)

    def _non_blocking_loop(self):
        """非阻塞主循环"""
        try:
            self.root.update_idletasks()
            self.root.update()
            self.root.after(10, self._non_blocking_loop)
        except tk.TclError:  # 窗口关闭时防止报错
            pass

    def close_overlay(self):
        """关闭窗口"""
        if self.root:
            self.root.destroy()

if __name__ == "__main__":
    overlay = TransparentOverlay(300, 200)
    overlay.open_overlay()
    print("Overlay is running without blocking the main thread.")
