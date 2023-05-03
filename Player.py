import pygame

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