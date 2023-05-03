import os
import sys
import random
import pygame
from pygame import gfxdraw
from create_labyrynth import printLabyrynth

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(20, 20, 16, 16)

    def moving(self, dx, dy):
        if dx != 0:
            self.moving_single_axis(dx, 0)
        if dy != 0:
            self.moving_single_axis(0, dy)

    def moving_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.shock(dx, dy)

    def shock(self, dx, dy):
        for Divider in Dividers:
            if self.rect.colliderect(Divider.rect):
                if dx > 0:
                    self.rect.right = Divider.rect.left
                if dx < 0:
                    self.rect.left = Divider.rect.right
                if dy > 0:
                    self.rect.bottom = Divider.rect.top
                if dy < 0:
                    self.rect.top = Divider.rect.bottom


class Divider(object):

    def __init__(self, pos):
        Dividers.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


os.environ["SDL_VIDEO_CENTERED"] = "1"
level = printLabyrynth()
pygame.init()

pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((560, 570))

time = pygame.time.Clock()
Dividers = []
player = Player()

# Holds the level layout in a list of strings.


# Parse the level string above. W = Divider, E = exit
x = y = 1
for row in level:
    for col in row:
        if col == "w":
            Divider((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 18
    y += 18
    x = 1

fleeing = True
while fleeing:

    time.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            fleeing = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            fleeing = False

    # moving the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.moving(-2, 0)
    if key[pygame.K_RIGHT]:
        player.moving(2, 0)
    if key[pygame.K_UP]:
        player.moving(0, -2)
    if key[pygame.K_DOWN]:
        player.moving(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        pygame.quit()
        sys.exit()

    # Draw the scene
    screen.fill((0, 0, 0))
    for Divider in Dividers:
        pygame.draw.ellipse(screen, (230, 8, 8), Divider.rect)
        pygame.draw.rect(screen, (0, 153, 0), end_rect)
        pygame.draw.rect(screen, (239, 255, 0), player.rect)
    # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,128))
    pygame.display.flip()
    time.tick(360)

pygame.quit()