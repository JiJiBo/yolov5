import multiprocessing
from multiprocessing import Process

from game_alone.ListenerKeybord import ListenerKeybord
from game_alone.NasGameConfig import NasGameConfig
from game_alone.SeeScreen import SeeScreen


class BigBoss:
    def __init__(self):
        manager = multiprocessing.Manager()
        self.shared_namespace = manager.Namespace()
        self.shared_namespace.instance = NasGameConfig()

    def run(self):
        pk = Process(target=ListenerKeybord, args=(self.shared_namespace,), name='Keyboard')
        pl = Process(target=SeeScreen, args=(self.shared_namespace,), name='Loop')
        # 启动进程
        pk.start()
        pl.start()
        # 等待进程完成
        pk.join()
        pl.join()
