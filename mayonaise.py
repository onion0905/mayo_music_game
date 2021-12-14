import pygame
import math
import time
pygame.init()

# Screen
wn = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Is Mayonnaise an Instrument?")
mayo = pygame.image.load("D:\program project\python_project\Games\mayo_music_game\images\mayo.webp")
pygame.display.set_icon(mayo)

# Back Ground
start_menu = pygame.image.load("D:\program project\python_project\Games\mayo_music_game\images\patrick_mayo.jpg")
start_menu = pygame.transform.scale(start_menu, (800, 600))
start_button = pygame.image.load("D:\program project\python_project\Games\mayo_music_game\images\start_button.png")
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
music = "D:\\program project\\python_project\\Games\\mayo_music_game\\images\\ver.hard.mp3"
track = pygame.mixer.music.load(music)

# Notes
'''
Time format:
ex: 0005.00
first four digits are for second
last two digits are for milisecond
'''

times_arrive = []
times_drop = []
notes = []
note_dict = {64:0, 192:1, 320:2, 448:3}
with open("D:\\program project\\python_project\\Games\\mayo_music_game\\times.txt", "r") as time_f:
    for i in time_f:
        i = int(i)
        i /= 1000
        i = round(i, 4)
        times_arrive.append(i)

with open("D:\\program project\\python_project\\Games\\mayo_music_game\\notes.txt", "r") as note_f:
    for i in note_f:
        i = int(i)
        i = note_dict[i]
        notes.append(i)

for i in times_arrive:
    i -= 1
    i = round(i, 4)
    times_drop.append(i)

# Functions
locations = [160, 285, 410, 535]
# def show_mayo(note):
#     for i in range(len(note)):
#         if note[i] == '1':
#             wn.blit(mayo, (locations[i], 50))
#             print("blitted")

print(times_arrive)
print(times_drop)
# Main process
running = True
back = 0
mouse = ""
pointer = 0
start_time = 0
started = False
ended = False
showing_array = []
tapping_array = []
while running:
    mouse_pos = pygame.mouse.get_pos()
    now_time = time.time()
    if not started:
        start_time = now_time
    time_pass = float(now_time - start_time)
    time_pass = round(time_pass, 4)
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
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                started = True
                start_time = time.time()

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

    # Notes displaying
    
    #print(time_pass)
    #print(float(times_drop[pointer]))
    #print(notes[pointer])
    #print(type(notes[pointer]))
    while time_pass <= (times_drop[pointer])+0.1 and time_pass >= (times_drop[pointer])-0.1 and not ended:
        data_array = []
        data_array = [times_drop[pointer], locations[notes[pointer]], -100, times_arrive[pointer]]
        showing_array.append(data_array)
        print(data_array)
        pointer += 1
        if pointer > len(times_drop) - 2:
            ended = True

    for i in range(len(showing_array)):
        try:
            showing_array[i][2] += 1
            if showing_array[i][3] < time_pass - 0.5:
                del(showing_array[i])
            else:
                wn.blit(mayo, (showing_array[i][1], showing_array[i][2]))
        except:
            break

    
    
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