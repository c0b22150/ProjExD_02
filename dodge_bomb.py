import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    r_bomb = pg.Surface((20, 20))
    pg.draw.circle(r_bomb, (255, 0, 0), (10, 10), 10)
    r_bomb.set_colorkey((0, 0, 0))
    rx = random.randint(0,WIDTH)
    ry = random.randint(0,HEIGHT)
    rb_rect = r_bomb.get_rect()
    rb_rect.center = rx, ry
    vx, vy = +5, +5
    clock = pg.time.Clock()
    clock.tick(50)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        rb_rect.move_ip(vx, vy)
        screen.blit(r_bomb, rb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()