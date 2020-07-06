import pygame, sys, json, os.path, time


# Functions start
pygame.init()
pygame.display.set_caption('World creator')
WINDOW_SIZE = (690,690)
display = pygame.display.set_mode(WINDOW_SIZE)
clock =pygame.time.Clock()

grass_img = pygame.image.load('grass.png')
dirt_img = pygame.image.load('dirt.png')
floor_metal_img = pygame.image.load('floor_metal.png')

font = pygame.font.SysFont('comicsans', 20)

def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def save(data):

    file_name = input('Give the file name')
    with open(file_name +'.json', 'w') as file:
        json.dump(data, file)
    # f = open(file_name + '.txt', 'w')
    # f.write(data)
    # f.close()

def create_world_table(width, height, value=0):
    world_block = []
    for x in range(width):
        world_block.append([])
        for y in range(height):
            world_block[x].append(value)
            # value += 1
    return world_block

name = input('Open file O / New file n : ')
if name == 'O':
    with open(input('Give the name of the .json file: ') + '.json') as json_file:
        blocks = json.load(json_file)
        width = len(blocks)
        print(width)
        height = len(blocks[0])
        print(height)

elif name == 'n':
    width = int(input('Give width: '))
    height = int(input('Give height: '))

    blocks = create_world_table(width, height)
    # walls = create_world_table(width, height)

shift = [0, 0]
speed = 10
brush = 1
ts = 32
menu = True
while True:
    display.fill((146, 244, 255))

    for x in range(shift[0]//ts,shift[0]//ts+WINDOW_SIZE[0]//ts +2):
        for y in range(shift[1]//ts,shift[1]//ts+WINDOW_SIZE[1]//ts +2):
            if -ts < x*ts-shift[0] < WINDOW_SIZE[0] and -ts < y*ts-shift[1] < WINDOW_SIZE[1]:

                if blocks[x][y] == 1:
                    #pygame.draw.rect(display, (250,0,133), (x*ts-shift[0],y*ts-shift[1],ts,ts), 4)
                    display.blit(grass_img, (x * ts - shift[0], y * ts - shift[1], ts, ts))

                elif blocks[x][y] == 2:
                    #pygame.draw.rect(display, (250,250,133), (x*ts-shift[0],y*ts-shift[1],ts,ts))
                    display.blit(dirt_img, (x * ts - shift[0], y * ts - shift[1], ts, ts))

                elif blocks[x][y] == 3:
                    #pygame.draw.rect(display, (250,250,133), (x*ts-shift[0],y*ts-shift[1],ts,ts))
                    display.blit(floor_metal_img, (x * ts - shift[0], y * ts - shift[1], ts, ts))


    M_x, M_y = pygame.mouse.get_pos()[0]+ shift[0], pygame.mouse.get_pos()[1]+shift[1]
    # print(shift)
    if menu:
        draw_place = M_x -shift[0] < WINDOW_SIZE[0] - 100
    else:
        draw_place = M_x - shift[0] < WINDOW_SIZE[0]

    if draw_place:

        if 0 < M_x < width*ts and 0 < M_y < height*ts:
            if pygame.mouse.get_pressed()[0]:
                blocks[M_x//ts][M_y//ts] = brush
            elif pygame.mouse.get_pressed()[1]:
                blocks[M_x // ts][M_y//ts] = 0
        else:
            pass



        if pygame.key.get_pressed()[pygame.K_w]:
            shift[1] -= speed
        elif pygame.key.get_pressed()[pygame.K_s]:
            shift[1] += speed
        elif pygame.key.get_pressed()[pygame.K_a]:
            shift[0] -= speed
        elif pygame.key.get_pressed()[pygame.K_d]:
            shift[0] += speed
        elif pygame.key.get_pressed()[pygame.K_DELETE]:
            blocks = create_world_table(width, height)

    if shift[1] < 0:
        shift[1] = 0
    elif shift[0] < 0:
        shift[0] = 0
    elif shift[1] > height*ts - WINDOW_SIZE[1]:
        shift[1] = height*ts - WINDOW_SIZE[1]
    elif shift[0] > width*ts - WINDOW_SIZE[0]:
        shift[0] = width*ts - WINDOW_SIZE[0]

    # Right Menu
    if pygame.key.get_pressed()[pygame.K_TAB] and menu == True:
        menu = False
        time.sleep(0.1)
    elif pygame.key.get_pressed()[pygame.K_TAB] and menu == False:
        menu = True
        time.sleep(0.1)

    if menu:
        pygame.draw.rect(display, (120, 120, 120), (WINDOW_SIZE[0] - 100, 0, 100, WINDOW_SIZE[1]))

        caption = font.render('TAB to hide', 1, (250, 250, 250))
        display.blit(caption, (WINDOW_SIZE[0]-90, 1))

        display.blit(grass_img, (WINDOW_SIZE[0]-100 + 34, 20))
        if pygame.mouse.get_pressed()[0] and WINDOW_SIZE[0]-100 + 34 < pygame.mouse.get_pos()[0] < WINDOW_SIZE[0]- 34 and 20 < pygame.mouse.get_pos()[1] < 20 + 32:
            brush = 1

        display.blit(dirt_img, (WINDOW_SIZE[0] - 100 + 34, 20 + 1*(10 + 32)))
        if pygame.mouse.get_pressed()[0] and WINDOW_SIZE[0]-100 + 34 < pygame.mouse.get_pos()[0] < WINDOW_SIZE[0]- 34 and 20 +1*(10 +32) < pygame.mouse.get_pos()[1] < 20 + 1*10 + (1+1)*32:
            brush = 2

        pygame.draw.rect(display, (250,0,50), (WINDOW_SIZE[0] - 100 + 34, 20 + 2*(10 + 32), ts, ts),1)
        display.blit(floor_metal_img, (WINDOW_SIZE[0] - 100 + 34, 20 + 2*(10 + 32)))
        if pygame.mouse.get_pressed()[0] and WINDOW_SIZE[0] - 100 + 34 < pygame.mouse.get_pos()[0] < WINDOW_SIZE[0] - 34 and 20 + 2*(10 + 32) < pygame.mouse.get_pos()[1] < 20 + 2*10 + (2+1)*32:
            brush = 3

    # key pressed
    if pygame.key.get_pressed()[pygame.K_1]:
        brush = 1
    if pygame.key.get_pressed()[pygame.K_2]:
        brush = 2
    if pygame.key.get_pressed()[pygame.K_3]:
        brush = 3
    if pygame.key.get_pressed()[pygame.K_4]:
        brush = 4
    if pygame.key.get_pressed()[pygame.K_5]:
        brush = 5
    if pygame.key.get_pressed()[pygame.K_6]:
        brush = 6

    # Save
    if pygame.key.get_pressed()[pygame.K_F12]:
        pygame.quit()
        break

    exit()
    pygame.display.update()
    clock.tick(60)

save(blocks)
