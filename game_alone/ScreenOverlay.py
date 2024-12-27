import tkinter as tk
import threading
import queue
import time
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

        # 创建一个队列，用于线程间通信
        self.queue = queue.Queue()

    def open_overlay(self):
        """显示透明窗口"""
        threading.Thread(target=self.run_task, daemon=True).start()
        self.check_queue()
        self.root.mainloop()

    def run_task(self):
        """子线程中运行的任务"""
        for i in range(5):  # 模拟长时间任务
            self.queue.put(f"Task {i} completed!")
            time.sleep(1)

    def check_queue(self):
        """检查队列并更新界面"""
        while not self.queue.empty():
            message = self.queue.get()
            print(message)  # 在主线程打印
            # 也可以在界面上更新内容，例如显示消息
        self.root.after(100, self.check_queue)

    def close_overlay(self):
        """关闭窗口"""
        if self.root:
            self.root.destroy()

if __name__ == "__main__":

    overlay = TransparentOverlay(300, 200)
    overlay.open_overlay()
