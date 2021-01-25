import pygame
pygame.init()

display = pygame.display.set_mode((650, 600))

pygame.display.set_caption("a Car Game")

move_right = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
move_left = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
bg = [pygame.image.load('background-1.png'), pygame.image.load('background-2.png'), pygame.image.load('background-3.png')]
char = pygame.image.load('1.png')

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.left = False
        self.right = False
        self.run_count = 0

# player movement
    def move(self, display):
        if self.run_count + 1 >= 9:
            self.run_count = 0

        if self.left:
            display.blit(move_left[self.run_count // 3], (self.x, self.y))
            self.run_count += 1
        elif self.right:
            display.blit(move_right[self.run_count // 3], (self.x, self.y))
            self.run_count += 1
        else:
            display.blit(char, (self.x, self.y))


car = Player(225, 350, 10, 30)


def game_window():
    display.blit(bg[car.run_count // 3], (0, 0))
    car.move(display)
    pygame.display.update()


run = True
# main window
while run:
    clock.tick(27)
# closing window loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # left arrow key input
    if keys[pygame.K_LEFT] and car.x > car.vel:
        if car.x > 100:
            car.x -= car.vel
            car.left = True
            car.right = False
    # right arrow key input
    elif keys[pygame.K_RIGHT] and car.x < 500 - car.width - car.vel:
        car.x += car.vel
        car.left = False
        car.right = True
    else:
        car.left = False
        car.right = False
        car.run_count = 0

    game_window()

pygame.quit()
