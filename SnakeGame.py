import pygame
import time
import random


pygame.init()


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (169, 169, 169)

#Dimensões d
width = 600
height = 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo da Cobra')


clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def mostrar_pontuacao(score):
    value = score_font.render("Pontuação: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def desenhar_cobra(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def desenhar_obstaculos(obstaculos, snake_block):
    for obst in obstaculos:
        pygame.draw.rect(dis, gray, [obst[0], obst[1], snake_block, snake_block])


def mensagem(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    
    x1 = width / 2
    y1 = height / 2

    
    x1_change = 0
    y1_change = 0

    
    snake_list = []
    length_of_snake = 1

    
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Gerar obstáculos aleatórios
    obstaculos = []
    for _ in range(30):  
        obst_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        obst_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        obstaculos.append([obst_x, obst_y])

    while not game_over:

        while game_close:
            dis.fill(blue)
            mensagem("Você perdeu! Pressione Q-Quit ou C-Continuar", red)
            mostrar_pontuacao(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Atualiza a posição da cobra
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        # Desenhar os obstáculos
        desenhar_obstaculos(obstaculos, snake_block)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Verifica se a cobra colidiu com seu corpo
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Verifica se a cobra colidiu com um obstáculo
        for obst in obstaculos:
            if x1 == obst[0] and y1 == obst[1]:
                game_close = True

        desenhar_cobra(snake_block, snake_list)
        mostrar_pontuacao(length_of_snake - 1)

        pygame.display.update()

        # Se a cobra comer a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
