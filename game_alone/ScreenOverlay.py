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

        # 创建画布
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 计算矩形位置
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.rect_x1 = (screen_width - config.width) // 2
        self.rect_y1 = (screen_height - config.height) // 2
        self.rect_x2 = self.rect_x1 + config.width
        self.rect_y2 = self.rect_y1 + config.height

        # 绘制矩形
        self.canvas.create_rectangle(
            self.rect_x1, self.rect_y1, self.rect_x2, self.rect_y2, outline="red", width=5
        )

        # 创建动态标签
        self.label_text = self.canvas.create_text(
            (self.rect_x1 + self.rect_x2) // 2,  # 中心位置 X
            (self.rect_y1 + self.rect_y2) // 2,  # 中心位置 Y
            text="", fill="white", font=("Arial", 24)
        )

        # 初始化标签
        self.update_label()

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
        """刷新标签内容"""
        new_label = self.get_label()
        self.canvas.itemconfig(self.label_text, text=new_label)
        # 定时更新标签（如果需要实时刷新）
        self.root.after(1000, self.update_label)  # 每隔1秒刷新一次

    def open_overlay(self):
        self.root.mainloop()

    def close_overlay(self):
        """关闭窗口"""
        if self.root:
            self.root.destroy()


