# importing
import pygame

pygame.init()

sizeX = 600
sizeY = 600
size = 9
screen = pygame.display.set_mode((sizeX, sizeY))
pygame.display.set_caption("Turn image To Text")
puppyImg = pygame.transform.scale(pygame.image.load('JackSucksAtLife.webp'), (sizeX, sizeY))
bOrW = "b"

if bOrW == "w":
    text = ["N", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "?",
            "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]

else:
    text = ["_", ".", ",", "-", "=", "+", ":", ";", "c", "b", "a", "!", "?",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "$", "W", "#", "@", "N"]

font = pygame.font.Font('freesansbold.ttf', size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def findColor():
    meanLst = []
    num = 0

    for i in range(sizeY):
        for j in range(sizeX):
            R, G, B, A = puppyImg.get_at((j, i))
            meanLst.append(R)
            meanLst.append(G)
            meanLst.append(B)
            num += 3

            if (i + 1) // size == (i + 1) / size and (j + 1) // size == (j + 1) / size:
                m = 0
                for color in meanLst:
                    m += color
                    num += 1

                if bOrW == "w":
                    mean = m // num

                else:
                    mean = m // (num - 20)
                num = 0
                m = 0
                meanLst = []
                if bOrW == "w":
                    if mean <= 12.5:
                        dText = font.render(text[0], True, (0, 0, 0))

                    elif mean <= 25:
                        dText = font.render(text[1], True, (0, 0, 0))

                    elif mean <= 25 + 12.5:
                        dText = font.render(text[2], True, (0, 0, 0))

                    elif mean <= 50:
                        dText = font.render(text[3], True, (0, 0, 0))

                    elif mean <= 50 + 12.5:
                        dText = font.render(text[4], True, (0, 0, 0))

                    elif mean <= 75:
                        dText = font.render(text[5], True, (0, 0, 0))

                    elif mean <= 75 + 12.5:
                        dText = font.render(text[7], True, (0, 0, 0))

                    elif mean <= 100:
                        dText = font.render(text[7], True, (0, 0, 0))

                    elif mean <= 112.5:
                        dText = font.render(text[8], True, (0, 0, 0))

                    elif mean <= 125:
                        dText = font.render(text[10], True, (0, 0, 0))

                    elif mean <= 125 + 12.5:
                        dText = font.render(text[12], True, (0, 0, 0))

                    elif mean <= 150:
                        dText = font.render(text[13], True, (0, 0, 0))

                    elif mean <= 150 + 12.5:
                        dText = font.render(text[15], True, (0, 0, 0))

                    elif mean <= 175:
                        dText = font.render(text[17], True, (0, 0, 0))

                    elif mean <= 175 + 12.5:
                        dText = font.render(text[18], True, (0, 0, 0))

                    elif mean <= 200:
                        dText = font.render(text[19], True, (0, 0, 0))

                    elif mean <= 200 + 12.5:
                        dText = font.render(text[20], True, (0, 0, 0))

                    elif mean <= 225:
                        dText = font.render(text[21], True, (0, 0, 0))

                    elif mean <= 225 + 12.5:
                        dText = font.render(text[22], True, (0, 0, 0))

                    else:
                        dText = font.render(text[24], True, (0, 0, 0))

                elif bOrW == "l":
                    if mean <= 12.5:
                        dText = font.render("l", True, (R, G, B, 255))

                    elif mean <= 25:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 25 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 50:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 50 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 75:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 75 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 100:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 112.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 125:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 125 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 150:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 150 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 175:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 175 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 200:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 200 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 225:
                        dText = font.render("l", True, (R, G, B))

                    elif mean <= 225 + 12.5:
                        dText = font.render("l", True, (R, G, B))

                    else:
                        dText = font.render("l", True, (R, G, B))


                elif bOrW == "c":
                    if mean <= 12.5:
                        dText = font.render(text[0], True, (R, G, B, 255))

                    elif mean <= 25:
                        dText = font.render(text[1], True, (R, G, B))

                    elif mean <= 25 + 12.5:
                        dText = font.render(text[2], True, (R, G, B))

                    elif mean <= 50:
                        dText = font.render(text[3], True, (R, G, B))

                    elif mean <= 50 + 12.5:
                        dText = font.render(text[4], True, (R, G, B))

                    elif mean <= 75:
                        dText = font.render(text[5], True, (R, G, B))

                    elif mean <= 75 + 12.5:
                        dText = font.render(text[7], True, (R, G, B))

                    elif mean <= 100:
                        dText = font.render(text[7], True, (R, G, B))

                    elif mean <= 112.5:
                        dText = font.render(text[8], True, (R, G, B))

                    elif mean <= 125:
                        dText = font.render(text[10], True, (R, G, B))

                    elif mean <= 125 + 12.5:
                        dText = font.render(text[12], True, (R, G, B))

                    elif mean <= 150:
                        dText = font.render(text[13], True, (R, G, B))

                    elif mean <= 150 + 12.5:
                        dText = font.render(text[15], True, (R, G, B))

                    elif mean <= 175:
                        dText = font.render(text[17], True, (R, G, B))

                    elif mean <= 175 + 12.5:
                        dText = font.render(text[18], True, (R, G, B))

                    elif mean <= 200:
                        dText = font.render(text[19], True, (R, G, B))

                    elif mean <= 200 + 12.5:
                        dText = font.render(text[20], True, (R, G, B))

                    elif mean <= 225:
                        dText = font.render(text[21], True, (R, G, B))

                    elif mean <= 225 + 12.5:
                        dText = font.render(text[22], True, (R, G, B))

                    else:
                        dText = font.render(text[24], True, (R, G, B))

                else:
                    if mean <= 12.5:
                        dText = font.render(text[0], True, WHITE)

                    elif mean <= 25:
                        dText = font.render(text[1], True, WHITE)

                    elif mean <= 25 + 12.5:
                        dText = font.render(text[2], True, WHITE)

                    elif mean <= 50:
                        dText = font.render(text[3], True, WHITE)

                    elif mean <= 50 + 12.5:
                        dText = font.render(text[4], True, WHITE)

                    elif mean <= 75:
                        dText = font.render(text[5], True, WHITE)

                    elif mean <= 75 + 12.5:
                        dText = font.render(text[7], True, WHITE)

                    elif mean <= 100:
                        dText = font.render(text[7], True, WHITE)

                    elif mean <= 112.5:
                        dText = font.render(text[8], True, WHITE)

                    elif mean <= 125:
                        dText = font.render(text[10], True, WHITE)

                    elif mean <= 125 + 12.5:
                        dText = font.render(text[12], True, WHITE)

                    elif mean <= 150:
                        dText = font.render(text[13], True, WHITE)

                    elif mean <= 150 + 12.5:
                        dText = font.render(text[15], True, WHITE)

                    elif mean <= 175:
                        dText = font.render(text[17], True, WHITE)

                    elif mean <= 175 + 12.5:
                        dText = font.render(text[18], True, WHITE)

                    elif mean <= 200:
                        dText = font.render(text[19], True, WHITE)

                    elif mean <= 200 + 12.5:
                        dText = font.render(text[20], True, WHITE)

                    elif mean <= 225:
                        dText = font.render(text[21], True, WHITE)

                    elif mean <= 225 + 12.5:
                        dText = font.render(text[22], True, WHITE)

                    else:
                        dText = font.render(text[24], True, WHITE)

                screen.blit(dText, (j - size, i - size))


run = True
while run:

    if bOrW == "w":
        screen.fill((255, 255, 255))

    else:
        screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    findColor()
    pygame.display.update()

