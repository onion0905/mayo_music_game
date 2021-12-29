import pygame as pg
pg.init()

#設定視窗背景
width, height = 640, 480                      
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("Sean's game")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

#藍球建立
ball = pg.Surface((70,70))     #建立球矩形繪圖區
ball.fill((255,255,255))       #矩形區塊背景為白色
pg.draw.circle(ball, (0,0,255), (35,35), 35, 0)  #畫藍色球
rect = ball.get_rect()         #取得球矩形區塊
rect.center = (320,240)        #球起始位置
x, y = rect.topleft            #球左上角坐標
speed = 3                      #球運動速度
clock = pg.time.Clock()        #建立時間元件

#關閉程式的程式碼
running = True
while running:
    clock.tick(30)        #每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    x += speed                 #改變水平位置
    rect.center = (x,y)        #坐標差異讓它移動
    if(rect.left <= 0 or rect.right >= screen.get_width()):   #到達左右邊界
        speed *= -1            #正負值交換

            
    screen.blit(bg, (0,0))
    screen.blit(ball, rect.topleft)  #繪製藍球
    pg.display.update()     #更新視窗
    
pg.quit()