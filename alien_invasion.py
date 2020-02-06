
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    # 初始化pygame、设置和屏幕对象
    pygame.init()

    ai_settings = Settings()


    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    # bg_color = (230, 230, 230)

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        gf.check_events()


        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()


        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()