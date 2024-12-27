import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt


class TransparentWindow(QMainWindow):
    def __init__(self, rect_width, rect_height):
        super().__init__()
        screen = app.primaryScreen().size()
        rect_x = (screen.width() - rect_width) // 2
        rect_y = (screen.height() - rect_height) // 2
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # 窗口中间绘制矩形
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect_width = rect_width
        self.rect_height = rect_height

        # 创建用于显示的 QLabel
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())

        # 绘制图像
        self.draw_image()

    def draw_image(self):
        # 创建一个透明背景的图片
        img = np.zeros((self.height(), self.width(), 4), dtype=np.uint8)

        # 绘制矩形线框
        color = (255, 0, 0, 255)  # RGBA: 红色，完全不透明
        thickness = 3  # 线框宽度
        cv2.rectangle(img,
                      (self.rect_x, self.rect_y),
                      (self.rect_x + self.rect_width, self.rect_y + self.rect_height),
                      color,
                      thickness)

        # 转换为 QImage
        qimg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(qimg)

        # 设置到 QLabel 显示
        self.label.setPixmap(pixmap)

    def mousePressEvent(self, event):
        # 禁用鼠标点击事件，防止窗口失去焦点
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 窗口大小和矩形参数
    screen = app.primaryScreen().size()
    rect_width, rect_height = 200, 100
    rect_x = (screen.width() - rect_width) // 2
    rect_y = (screen.height() - rect_height) // 2

    # 创建窗口
    window = TransparentWindow(rect_width, rect_height)
    window.show()

    sys.exit(app.exec_())
