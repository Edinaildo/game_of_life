import pygame
import random

pygame.init()

size = (400, 400)
display = pygame.display.set_mode(size)
pygame.display.set_caption("Jogo da Vida")

relogio = pygame.time.Clock()
done = False

grid = [[random.choice([0, 1]) for _ in range(30)] for _ in range(30)]

def fazer_grade():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                rect = pygame.Surface([10, 10])
                rect.fill((255, 255, 255))
                display.blit(rect, (j*20, i*20))

def mover_proximo():
    temp = [list(i) for i in grid]

    for i in range(len(temp)):
        for j in range(len(temp[1])):
            vizinhos = encontrar_vizinhos(i, j, temp)
            if temp[i][j] == 0 and vizinhos == 3:
                grid[i][j] = 1
            elif temp[i][j] == 1 and (vizinhos < 2 or vizinhos > 3):
                    grid[i][j] = 0
            else:
                grid[i][j] = temp[i][j]


def encontrar_vizinhos(x, y, temp):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            lin = x+1
            col = y+j
            if col > len(temp[0])-1:
                col = 0
            if lin > len(temp)-1:
                lin = 0
            total += temp[lin][col]
    return total-temp[x][y]

while not done:
    display.fill(0)

    fazer_grade()
    mover_proximo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    relogio.tick(1)