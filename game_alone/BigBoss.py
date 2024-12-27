import multiprocessing
from multiprocessing import Process

from game_alone.ListenerKeybord import ListenerKeybord
from game_alone.NasGameConfig import NasGameConfig
from game_alone.ScreenOverlay import TransparentOverlay
from game_alone.SeeScreen import SeeScreen


class BigBoss:
    def __init__(self):
        self.instance = NasGameConfig()

    def run(self):
        pk = Process(target=ListenerKeybord, args=(self.instance,), name='Keyboard')
        pl = Process(target=SeeScreen, args=(self.instance,), name='Loop')
        pt = Process(target=TransparentOverlay, args=(self.instance,), name='Rect')
        # 启动进程
        pk.start()
        pl.start()
        pt.start()
        # 等待进程完成
        pk.join()
        pl.join()
        pt.join()
