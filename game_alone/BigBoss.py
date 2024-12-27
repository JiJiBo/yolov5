import multiprocessing
from multiprocessing import Process

from game_alone.ListenerKeybord import ListenerKeybord
from game_alone.NasGameConfig import NasGameConfig
from game_alone.SeeScreen import SeeScreen


class BigBoss:
    def __init__(self):
        self.config = NasGameConfig()
        self.INIT_DATA = {
            "config": self.config,
        }
        manager = multiprocessing.Manager()
        self.data = manager.dict()
        self.data.update(self.INIT_DATA)

        self.keyboard=ListenerKeybord(self.config)
        self.see = SeeScreen(self.INIT_DATA)
    def run(self):

        pk = Process(target=self.keyboard.call, args=( ), name='Keyboard')
        pl = Process(target=self.see.start_monitoring, args=( ), name='Loop')
        # 启动进程
        pk.start()
        pl.start()
        # print(6)
        pk.join()
