import pygame
from sys import exit

pygame.init()

# объявляем ширину и высоту экрана
width = 800
height = 400

# устанавливаем количество кадров в секунду
fps = 60
# создаём объект таймера
clock = pygame.time.Clock()

# создаём новую поверхность
# 1 - задаём размеры:
width_ts = 200
height_ts = 200
# 2 - создаём  поверхность по  размерам
test_surface = pygame.Surface((width_ts, height_ts))
# 3 - добавляем цвет
test_surface.fill('White')

# загружаем в переменную картинки из папки с нашим файлом
back = pygame.image.load('code_game_back_floor.jpg')
hero = pygame.image.load('detective.png')
pot = pygame.image.load('teapot.png')
candle = pygame.image.load('candlestick.png')
box = pygame.image.load('wooden_box.png')

# даём название окну игры
pygame.display.set_caption("Detective CODE Game")

# объявляем переменную-флаг для цикла игры
game = True

# создаём экран игры
screen = pygame.display.set_mode((width, height))

# запускаем бесконечный цикл
while game:
    # получаем список возможных действий игрока
    for event in pygame.event.get():
        # если пользователь нажал на крестик закрытия окна
        if event.type == pygame.QUIT:
            # выключаем цикл
            pygame.quit()
            # добавляем корректное завершение работы
            exit()

    # размещаем новые поверхности на нашем экране
    screen.blit(back, (0, 0))
    screen.blit(hero, (15, 130))
    screen.blit(candle, (675, 30))
    screen.blit(box, (700, 180))
    screen.blit(pot, (675, 275))

    # обновляем экран игры
    pygame.display.update()
    # добавляем к таймеру количество fps для частоты обновления основного цикла
    clock.tick(fps)
