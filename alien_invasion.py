import sys
import pygame

from setting import Setting
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.setting=Setting()

        self.screen=pygame.display.set_mode(
            (self.setting.screen_width,self.setting.screen_height))
        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width=self.screen.get_rect().width
        # self.settings.screen_height=self.sreen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()


        #设置背景色
        self.bg_color=(230,230,230)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            # #监视键盘和鼠标事件
            # for event in pygame.event.get():
            #     if event.type==pygame.QUIT:
            #         sys.exit()

            self._update_screen()
            # #每次循环时都重绘背景
            # self.screen.fill(self.setting.bg_color)
            # self.ship.blitme()

            self.ship.update()
            self.bullets.update()

            self.update_bullets()
            #删除消失的子弹
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom<=0:
            #         self.bullets.remove(bullet)

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    def _check_events(self):
        #监视键盘和鼠标事件
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    # if event.key==pygame.K_RIGHT:
                    #     self.ship.moving_right=True
                    # elif event.key==pygame.K_LEFT:
                    #     self.ship.moving_left=True
                        # #向右移动飞船
                        # self.ship.rect.x+=1
                elif event.type==pygame.KEYUP:
                    self._check_keyup_events(event)
                    # if event.key==pygame.K_RIGHT:
                    #     self.ship.moving_right=False
                    # elif event.key==pygame.K_LEFT:
                    #     self.ship.moving_left=False
                
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True   
        elif event.key==pygame.K_q:
            pygame.quit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
        elif event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False 

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets)<self.setting.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        #每次循环时都重绘背景
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #让最近绘制的屏幕可见
        pygame.display.flip()
        
if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()
