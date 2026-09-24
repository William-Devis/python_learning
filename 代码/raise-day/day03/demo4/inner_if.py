"""
    嵌套if结构  外层选择结构条件满足以后 才可以执行内层的选择结构
    需求：学校举行百米跑步比赛 如果跑步时间小于15秒 可以进入决赛 再根据性别分别分组 进入 男子组 或者 女子组
"""

time = float(input("请输入你的成绩\n"))


if time < 15:
    sex = input("请输入你的性别\n")
    if sex == "male":
        print("恭喜你进入男子组决赛")
    elif sex == "female":
        print("恭喜你进入女子组决赛")
    else:
        print("您输入的性别有误")
else:
    print("很遗憾，回家休息")

print("程序结束")

