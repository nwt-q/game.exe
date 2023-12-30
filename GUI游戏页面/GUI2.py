import tkinter as tk
import pygame
import random
import os
from coust import *

# base_folder = os.path.dirname(__file__)

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("经典")
        self.master.geometry("800x800")

        tk.Button(master, text='开始游戏', width=30, height=2, command=self.run).grid(row=2, column=1, sticky="e",padx=270, pady=10)
        tk.Button(master, text='退出', width=30, height=2, command=master.quit).grid(row=3, column=1, sticky="e", padx=270, pady=10)

    def run(self):
        if __name__ == '__main__':

            pygame.init()
            screen = pygame.display.set_mode((SCREEN_WIDTH, HEIGHT))

            pygame.display.set_caption("俄罗斯方块")
            clock = pygame.time.Clock()
            FPS = 30

            score = 0
            level = 1
            screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
            # 设置游戏的根目录为当前文件夹

            def show_text(surf, text, size, x, y, color=WHITE):
                # font_name = os.path.join(base_folder, "D:\\project\\code\\pic\\yellow.png")
                font = pygame.font.Font(None, 36)
                text_surface = font.render(text, True, color)
                text_rect = text_surface.get_rect()
                text_rect.midtop = (x, y)
                surf.blit(text_surface, text_rect)

            class CubeShape(object):
                SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
                I = [[(0, -1), (0, 0), (0, 1), (0, 2)],
                     [(-1, 0), (0, 0), (1, 0), (2, 0)]]
                J = [[(-2, 0), (-1, 0), (0, 0), (0, -1)],
                     [(-1, 0), (0, 0), (0, 1), (0, 2)],
                     [(0, 1), (0, 0), (1, 0), (2, 0)],
                     [(0, -2), (0, -1), (0, 0), (1, 0)]]
                L = [[(-2, 0), (-1, 0), (0, 0), (0, 1)],
                     [(1, 0), (0, 0), (0, 1), (0, 2)],
                     [(0, -1), (0, 0), (1, 0), (2, 0)],
                     [(0, -2), (0, -1), (0, 0), (-1, 0)]]
                O = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
                S = [[(-1, 0), (0, 0), (0, 1), (1, 1)],
                     [(1, -1), (1, 0), (0, 0), (0, 1)]]
                T = [[(0, -1), (0, 0), (0, 1), (-1, 0)],
                     [(-1, 0), (0, 0), (1, 0), (0, 1)],
                     [(0, -1), (0, 0), (0, 1), (1, 0)],
                     [(-1, 0), (0, 0), (1, 0), (0, -1)]]
                Z = [[(0, -1), (0, 0), (1, 0), (1, 1)],
                     [(-1, 0), (0, 0), (0, -1), (1, -1)]]

                SHAPES_WITH_DIR = {
                    'I': I, 'J': J, 'L': L, 'O': O, 'S': S, 'T': T, 'Z': Z
                }

                def __init__(self):
                    self.shape = self.SHAPES[random.randint(0, len(self.SHAPES) - 1)]
                    # 骨牌所在的行列
                    self.center = (2, GRID_NUM_WIDTH // 2)
                    self.dir = random.randint(0, len(self.SHAPES_WITH_DIR[self.shape]) - 1)
                    self.color = CUBE_COLORS[random.randint(0, len(CUBE_COLORS) - 1)]

                def get_all_gridpos(self, center=None):
                    curr_shape = self.SHAPES_WITH_DIR[self.shape][self.dir]
                    if center is None:
                        center = [self.center[0], self.center[1]]
                    return [(cube[0] + center[0], cube[1] + center[1])
                            for cube in curr_shape]

                def conflict(self, center):
                    for cube in self.get_all_gridpos(center):
                        # 超出屏幕之外，说明不合法
                        if cube[0] < 0 or cube[1] < 0 or cube[0] >= GRID_NUM_HEIGHT or \
                                cube[1] >= GRID_NUM_WIDTH:
                            return True

                        # 不为None，说明之前已经有小方块存在了，也不合法
                        if screen_color_matrix[cube[0]][cube[1]] is not None:
                            return True

                    return False

                def rotate(self):
                    new_dir = self.dir + 1
                    new_dir %= len(self.SHAPES_WITH_DIR[self.shape])
                    old_dir = self.dir
                    self.dir = new_dir
                    if self.conflict(self.center):
                        self.dir = old_dir
                        return False

                def down(self):
                    # import pdb; pdb.set_trace()
                    center = (self.center[0] + 1, self.center[1])
                    if self.conflict(center):
                        return False

                    self.center = center
                    return True

                def left(self):
                    center = (self.center[0], self.center[1] - 1)
                    if self.conflict(center):
                        return False
                    self.center = center
                    return True

                def right(self):
                    center = (self.center[0], self.center[1] + 1)
                    if self.conflict(center):
                        return False
                    self.center = center
                    return True

                def draw(self):
                    for cube in self.get_all_gridpos():
                        pygame.draw.rect(screen, self.color,
                                         (cube[1] * GRID_WIDTH, cube[0] * GRID_WIDTH,
                                          GRID_WIDTH, GRID_WIDTH))
                        pygame.draw.rect(screen, WHITE,
                                         (cube[1] * GRID_WIDTH, cube[0] * GRID_WIDTH,
                                          GRID_WIDTH, GRID_WIDTH),
                                         1)

            def draw_grids():
                for i in range(GRID_NUM_WIDTH):
                    pygame.draw.line(screen, LINE_COLOR,
                                     (i * GRID_WIDTH, 0), (i * GRID_WIDTH, HEIGHT))

                for i in range(GRID_NUM_HEIGHT):
                    pygame.draw.line(screen, LINE_COLOR,
                                     (0, i * GRID_WIDTH), (WIDTH, i * GRID_WIDTH))

                pygame.draw.line(screen, WHITE,
                                 (GRID_WIDTH * GRID_NUM_WIDTH, 0),
                                 (GRID_WIDTH * GRID_NUM_WIDTH, GRID_WIDTH * GRID_NUM_HEIGHT))

            def draw_matrix():
                screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
                for i, row in zip(range(GRID_NUM_HEIGHT), screen_color_matrix):
                    for j, color in zip(range(GRID_NUM_WIDTH), row):
                        if color is not None:
                            pygame.draw.rect(screen, color,
                                             (j * GRID_WIDTH, i * GRID_WIDTH,
                                              GRID_WIDTH, GRID_WIDTH))
                            pygame.draw.rect(screen, WHITE,
                                             (j * GRID_WIDTH, i * GRID_WIDTH,
                                              GRID_WIDTH, GRID_WIDTH), 2)

            def draw_score():
                show_text(screen, u'得分：{}'.format(score), 20, WIDTH + SIDE_WIDTH // 2, 100)

            def remove_full_line():
                score = 0
                #global screen_color_matrix
                # global score
                global level
                screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
                new_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
                index = GRID_NUM_HEIGHT - 1
                n_full_line = 0
                for i in range(GRID_NUM_HEIGHT - 1, -1, -1):
                    is_full = True
                    for j in range(GRID_NUM_WIDTH):
                        if screen_color_matrix[i][j] is None:
                            is_full = False
                            continue
                    if not is_full:
                        new_matrix[index] = screen_color_matrix[i]
                        index -= 1
                    else:
                        n_full_line += 1
                score += n_full_line
                level = score // 20 + 1
                screen_color_matrix = new_matrix

            def show_welcome(screen):#显示文字
                screen = pygame.display.set_mode((SCREEN_WIDTH, HEIGHT))
                show_text(screen, u'game', 30, WIDTH / 2, HEIGHT / 2)
                show_text(screen, u'enter', 20, WIDTH / 2, HEIGHT / 2 + 50)



            running = True
            gameover = True
            counter = 0
            live_cube = None
            while running:
                screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if gameover:
                            gameover = False
                            live_cube = CubeShape()
                            break
                        if event.key == pygame.K_LEFT:
                            live_cube.left()
                        elif event.key == pygame.K_RIGHT:
                            live_cube.right()
                        elif event.key == pygame.K_DOWN:
                            live_cube.down()
                        elif event.key == pygame.K_UP:
                            live_cube.rotate()
                        elif event.key == pygame.K_SPACE:
                            while live_cube.down() == True:
                                pass
                        remove_full_line()

                # level 是为了方便游戏的难度，level 越高 FPS // level 的值越小
                # 这样屏幕刷新的就越快，难度就越大
                if gameover is False and counter % (FPS // level) == 0:
                    # down 表示下移骨牌，返回False表示下移不成功，可能超过了屏幕或者和之前固定的
                    # 小方块冲突了
                    if live_cube.down() == False:
                        for cube in live_cube.get_all_gridpos():
                            screen_color_matrix[cube[0]][cube[1]] = live_cube.color
                        live_cube = CubeShape()
                        if live_cube.conflict(live_cube.center):
                            gameover = True
                            score = 0
                            live_cube = None
                            # screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
                    # 消除满行
                    remove_full_line()
                counter += 2
                # 更新屏幕
                screen.fill(BLACK)
                draw_grids()
                draw_matrix()
                draw_score()
                if live_cube is not None:
                    live_cube.draw()
                if gameover:
                    show_welcome(screen)
                pygame.display.flip()
                def main(running):
                    self.running= running
                    running = False
                    #判断
if __name__ == '__main__':
    app = tk.Tk()
    game = Game(app)
    app.mainloop()
