# импортируем зависимости и дополнительные модули
import pygame
from sys import exit
import time

# включаем модуль pygame
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

# добавляем счётчики для подсчёта времени в игре - это будут наши очки
start_time = 0
final_score = 0

# загружаем в переменные картинки из папки с нашим файлом
back_main_screen = pygame.image.load('code_game_back.jpg').convert()
back = pygame.image.load('code_game_back_floor.jpg').convert()
hero = pygame.image.load('detective.png').convert_alpha()
pot = pygame.image.load('teapot.png').convert_alpha()
candle = pygame.image.load('candlestick.png').convert_alpha()
box = pygame.image.load('wooden_box.png').convert_alpha()

# даём название окну игры
pygame.display.set_caption('Detective CODE Game')

# объявляем переменную-флаг для цикла игры
game = False

# создаём объекты текста: в первой строчке задаём настройки шрифта,
# во второй сам текст и его цвет, в третьей - помещаем текст
# в прямоугольную рамку и размещаем на заднных координатах

# текст с названием игры
text_font = pygame.font.Font('prstartk.ttf', 15)
text_surface = text_font.render('Detective CODE Game', False, 'White')
text_name_rect = text_surface.get_rect(center=(400, 30))

# текст с сообщением о столкновении
text_font_collide = pygame.font.Font('prstartk.ttf', 50)
text_collide = text_font_collide.render('CoLLiDE!!', False, 'Red')
text_collide_rect = text_collide.get_rect(center=(400, 200))

# текст главного меню
text_font_new_game = pygame.font.Font('prstartk.ttf', 20)
text_newgame_str1 = text_font_new_game.render('If you want to start,', False, 'Green')
text_newgame_rect1 = text_newgame_str1.get_rect(center=(400, 325))
text_newgame_str2 = text_font_new_game.render('press space', False, 'Green')
text_newgame_rect2 = text_newgame_str2.get_rect(center=(400, 350))

# текст для подсчёта очков
text_font_score = pygame.font.Font('prstartk.ttf', 15)
# текст для вывода очков при окончании игры
text_ts_font = pygame.font.Font('prstartk.ttf', 20)


# функция подсчёта очков
def display_score():
    # получаем время текущей игры: от общего времени в игре мы
    # отнимаем время, сыгранное за время запуска скрипта
    current_time = pygame.time.get_ticks() - start_time
    # создаём объект текста количества очков - сыгранное время
    score_surface = text_font_score.render(f'{current_time}', False, 'Purple')
    # помещаем текст с количеством очков в прямоугольник
    score_rect = score_surface.get_rect(bottomright=(795, 395))
    # размещаем прямоугольник на поверхности
    screen.blit(score_surface, score_rect)
