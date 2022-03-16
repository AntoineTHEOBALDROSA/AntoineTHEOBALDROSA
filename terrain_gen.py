import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Terrain Generation")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SIZE = 10


def generate_random_map(WIDTH, HEIGHT):
    map = []
    for i in range(WIDTH//SIZE):
        L = []
        for j in range(HEIGHT//SIZE):
            if random.randint(0, 20) <= 10:
                L.append(1)  # green
            else:
                L.append(0)  # blue
        map.append(L)
    return map


def smooth_map(map):
    for i in range(len(map)):  # len(map)-1
        for j in range(len(map[i])):  # len(map[i])-1
            neighboor = []
            try:
                neighboor.append(map[i-1][j-1])
            except:
                pass
            try:
                neighboor.append(map[i-1][j])
            except:
                pass
            try:
                neighboor.append(map[i-1][j+1])
            except:
                pass
            try:
                neighboor.append(map[i][j-1])
            except:
                pass
            try:
                neighboor.append(map[i][j+1])
            except:
                pass
            try:
                neighboor.append(map[i+1][j-1])
            except:
                pass
            try:
                neighboor.append(map[i+1][j])
            except:
                pass
            try:
                neighboor.append(map[i+1][j+1])
            except:
                pass

            L = [0, 0]  # green, blue = 0, 0
            for elt in neighboor:
                if elt == 0:
                    L[1] += 1
                else:
                    L[0] += 1

            if L[0] > L[1]:
                map[i][j] = 1
            elif L[1] > L[0]:
                map[i][j] = 0

    return map


def draw_map(WIN, map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                pygame.draw.rect(WIN, BLUE, pygame.Rect(
                    i*SIZE, j*SIZE, (i+1)*SIZE, (j+1)*SIZE))

            else:
                pygame.draw.rect(WIN, GREEN, pygame.Rect(
                    i*SIZE, j*SIZE, (i+1)*SIZE, (j+1)*SIZE))


def place_random(map, color, number):
    if color == "green":
        color = 1
    elif color == "blue":
        color = 0

    for i in range(number):
        row = random.randint(0, len(map)-1)
        column = random.randint(0, len(map)-1)
        print(row, column)
        map[row][column] = color
        if random.randint(0, 10) <= 4:
            try:
                map[row+1][column] = color
                map[row-1][column] = color
                map[row][column-1] = color
                map[row][column+1] = color
            except:
                pass

    return map


def main():
    run = True
    clock = pygame.time.Clock()

    map = generate_random_map(WIDTH, HEIGHT)
    draw_map(WIN, map)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    draw_map(WIN, smooth_map(map))

                if event.key == pygame.K_b:
                    place_random(map, "blue", 300)
                    draw_map(WIN, map)

                if event.key == pygame.K_g:
                    place_random(map, "green", 300)
                    draw_map(WIN, map)

                if event.key == pygame.K_c:
                    map = generate_random_map(WIDTH, HEIGHT)
                    draw_map(WIN, map)

        pygame.display.update()

    pygame.quit()


main()

# ESPACE : smooth
# C : clear
# B : rajouter du bleu
# G : rajouter du vert (green)
# modifier la taille des pixels : modifier SIZE ligne 14
