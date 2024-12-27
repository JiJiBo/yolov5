from multiprocessing import Manager

class NasGameConfig:
    def __init__(self, width=640, height=640, fps=30):
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
            "fps": fps
        })

    def start(self):
        """启动配置"""
        if self.shared_config["is_started"]:
            return
        print("NasGameConfig started")
        self.shared_config["is_started"] = True

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

    def set_red(self):
        """设置为红方"""
        print("NasGameConfig set to red")
        self.shared_config["is_red"] = True

    def set_blue(self):
        """设置为蓝方"""
        print("NasGameConfig set to blue")
        self.shared_config["is_red"] = False

    def get_config(self):
        """获取当前配置"""
        return dict(self.shared_config)
