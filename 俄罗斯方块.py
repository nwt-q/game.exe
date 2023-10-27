import pygame, sys
import random

# 物块的形状是二维数组
all_block = [
    [[0, 0], [0, 1], [0, 2], [0, 3], ],  # 一个物体4个方块组成      长方形
    [[0, 0], [0, 1], [1, 0], [1, 1], ],  # 7个列表表示7种形状      正方形
    [[0, 0], [1, 0], [0, 1], [0, 2], ],  # 7字型
    [[0, 0], [0, 1], [0, -1], [0, -2], ],  # 倒7字型
    [[0, 0], [0, 1], [1, 1], [1, 2], ],  # Z字型
    [[0, 0], [0, -1], [1, -1], [1, -2], ],  # 倒z字型
    [[0, 0], [0, 1], [0, -1], [1, 0]],  # T字型
]

backgroud = [[0 for column in range(0, 10)] for row in range(0, 23)]  # 创造列表集
backgroud[0] = [1 for colum in range(0, 10)]  # 把0层修改为[1*10]

# 设置全局变量
# select_block = list(random.choice(all_block))  # 从7个形状中随机选择一种
initial_position = [21, 5]
times = 0  # 计时
score = [0]  # 得分  系统出错

gameover = []  # 游戏结束

press = False  # 按键加速
# 初始化
pygame.init()
screen = pygame.display.set_mode((400, 800))  # 设置窗口大小
select_block = list(random.choice(all_block))


def block_down():
    global select_block  # 将global改为全局变量
    y, x = initial_position  # initial_position = [21, 5]
    y -= 1  # 表示相距的间隔
    for row, column in select_block:  # 调节方块下落的位置
        row += y
        column += x
        if backgroud[row][column]:  # 注意
            break
    else:
        initial_position.clear()  # 刷新对初始位置进行更新
        initial_position.extend([y, x])  # [x,y]定义:[一个列表集,第一个值表示1行row,第二个值表示column
        return
    y, x = initial_position
    for row, column in select_block:
        row += y  # 对当前选择的方块
        column += x
        backgroud[row][column] = 1  # 这个是是将背景网格中指定位置的值修改为1
    complete_row = []  # 用来存储静态的block就是完成一行后,将静态block存储在数组中
    # 然后通过删除数组元素达到消除方块的效果

    # 下面代码用于处理和检测背景网格中是不是有完整的行
    for row in range(1, 21):  # 通过循环遍历背景网格中的每一行
        if 0 not in backgroud[row]:  # 条件判断是否存在值为0的元素，如果不存在，则表示该行是完整的。
            complete_row.append(row)  # 如果一行是完整的将其行号row添加到complete_row中
    for row in complete_row:  # 再次循环对每一行进行遍历
        backgroud.pop(row)  # 将完整的行移除
        backgroud.append(list(0 for _ in range(0, 10)))  # 注意 移除行后在网格底部添加一个新行就是为让网格大小保持不变
    score[0] += len(complete_row)  # 计算消除行数并记录
    pygame.display.set_caption('你现在的分数是 ' + str(score[0]) + '分')  # 显示消除行数显示标题中
    # text = font.render("Score: " + str(score[0]), True, (0, 0, 0))
    initial_position.clear()  # 清空 initial_position列表中的元素
    select_block = list(random.choice(all_block))  # 随机选择一个方块
    initial_position.extend(select_block)  # 将选中的方块赋值给initial_position,initial_position里面存储着随机选择的方块
    initial_position.clear()  # 当动态的block变成静态block清楚initial_position中存储的上个方块的信息然后为重新加载方块做准备
    initial_position.extend([20, 5])  # 将[20,5]添加到initial_position中[20,5]代表下落的初始坐标
    y, x = initial_position
    for row, column in select_block:  # 用于确定方块的偏移量
        row += y
        column += x
        if backgroud[row][column] == 1:  # 判断静态block对应位置是否为1如果是说明当前方块于背景中已有方块重叠
            gameover.append(1)
            # 这段代码的逻辑是遍历选中的方块中的每个位置，将其与背景中对应位置的值进行比较，如果发生碰撞，则将游戏结束的标志（值为 1）
# 详细解释
# 首先，通过 `for row, column in select_block:` 遍历 `select_block` 列表中的每个元素，其中每个元素都是一个包含方块位置信息的列表，例如 `[row, column]`。
#
# 然后，将 `row` 和 `column` 分别加上变量 `y` 和 `x` 的值。这里的 `y` 和 `x` 可能表示方块在背景中的偏移量，用于确定方块的实际位置。
#
# 接下来，通过 `if backgroud[row][column] == 1:` 条件语句判断背景中对应位置的值是否为 1。如果是，说明当前方块与背景中已有的方块重叠，即发生碰撞。
#
# 如果发生碰撞，将值为 1 的元素添加到 `gameover` 列表中，以表示游戏结束。
#
# 综上所述，这段代码的逻辑是遍历选中的方块中的每个位置，将其与背景中对应位置的值进行比较，如果发生碰撞，则将游戏结束的标志（值为 1）添加到 `gameover` 列表中。

# TODO:
# def block_down():
#     # select_block = list(random.choice(all_block))
#     y, x = initial_position  # initial_position = [21, 5]
#     y -= 1  # 表示相距的间隔
#     for row, column in select_block:
#         row += y
#         column += x
#         if backgroud[row][column]:  # 注意
#             break
#     else:
#         initial_position.clear()
#         initial_position.extend([y, x])  # [x,y]定义:[一个列表集,第一个值表示1行row,第二个值表示column
#         return
#     y, x = initial_position
#     for row, column in select_block:
#         row += y  # 对当前选择的方块
#         column += x
#         backgroud[row][column] = 1
#     complete_row = []
#     for row in range(1, 21):
#         if 0 not in backgroud[row]:
#             complete_row.append(row)
#     for row in complete_row:
#         backgroud.pop(row)
#         backgroud.append(list(0 for _ in range(0, 50)))  # 注意
#     score[0] += len(complete_row)
#     pygame.display.set_caption('Tetris,Your Score: ' + str(score[0]) + 'By Tonymot')
#     initial_position.clear()
#     initial_position.extend(list(random.choice(all_block)))#感觉没有什么用
#     initial_position.clear()
#     initial_position.extend([20, 5])
#     y, x = initial_position
#     # select_block = list(random.choice(all_block))
#     for row, column in select_block:
#         row += y
#         column += x
#         if backgroud[row][column] == 1:
#             gameover.append(1)


# 首先，在代码中，得分的计算是通过统计消除行数来实现的。当检测到某一行被完全填满时，会将该行从backgroud中移除，并在顶部添加一行空白行。然后，通过累加消除的行数来更新得分。这部分逻辑看起来是正确的。
#
# 但是，需要注意的是，在计算得分之前，你使用了initial_position.clear()清空了initial_position列表，然后又使用initial_position.extend(list(random.choice(all_block)))重新添加了新的方块位置。这样做会导致之前的方块位置信息丢失，无法正确计算得分。
#
# 为了解决这个问题，你可以在计算得分之前，先将initial_position的值保存到一个临时变量中，然后再进行清空和重新添加方块位置的操作

def draw_block():
    y, x = initial_position
    for row, column in select_block:
        row += y
        column += x
        pygame.draw.rect(screen, (255, 165, 0), (column * 40, 800 - row * 40, 38, 38))
    for row in range(1, 21):
        for column in range(0, 10):
            if backgroud[row][column] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (column * 40, 800 - row * 40, 38, 38))


def rotate():
    y, x = initial_position
    # select_block = list(random.choice(all_block))
    rotating_position = [(-colum, row) for row, colum in select_block]  # 计算方块旋转后的位置
    for row, colum in rotating_position:
        row += y
        colum += x
        if colum < 0 or colum > 9 or backgroud[row][colum]:
            break
    else:
        select_block.clear()
        select_block.extend(rotating_position)


def move(d):
    y, x = initial_position
    # select_block = list(random.choice(all_block))
    x += d
    for row, colum in select_block:
        row += y
        colum += x
        if colum < 0 or colum > 9 or backgroud[row][colum]:
            break
    else:
        initial_position.clear()
        initial_position.extend([y, x])


while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                press = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate()  # 据你提供的代码，无法向下加速的原因是在处理pygame.KEYUP事件时，判断按键是否为向下键时使用了错误的语句。
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:  # 具体来说，在代码中，当检测到键盘按键释放事件（pygame.KEYUP）时，判断按键是否为向下键时应该使用event.key
                    # 而不是event.type。
                    move(1)  # 因此，将event.type改为event.key即可解决这个问题
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move(-1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                press = False

    if times % 60 == 0:
        block_down()
    times += 1
    if press:
        times += 10
    if gameover:
        sys.exit()
    draw_block()
    pygame.time.Clock().tick(400)
    # 创建字体对象
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score[0]), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.update()
    pygame.display.flip()

# 俄罗斯方块基本类
# 方块
# 旋转
# 移动
# 物块
# 形状
# 碰撞检测
# 绘制
