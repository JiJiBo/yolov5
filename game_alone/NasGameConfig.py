from multiprocessing import Manager


class NasGameConfig:
    def __init__(self, width=960, height=640, fps=60):
        """
        初始化共享配置。
        :param width: 游戏宽度
        :param height: 游戏高度
        :param fps: 游戏帧率
        """
        manager = Manager()
        self.shared_config = manager.dict({
            "is_started": False,
            "is_destroyed": False,
            "model_path": "csgo/best.pt",
            "is_red": True,
            "ads": 0.95,
            "width": width,
            "height": height,
            "fps_current": fps,
            "fps": fps
        })

    @property
    def isStarted(self):
        """是否已启动"""
        return self.shared_config["is_started"]

    @property
    def isDes(self):
        """是否已销毁"""
        return self.shared_config["is_destroyed"]

    @property
    def model_path(self):
        """模型路径"""
        return self.shared_config["model_path"]

    @property
    def isRed(self):
        """是否为红方"""
        return self.shared_config["is_red"]

    @property
    def ads(self):
        """缩放比例"""
        return self.shared_config["ads"]

    @property
    def width(self):
        """屏幕宽度"""
        return self.shared_config["width"]

    @property
    def height(self):
        """屏幕高度"""
        return self.shared_config["height"]

    @property
    def fps(self):
        """帧率"""
        return self.shared_config["fps"]
    @property
    def fps_current(self):
        """帧率"""
        return self.shared_config["fps_current"]

    def start(self):
        """启动配置"""
        if self.shared_config["is_started"]:
            return
        print("NasGameConfig started")
        self.shared_config["is_started"] = True

    def toogle(self):
        """启动配置"""
        if self.shared_config["is_started"]:
            self.pause()
        else:
            self.start()

    def pause(self):
        """暂停配置"""
        if not self.shared_config["is_started"]:
            return
        print("NasGameConfig paused")
        self.shared_config["is_started"] = False

    def destroy(self):
        """销毁配置"""
        print("NasGameConfig destroyed")
        self.shared_config["is_started"] = False
        self.shared_config["is_destroyed"] = True

    def setRed(self):
        """设置为红方"""
        print("NasGameConfig set to red")
        self.shared_config["is_red"] = True

    def setBlue(self):
        """设置为蓝方"""
        print("NasGameConfig set to blue")
        self.shared_config["is_red"] = False

    def get_config(self):
        """获取当前配置"""
        return dict(self.shared_config)
