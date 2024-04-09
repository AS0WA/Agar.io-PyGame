import pygame
from random import randint, choice


pygame.init()
pygame.display.set_caption('game')
resolution = (1900, 1000)
window = pygame.display.set_mode(resolution)


class Player:
    def __init__(self):
        self.x_cord = resolution[0] / 2
        self.y_cord = resolution[1] / 2
        self.radius = 10
        self.speed = 5
        self.hitbox = pygame.Rect(self.x_cord - self.radius, self.y_cord - self.radius, self.radius * 2, self.radius * 2)

    def tick(self, keys, radius):
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.y_cord -= self.speed / 1.5
            self.x_cord -= self.speed / 1.5
        elif (keys[pygame.K_w] or keys[pygame.K_UP]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.y_cord -= self.speed / 1.5
            self.x_cord += self.speed / 1.5
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.y_cord += self.speed / 1.5
            self.x_cord -= self.speed / 1.5
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self.y_cord += self.speed / 1.5
            self.x_cord += self.speed / 1.5

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y_cord += self.speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_cord += self.speed
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y_cord -= self.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_cord -= self.speed

        radius += 10
        self.hitbox = pygame.Rect(self.x_cord - radius, self.y_cord - radius, radius * 2, radius * 2)

    def draw(self, radius):
        radius += 10
        pygame.draw.circle(window, (255, 255, 255), (self.x_cord, self.y_cord), radius)


class Points:
    def __init__(self):
        self.x_cord = randint(0, 1900)
        self.y_cord = randint(0, 1000)
        self.width = 10
        self.height = 5
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 150, 0), (255, 0, 150), (150, 255, 0), (0, 255, 150), (150, 0, 255), (0, 150, 255)]
        self.color = choice(colors)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x_cord, self.y_cord), 7)


class Background:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0

    def tick(self):
        pass

    def draw(self):
        window.fill((0, 0, 0))


def main():
    run = True
    player = Player()
    background = Background()
    clock = 0
    points = []
    score = 0

    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if clock >= 0.1:
            clock = 0
            points.append(Points())

        player.tick(keys, score)
        background.tick()

        for point in points:
            point.tick()

        for point in points:
            if player.hitbox.colliderect(point.hitbox):
                points.remove(point)
                score += 1

        background.draw()
        player.draw(score)
        for point in points:
            point.draw()
        score_text = pygame.font.Font.render(pygame.font.SysFont('arial', 20), f'SCORE: {score}', True, (255, 255, 255))
        window.blit(score_text, (0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()