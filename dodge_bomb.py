import random
import sys
import pygame as pg
import time


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}


def check_bound(rect) -> tuple[bool, bool]:
    """
    こうかとんrect, 爆弾rect が画面内か画面外かを判定する関数
    引数：こうかとんrect or 爆弾rect
    戻り値：横方向と縦方向の判定結果タプル(True:画面内, False:画面外)
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:
        yoko = False 
    if rect.top < 0 or HEIGHT < rect.bottom:
        tate = False
    return yoko, tate




def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400
    r_bomb = pg.Surface((20, 20))
    pg.draw.circle(r_bomb, (255, 0, 0), (10, 10), 10)
    r_bomb.set_colorkey((0, 0, 0))
    rx = random.randint(0,WIDTH)
    ry = random.randint(0,HEIGHT)
    rb_rect = r_bomb.get_rect()
    rb_rect.center = rx, ry
    vx, vy = +5, +5
    clock = pg.time.Clock()
    tmr = 0

    font = pg.font.Font(None, 80)
    moji = font.render("Finish!!", True, (0, 0, 255))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if kk_rect.colliderect(rb_rect):
            screen.blit(moji, [WIDTH/2, HEIGHT/2])
            pg.display.update()
            print("ゲームオーバー")
            time.sleep(2)
            return 
        key_list = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_list[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rect.move_ip(sum_mv)
        if check_bound(kk_rect) != (True, True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        rb_rect.move_ip(vx, vy)
        yoko, tate = check_bound(rb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(r_bomb, rb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()