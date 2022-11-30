import pygame
import numpy as np

# variables
PHNM = 6041234567 # need to make some kinda input for this
NAME = "maki"
WIDTH = 1000
HEIGHT = 800
count = 0
botnum = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
BALLNUM = 10
BALLCOL = []
for b in np.arange(BALLNUM):
    BALLCOL.append(np.random.randint(50, 256, size=3))

# initial positions, velocities
posx = WIDTH*np.linspace(0.1, 0.9, BALLNUM)
posy = HEIGHT*np.random.rand(BALLNUM)
vy = 0.5

def update():
    """
    moves balls down, if they go past the screen move
    them back to the top
    """
    global posx, posy, vy
    for p in np.arange(len(posy)):
        if posy[p] + vy >= HEIGHT:
            posy[p] = 0
        else:
            posy[p] += vy

def render(screen):
    """
    renders balls
    """

    # draw balls
    for b in np.arange(BALLNUM):
        font = pygame.font.SysFont(None, 42)
        img = font.render(str(b), True, (0, 0, 0))
        pygame.draw.circle(screen, BALLCOL[b], (posx[b], posy[b]), 50)
        screen.blit(img, (posx[b]-8, posy[b]-14))
    font2 = pygame.font.SysFont(None, 80)
    img2 = font2.render("".join(botnum), True, (0, 0, 0))
    img3 = font2.render(NAME, True, (0, 0, 0))
    screen.blit(img2, (WIDTH / 2 - 180, HEIGHT - 180))
    screen.blit(img3,(WIDTH / 2 - 90, HEIGHT - 110))
    pygame.display.update()

def run_game():
    """
    runs poke-a-dot game.
    """
    global botnum, count, posx, posy, BALLCOL
    ph_number = "{0}".format(PHNM)
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    # run game
    running = True
    while running:

        pygame.mouse.set_visible(True)

        # white bg
        screen.fill((255, 255, 255))

        if ph_number == "":
            font3 = pygame.font.SysFont(None, 150)
            font4 = pygame.font.SysFont(None, 50)
            img = font3.render("Good Job!", True, (0, 0, 0))
            img2 = font4.render("+ 15 myelin. press space to restart.", True, (0,128,0))
            screen.blit(img, (WIDTH/5+25, HEIGHT/2 - 100))
            screen.blit(img2, (WIDTH / 7 + 60, HEIGHT / 2))
            pygame.display.update()
        else:
            # number we want to be clicked:
            num = ph_number[0]
            pos = [[x, y] for x, y in zip(posx, posy)]
            circ = pos[int(num)]

        for event in pygame.event.get():
            # close game
            if event.type == pygame.QUIT:
                running = False
            # check if right num clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                # math things!
                sqx = (x - circ[0]) ** 2
                sqy = (y - circ[1]) ** 2
                if (sqx + sqy) < 2500:
                    # place num on screen
                    botnum[count] = num
                    render(screen)
                    # remove first number
                    ph_number = ph_number[1:]
                    count += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    botnum = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
                    ph_number = str(PHNM)
                    count = 0
                    posx = WIDTH * np.linspace(0.1, 0.9, BALLNUM)
                    posy = HEIGHT * np.random.rand(BALLNUM)
                    BALLCOL = []
                    for b in np.arange(BALLNUM):
                        BALLCOL.append(np.random.randint(50, 256, size=3))
        if ph_number != "":
            update()
            render(screen)

run_game()