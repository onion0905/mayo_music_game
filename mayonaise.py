import pygame
import math
pygame.init()

# Screen
wn = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Is Mayonnaise an Instrument?")
mayo = pygame.image.load("images\mayo.webp")
pygame.display.set_icon(mayo)

# Back Ground
start_menu = pygame.image.load("images\patrick_mayo.jpg")
start_menu = pygame.transform.scale(start_menu, (800, 600))
start_button = pygame.image.load("images\start_button.png")
start_button = pygame.transform.scale(start_button, (200, 100))
mayo = pygame.transform.rotate(mayo, 90)
mayo = pygame.transform.scale(mayo, (100, 100))

 
# Objects
slot = (125, 30)
rect = pygame.Rect(200, 0, 10, 600)
white_back = pygame.Rect(0, 0, 800, 600)
border_left_line = pygame.Rect(140, 0, 10, 600)
border_right_line = pygame.Rect(650, 0, 10, 600)
display_pressed1 = pygame.Rect(150, 500, slot[0], slot[1])
display_pressed2 = pygame.Rect(275, 500, slot[0], slot[1])
display_pressed3 = pygame.Rect(400, 500, slot[0], slot[1])
display_pressed4 = pygame.Rect(525, 500, slot[0], slot[1])


# Main process
running = True
back = 0
mouse = ""
while running:
    mouse_pos = pygame.mouse.get_pos()
    # background displaying
    if back:
        pygame.draw.rect(wn, (107, 186, 241), white_back) #waiting to be fixed
        pygame.draw.rect(wn, (255, 255, 0), border_left_line)
        pygame.draw.rect(wn, (255, 255, 0), border_right_line)
        
        pygame.draw.line(wn, (255, 255, 255), (275, 0),(275, 600))
        pygame.draw.line(wn, (255, 255, 255), (400, 0),(400, 600))
        pygame.draw.line(wn, (255, 255, 255), (525, 0),(525, 600))
        
        pygame.draw.line(wn, (100, 100, 100), (150, 500),(650, 500))
        pygame.draw.line(wn, (100, 100, 100), (150, 530),(650, 530))
    else:
        wn.blit(start_menu, (0, 0))
        wn.blit(start_button, (370, 70))
        if mouse == "down":
            if mouse_pos[0] > 300 and mouse_pos[0] < 500 and mouse_pos[1] > 100 and mouse_pos[1] < 200:
                back = 1

    # pressed key displaying
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed1)
        wn.blit(mayo, (160, 500))
    if keys[pygame.K_f]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed2)
    if keys[pygame.K_j]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed3)
    if keys[pygame.K_k]:
        pygame.draw.rect(wn, (99, 170, 219), display_pressed4)
    
    
    # pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = "down"
            print(mouse)
        if event.type != pygame.MOUSEBUTTONDOWN:
            mouse = ""
    

    #print(mouse_pos)
    pygame.display.update()