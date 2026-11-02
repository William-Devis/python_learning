"""
    测试模块 本模块包含测试类
"""
from birds import RedBird, YellowBird, BlueBird
from obstacle import Obstacle

print("测试类")

red_bird = RedBird("小红","红色","火焰冲击")
yellow_bird = YellowBird("小黄","黄色","艳阳冲击")
blue_bird = BlueBird("小蓝","蓝色","分裂攻击，分散成3只小鸟")


obs_1 = Obstacle("木桩",100)
obs_2 = Obstacle("石头",200)
obs_3 = Obstacle("金刚",300)

obs_3.be_attacked(red_bird)
obs_3.be_attacked(yellow_bird)
obs_3.be_attacked(blue_bird)