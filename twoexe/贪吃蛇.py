import pygame
import sys
import random

# 先定义全局然后后面用于页面 应该定义窗口大小
SCREEN_X = 600
SCREEN_Y = 600


# https://gitee.com/codetimer/Snake/blob/master/main.py

# 创建蛇类
# 我们这里以25为单位
class Snake(object):  # 我们用得上object吗?
    # 初始化我们要的各种属性
    def __init__(self):
        self.dirction = pygame.K_RIGHT  # 缩进有问题服服服服
        self.body = []
        for x in range(5):
            self.addnode()

    # def __int__(self):
    #     self.dirction = pygame.K_RIGHT  # 通过键盘定位来固定其移动方向对键盘的
    #     self.body = []  # 用数组去储存蛇的body即他的长度
    #     for x in range(5):  # x的范围是0到4 ????so这个干嘛的?  为什么循环5次#因为吃一个食物要增加5个单位长度
    #         self.addnode()  # 我调用了我要定义的属性 这个干嘛的? 通过调用sddnode的方法来为蛇增加长度将这个循环5次

    # 移动无论何时都是从前面加一#so要从列表开头加懂/就是他不是在尾部加蛇的长度而是在头加有点反人类我也觉的
    def addnode(self):  # 定义 左右 位置 初始化的位置
        left, top = (0, 0)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)  # 现在还不知道有什么用#用来增加蛇的长度
        node = pygame.Rect(left, top, 25, 25)  # python中一个Rect的类用来创建一个矩形的位置和尺寸
        if self.dirction == pygame.K_LEFT:  # 用pygame来捕获键盘输入然后返回到程序的实际操作种
            node.left -= 25  # 表示node蛇头向右移动左加右减
        elif self.dirction == pygame.K_RIGHT:  # 前后移动距离为25个单位
            node.left += 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        self.body.insert(0, node)  # self.body是一个列表的开头 node是一个对像通过insert方法调用,
        # 将node对象放在body的开头然后用列表代表一个

        # 向该方向移动要增加该方向的蛇的长度

        # 删除最后一个块???为什么?

        # 等价
        # left = self.body[0].left
        # top = self.body[0].top

        # !!!!!注意这里缩进有问题

    def delnode(self):  # 因为蛇的长度是固定的后面的长度要减
        self.body.pop()  # pop()删除数组尾部

    # 死亡判断
    def isdead(self):  # 碰撞检测
        # 到达边界撞墙
        if self.body[0].x not in range(SCREEN_X):  # 我猜这个应该表达的意思是
            # 这个蛇x轴的坐标到没有达我创建的窗口的x轴的边界就返回true然后继续运行
            return True  # 啊?为什么返回Ture 返回Ture表示撞到了
        if self.body[0].y not in range(SCREEN_Y):  # 现在的screen改版了
            return True
        if self.body[0] in self.body[1:]:  # ????为什么是1? 对 !是[1:]代表body的后面的值
            return True
        return False  # 都没有判断返回判断False

    # 定义移动
    def move(self):
        self.addnode()  # 将捕获的键盘输入信息进行转移到实际蛇的位移中
        self.delnode()  # 前面加了后面进行删除操作 其实可以将move单独分离

        # 前面定义的位移是单方向的而我们就要丰富下移动方向 于是定义一个类来带表方向位移
        # wc 改变方向还要考虑不可以逆向改变

    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]  # 为什么不可以加()因为加了()会代表俩输入值间代表某种关系
        # 为什么要将俩者存储在同一数组中因为俩者同水平
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:  # ??? curkey是什么??? # 检测curkey是否在LR和UD列表中
            if (curkey in LR) and (self in LR):  # 接下来的两个条件语句
                # 检查当前的移动方向是否与按下的键相同。
                # 如果是，则没有必要改变移动方向，
                # 可以直接返回。因此，这里没有返回值，只是简单地退出方法。
                return  # ???为什么没有返回值???只是进行操作?
            if (curkey in UD) and (self.dirction in UD):
                return  # ???为什么没有返回值???只是进行操作?
            self.dirction = curkey  # 移动的方向赋值位curkey更新当前位置
            # 如果不是按下相同键就直接返回不改变方向

    # 蛇的类定义完成,那么要定义食物的类
    # 方法: 食物的放置位置/和什么时候移除


class Food:
    def __init__(self):  # 老规矩初始化 初始化的是食物的大小吗?
        self.rect = pygame.Rect(-25, 0, 25, 25)  # ???? 只是创建了一个矩形, # 136 行会用
        # (left：-25 矩形左上角的 x 坐标,top：0 矩形左上角的 y 坐标) 其实已经告诉了矩形大小
        # width：25 矩形的宽度  这里就是告诉上下的像素
        # height：25 矩形的高度

    def remove(self):  # 食物的移动
        self.rect.x = -25  # 这个?????写错了 定义了墙的边界

    def set(self):
        if self.rect.x == -25:
            allpos = []
            # 不靠墙太进 25~SCREEN_X - 25??/?/?/??
            for pos in range(25, SCREEN_X - 25, 25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)  # 让食物随机出现额就是x轴和y轴出现随机的数
            self.rect.top = random.choice(allpos)
            print(self.rect)  # 然后显示食物


def show_text(screen, pos, text, color, font_bold=False, font_size=30, font_italic=False):
    # 设置文字大小
    cur_font = pygame.font.SysFont(None, font_size)
    # 加粗
    cur_font.set_bold(font_bold)
    # 斜体
    cur_font.set_italic(font_italic)
    # 设置内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    screen.blit(text_fmt, pos)


# 主要部分可以这样说运行部分
def main():
    pygame.init()
    screen_size = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("贪吃蛇")  # 游戏标题
    clock = pygame.time.Clock()  # ??//?这个干什么的??/
    scores = 0  # 定义分数分数先初始化
    isdead = False  # 定义死亡

    # 蛇/食物 将蛇和食物实例化
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 用于处理 Pygame 中事件循环的代码。
                sys.exit()  # pygame.event.get() 方法返回一个包含所有当前待处理事件的列表。
            if event.type == pygame.KEYDOWN:  # 通过使用 for event in pygame.event.get(): 的语法，
                snake.changedirection(event.key)  # 可以遍历该列表，并依次处理每个事件。
                # 死后按space重新开始
                if event == pygame.KSCAN_SPACE and isdead:
                    return main()

        screen.fill((255, 255, 255))  # 背景颜色

        # 画蛇身 / 每一不加1一为5个单位长度
        if not isdead:
            scores += 1  # 吃一个食物分数加1
            snake.move()  # 蛇移动
        for rect in snake.body:  # 这个蛇的身体来自body
            pygame.draw.rect(screen, (20, 220, 39), rect, 0)  # ????这个我猜应该是画蛇然后定义蛇的`颜色
            # 注意我这里多了(20, 220, 39)
        isdead = snake.isdead()  # 将蛇的死亡判定实例化
        # 显示死亡文字
        if isdead:
            # font = pygame.font.SysFont(None, 100, bold=False)
            # text = font.render("你tm会不会完?", False, (0, 0, 22), (227, 29, 18))
            # screen.blit(text, (100, 200))
            show_text(screen, (100, 200), "Will you tm can finish this game??", (227, 29, 18), False, 20)
            show_text(screen, (150, 260), "Press the space to challenge again.....", (0, 0, 22), False, 20)  # screen, (150, 260),
            # text = font.render("按空格再次挑战.....", False, 30, (0, 0, 22))
            # screen.blit(text, (100, 200))
            # text = font.render("Score: " + str(scores[0]), True, (0, 0, 0))
            # rendered_text = font.render(show_text, True, )
            # screen.blit(show_text, (10, 10))

            # 食物处理 / 吃到食物加50分离谱这么高
            # 当食物rect 与蛇头重合, 吃掉 ->蛇增加一给Node 结点就是长度加一
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()  # 食物移动
            snake.addnode()  # 蛇长度加他定义的1

        food.set()  # 让食物重新出现
        pygame.draw.rect(screen, (136, 0, 21), food.rect, 0)  # ??//?/?我实在没有明白

        # 显示分数
        show_text(screen, (50, 500), "Sore:" + str(scores), (223, 223, 223))
        # text = font.render("Score: " + str(scores[0]), True, (223, 223, 223))
        # screen.blit(text, (50, 500))
        pygame.display.flip()
        # pygame.display.update()
        clock.tick(5)  # 这个拿来干嘛的没有看懂?是拿来计时的吗?我看有可能
        # pygame.display.update()



if __name__ == "__main__":
    main()
