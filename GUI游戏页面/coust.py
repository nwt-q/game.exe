GRID_WIDTH = 30  # 格栏宽度
GRID_NUM_WIDTH = 15  # 网格的宽度
GRID_NUM_HEIGHT = 25  # 网格的高度
WIDTH, HEIGHT = GRID_WIDTH * GRID_NUM_WIDTH, GRID_WIDTH * GRID_NUM_HEIGHT  # 游戏总界面大小
SIDE_WIDTH = 200
SCREEN_WIDTH = WIDTH + SIDE_WIDTH
WHITE = (0xff, 0xff, 0xff)
BLACK = (0, 0, 0)

LINE_COLOR = (0x33, 0x33, 0x33)

CUBE_COLORS = [
    (220, 20, 60), (0, 191, 255), (173, 216, 230),
    (0x99, 0x00, 0x66), (0xff, 0xcc, 0x00), (0xcc, 0x00, 0x33),
    (0xff, 0x00, 0x33), (0x00, 0x66, 0x99), (60, 179, 113),
    (0x99, 0x00, 0x33), (0xcc, 0xff, 0x66), (128, 128, 0),
]