import pygame
from pygame.draw import circle, rect
from random import randrange
import json

pygame.init()

FPS = 30
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
MAX_SPEED = 15
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Ball():
    def __init__(self):
        self.radius = randrange(51)
        self.x = randrange(self.radius, SCREEN_WIDTH - self.radius + 1)
        self.y = randrange(self.radius, SCREEN_HEIGHT - self.radius + 1)
        self.speed_x = randrange(-MAX_SPEED, MAX_SPEED + 1)
        self.speed_y = randrange(-MAX_SPEED, MAX_SPEED + 1)
        self.color = (randrange(256), randrange(256), randrange(256))
        self.point = 1
        circle(screen, self.color, (self.x, self.y), self.radius, 0)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Проверки столкновения шарика со стенами и вызов метода отражения 
        # в случае столкновения
        if self.x - self.radius < 0:
            self.reflection(0, MAX_SPEED + 1, -MAX_SPEED, MAX_SPEED + 1)
        elif self.x + self.radius > SCREEN_WIDTH:
            self.reflection(-MAX_SPEED, 0, -MAX_SPEED, MAX_SPEED + 1)
        if self.y - self.radius < 0:
            self.reflection(-MAX_SPEED, MAX_SPEED + 1, 0, MAX_SPEED + 1)
        elif self.y + self.radius > SCREEN_HEIGHT:
            self.reflection(-MAX_SPEED, MAX_SPEED + 1, -MAX_SPEED, 0)
        circle(screen, self.color, (self.x, self.y), self.radius, 0)

    def reflection(self, x_speed_min_limit, x_speed_max_limit,
                   y_speed_min_limit, y_speed_max_limit):
        self.speed_x = randrange(x_speed_min_limit, x_speed_max_limit, )
        self.speed_y = randrange(y_speed_min_limit, y_speed_max_limit)

    def hit_check(self, click):
        # Проверка с помощью теоремы Пифагора попадания по шарику
        if (click.pos[0] - self.x) ** 2 + (click.pos[1] - self.y) ** 2 <= \
                self.radius ** 2:
            return True


class Square_with_hole():
    def __init__(self):
        self.ext_size = randrange(30, 101)
        self.int_size = int(self.ext_size * 0.5)
        self.thickness = (self.ext_size - self.int_size) // 2
        self.x = randrange(self.ext_size, SCREEN_WIDTH - self.ext_size + 1)
        self.y = randrange(self.ext_size, SCREEN_HEIGHT - self.ext_size + 1)
        self.color = (randrange(256), randrange(256), randrange(256))
        self.point = 2
        rect(screen, self.color, [self.x, self.y, self.ext_size,
                                  self.ext_size], 0)
        rect(screen, BLACK, [self.x + self.thickness, self.y + self.thickness,
                             self.int_size, self.int_size], 0)

    def move(self):
        self.x += randrange(-MAX_SPEED, MAX_SPEED + 1)
        self.y += randrange(-MAX_SPEED, MAX_SPEED + 1)
        # Проверки столкновения прямоугольника с отверстием со стенами и 
        # вызов метода отражения в случае столкновения
        if self.x < 0:
            self.reflection(0, MAX_SPEED + 1, -MAX_SPEED, MAX_SPEED + 1)
        elif self.x + self.ext_size > SCREEN_WIDTH:
            self.reflection(-MAX_SPEED, 0, -MAX_SPEED, MAX_SPEED + 1)
        if self.y < 0:
            self.reflection(-MAX_SPEED, MAX_SPEED + 1, 0, MAX_SPEED + 1)
        elif self.y + self.ext_size > SCREEN_HEIGHT:
            self.reflection(-MAX_SPEED, MAX_SPEED + 1, -MAX_SPEED, 0)
        rect(screen, self.color, [self.x, self.y, self.ext_size,
                                  self.ext_size], 0)
        rect(screen, BLACK, [self.x + self.thickness, self.y + self.thickness,
                             self.int_size, self.int_size], 0)

    def reflection(self, x_speed_min_limit, x_speed_max_limit,
                   y_speed_min_limit, y_speed_max_limit):
        self.x += randrange(x_speed_min_limit, x_speed_max_limit, )
        self.y += randrange(y_speed_min_limit, y_speed_max_limit)

    def hit_check(self, click):
        # Проверка по координатам попадания по прямоугольнику с отверстием
        if (self.x <= click.pos[0] <= self.x + self.ext_size and
            self.y <= click.pos[1] <= self.y + self.ext_size) and not \
                (self.x + self.thickness <= click.pos[0] <= self.x + self.thickness +
                 self.int_size and self.y + self.thickness <= click.pos[1] <= self.y +
                 self.thickness + self.int_size):
            return True


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
# Извлечение данных из таблицы рекордов в соответствии с именем игрока или 
# создание для него ячейки в таблице, если его там не было
with open('record_table.json') as f:
    data = json.load(f)
name = input('Имя игрока: ')
if name in data:
    max_prev_score = data[name][-1]
else:
    data[name] = []
    max_prev_score = 0
# Создание шариков
target_list = []
for i in range(randrange(3, 9)):
    target_list.append(Ball())
# Создание квадратов с отверстием
for i in range(randrange(3, 9)):
    target_list.append(Square_with_hole())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Запуск проверки попадания по мишени для каждой мишени, 
            # увеличение количества очков при попадании
            for target in target_list:
                if target.hit_check(event):
                    score += target.point
                    print('Score: ' + str(score))
    screen.fill(BLACK)
    for target in target_list:
        target.move()
    pygame.display.update()
# Запись нового рекорда в таблицу в случае его установления и 
# загрузка данных в файл
if score > max_prev_score:
    data[name].append(score)
with open('record_table.json', 'w') as f:
    json.dump(data, f)

print('История ваших рекордов:')
print(' '.join([str(record) for record in data[name]]))

print('Рейтинг игроков:')
players_and_records_list = []
for player_name in data:
    players_and_records_list.append((player_name, data[player_name][-1]))
players_and_records_list.sort(key=lambda x: -x[1])
number = 1
for pair in players_and_records_list:
    print(number, pair[0], pair[1])
    number += 1

pygame.quit()
