import pygame
pygame.init()

display = pygame.display.set_mode((650, 600))

pygame.display.set_caption("a Car Game")

move_right = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
move_left = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
bg = [pygame.image.load('background-1.png'), pygame.image.load('background-2.png'), pygame.image.load('background-3.png')]
# char = pygame.image.load('1.png')

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


car = Player(225, 350, 100, 216)


def game_window():
    car.move(display)
    for bullet in bullets:
        bullet.draw(display)
    pygame.display.update()


run = True
bullets = []
# main window
while run:
    clock.tick(18)
# closing window loop
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
    elif keys[pygame.K_RIGHT] and car.x < 500 - car.width - car.vel:
        car.x += car.vel
    else:
        car.run_count = 0

    game_window()

pygame.quit()
