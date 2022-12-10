import pygame


class Button():
    def __init__(self, sf, img, width, height, x, y):
        self.sf = sf
        self.origin = pygame.image.load(img)
        self.img = pygame.transform.scale(self.origin, (width, height))
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, ):
        self.sf.blit(self.img, (self.x, self.y))
        pygame.display.flip()

    def check_click(self, mouse_pos):
        mx, my = mouse_pos
        return (self.x <= mx <= self.x + self.width) and (self.y <= my <= self.y + self.height)

    def resize(self, widthIn, heightIn):
        self.img = pygame.transform.scale(self.origin, (widthIn, heightIn))

    def move(self, newx, newy):
        self.x = newx
        self.y = newy


def update():
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((500, 500))
color = (255, 0, 0)
button = Button(screen, "pixilart-drawing.png", 250, 250, 20, 20)
while True:
    button.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.check_click(event.pos):
                print('Нажали на кнопку')

