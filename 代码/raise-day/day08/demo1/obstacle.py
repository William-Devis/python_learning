"""
    障碍物模块
    本模块包含障碍物类
"""
from birds import RedBird, YellowBird, BlueBird


class Obstacle:
    """
        障碍物类
        名字属性 强度属性
    """

    def __init__(self,name,strength):
        self.name = name
        self.strength = strength

    def be_attacked(self,bird):
        print(f"{bird.name}冲向了{self.name}")
        # 使用年类对象 使用技能
        bird.use_skill()

        if isinstance(bird,RedBird):
            damage = 80
        elif isinstance(bird,YellowBird):
            damage = 70
        elif isinstance(bird,BlueBird):
            damage = 30 * 3
        else:
            print("类型错误") # 暂时先提示 后续可以抛出异常 raise关键字

        self.strength -= damage

        if self.strength <= 0:
            print(f"{self.name}被摧毁了")
        else:
            print(f"{self.name}被{bird.name}造成了{damage}伤害")















