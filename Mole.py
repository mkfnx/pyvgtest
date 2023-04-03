import pygame


class Mole(pygame.Rect):
    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, size)
        self.x = x
        self.y = y
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # def hit(self, x, y):
    #     if self.x < x < self.x + self.image.get_width() and self.y < y < self.y + self.image.get_height():
    #         return True
    #     else:
    #         return False
