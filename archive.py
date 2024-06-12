import pygame
from sys import exit

pygame.init()

# объявляем ширину и высоту экрана
width = 800
height = 400

# создаём экран игры
screen = pygame.display.set_mode((width, height))

# устанавливаем количество кадров в секунду
fps = 60
# создаём объект таймера
clock = pygame.time.Clock()

# создаём объект шрифта: в скобках указываем шрифт и размер через запятую
text_font = pygame.font.Font('prstartk.ttf', 15)

# создаём новую поверхность
# 1 - задаём размеры:
width_ts = 200
height_ts = 200
# 2 - создаём  поверхность по  размерам
test_surface = pygame.Surface((width_ts, height_ts))
# 3 - добавляем цвет
test_surface.fill('White')

# загружаем в переменную картинки из папки с нашим файлом
back = pygame.image.load('code_game_back_floor.jpg').convert()
hero = pygame.image.load('detective.png').convert_alpha()
pot = pygame.image.load('teapot.png').convert_alpha()
candle = pygame.image.load('candlestick.png').convert_alpha()
box = pygame.image.load('wooden_box.png').convert_alpha()

# объявляем переменные с начальными координатами для всех анимаций
hero_x_pos = 15
hero_y_pos = 130
pot_x_pos = 800
pot_y_pos = 275
candle_x_pos = 800
candle_y_pos = 30
box_x_pos = 800
box_y_pos = 180

# создаём сигнальные переменные
pot_flag = False
box_flag = False

is_move_up = False
is_move_down = False

# создаём объект текста: в скобках указываем текст, сглаживание и цвет
text_surface = text_font.render('Detective CODE Game', False, 'White')

# даём название окну игры
pygame.display.set_caption('Detective CODE Game')

# объявляем переменную-флаг для цикла игры
game = True

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

        # keys = pygame.key.get_pressed()
        #
        # if keys[pygame.K_UP]:
        #     hero_y_pos -= 15
        # if keys[pygame.K_DOWN]:
        #     hero_y_pos += 15

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == pygame.K_UP:
                is_move_up = True
            if key == pygame.K_DOWN:
                is_move_down = True
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            if key == pygame.K_UP:
                is_move_up = False
            if key == pygame.K_DOWN:
                is_move_down = False

    if is_move_up:
        hero_y_pos -= 15

    if is_move_down:
        hero_y_pos += 15

    # размещаем все поверхности на нашем экране
    screen.blit(back, (0, 0))
    screen.blit(hero, (hero_x_pos, hero_y_pos))
    screen.blit(candle, (candle_x_pos, candle_y_pos))
    screen.blit(box, (box_x_pos, box_y_pos))
    screen.blit(pot, (pot_x_pos, pot_y_pos))
    back.blit(text_surface, (250, 15))

    candle_x_pos -= 4
    if candle_x_pos == 400:
        pot_flag = True

    if pot_flag:
        pot_x_pos -= 4

    if pot_x_pos == 400:
        box_flag = True

    if box_flag:
        box_x_pos -= 4

    if candle_x_pos == -100:
        candle_x_pos = 800

    if pot_x_pos == -100:
        pot_x_pos = 800

    if box_x_pos == -100:
        box_x_pos = 1000

    # обновляем экран игры
    pygame.display.update()
    # добавляем к таймеру количество fps для частоты обновления основного цикла
    clock.tick(fps)
