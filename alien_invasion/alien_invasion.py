# import sys # for only used in gf ( gf already import
import pygame
# import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
# from alien import Alien
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()

    # alien_invasion settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#   screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建用于存储子弹和外星人的编组
    bullets = Group()
    aliens = Group()
    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 设置背景色(not use settings.py
#   bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # if stats.game_active == False:
        #     print("game over!")
run_game()