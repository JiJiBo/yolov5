import tkinter as tk


class TransparentOverlay:
    def __init__(self, config):
        self.root = tk.Tk()
        self.config = config
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.overrideredirect(True)  # 去除窗口装饰（边框、标题栏）
        self.root.attributes("-topmost", True)  # 窗口置顶
        self.root.attributes("-transparentcolor", "black")  # 设置黑色为透明
        self.root.configure(bg="black")  # 背景透明
        self.time = 1 / self.config.fps * 1000
        # 创建画布
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 绘制矩形
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.rect_x1 = (screen_width - config.width) // 2
        self.rect_y1 = (screen_height - config.height) // 2
        self.rect_x2 = self.rect_x1 + config.width
        self.rect_y2 = self.rect_y1 + config.height

        self.canvas.create_rectangle(
            self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2, outline="red", width=5
        )

        # 创建动态标签（显示在左上角）
        self.label_text = self.canvas.create_text(
            10, 10,  # 左上角位置 (x, y)
            text="", fill="red", font=("Arial", 16), anchor="nw"  # anchor="nw" 设置左上对齐
        )

        # 初始化标签
        self.update_label()
        self.open_overlay()

    def get_label(self):
        if self.config.isRed:
            body = "匪徒"
        else:
            body = "警察"
        if self.config.isStarted:
            status = "启动"
        else:
            status = "暂停"
        return f"{body} - {status}"

    def update_label(self):
        """刷新标签内容，每帧60帧刷新"""
        new_label = self.get_label()
        self.canvas.itemconfig(self.label_text, text=new_label)
        self.root.after(int(self.time), self.update_label)  # 每秒60帧

    def open_overlay(self):
        self.root.mainloop()

    def close_overlay(self):
        """关闭窗口"""
        if self.root:
            self.root.destroy()
