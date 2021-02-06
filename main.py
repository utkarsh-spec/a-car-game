import pygame
pygame.init()

display = pygame.display.set_mode((650, 600))

pygame.display.set_caption("a Car Game")

move_right = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
move_left = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
bg = [pygame.image.load('background-1.png'), pygame.image.load('background-2.png'), pygame.image.load('background-3.png')]
enemy = pygame.image.load('Car.png')

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.car_move = True
        self.bg_move = True
        self.bg_count = 0

# player movement
    def move(self, display):

        if self.bg_count + 1 >= 9:
            self.bg_count = 0

        if self.bg_move:
            display.blit(bg[self.bg_count // 3], (0, 0))
            self.bg_count += 1

        if self.car_move:
            display.blit(move_left[self.bg_count // 3], (self.x, self.y))
            self.bg_count += 1


class Projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 20

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)


class Enemy(object):
    enemy = pygame.image.load('Car.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5

    def draw(self, display):
        display.blit(enemy, (self.x, self.y))
        self.move()

    def move(self):
        if self.y < 600:
            self.y += self.vel
            if self.y == 600:
                self.y = -200


# main loop
def game_window():
    car.move(display)
    enm.draw(display)
    enm2.draw(display)

    for bullet in bullets:
        bullet.draw(display)
    pygame.display.update()


run = True
bullets = []
# object generator
car = Player(225, 350, 100, 216)
enm = Enemy(100, 100)
enm2 = Enemy(350, 400)

while run:
    clock.tick(18)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 650 and bullet.x > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 500:
            bullets.append(Projectile(round(car.x + car.width//2), round(car.y), 4, (0, 0, 0)))
    # left arrow key input
    if keys[pygame.K_LEFT] and car.x > car.vel:
        if car.x > 100:
            car.x -= car.vel
    # right arrow key input
    elif keys[pygame.K_RIGHT] and car.x < 600 - car.width - car.vel:
        car.x += car.vel
    else:
        car.run_count = 0
    # main function loop
    game_window()

pygame.quit()
