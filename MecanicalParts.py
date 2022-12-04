import pygame


class Button():
    def __init__(self, sf, img, width, height, x, y):
        self.sf = sf
        self.origin = pygame.image.load(img)
        self.img = pygame.transform.scale(self.origin, (40, 10))
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, ):
        self.sf.blit(self.img, (self.x, self.y))
        pygame.display.flip()

    def run(self):
        a = self.x + self.width
        b = self.y + self.height
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.mouse.get_pos() >= (self.x, self.y):
                    print('click')

    def resize(self, widthIn, heightIn):
        image = pygame.transform.scale(self.sf, (widthIn, heightIn))

    def move(self, newx, newy):
        self.x = newx
        self.y = newy


def update():
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((500, 500))
color = (255, 0, 0)
while True:
    button = Button(screen, "pixilart-drawing.png", 250, 250, 20, 20)
    button.draw()
    button.run()

import pygame


class Button():
    def __init__(self, sf, img, width, height, x, y):
        self.sf = sf
        self.img = img
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, ):
        image = pygame.image.load(self.img)
        self.sf.blit(image, (self.x, self.y))
        pygame.display.flip()

    def run(self):
        a = self.x + self.width
        b = self.y + self.height
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.mouse.get_pos() >= (self.x, self.y) and pygame.mouse.get_pos() >= (a, b):
                    print('click')

    def resize(self, widthIn, heightIn):
        image = pygame.transform.scale(self.sf, (widthIn, heightIn))

    def move(self, newx, newy):
        self.x = newx
        self.y = newy


def update():
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((500, 500))
color = (255, 0, 0)
while True:
    button = Button(screen, "pixilart-drawing.png", 250, 250, 20, 20)
    button.draw()
    button.run()

