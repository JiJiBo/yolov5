import multiprocessing

from game_alone.BigBoss import BigBoss
from game_alone.NasGameConfig import NasGameConfig


def start():
    boss = BigBoss()
    boss.run()


if __name__ == '__main__':
    start()
