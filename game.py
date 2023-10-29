import pygame
import random
import datetime

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Diwali Animation")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
font_cursive = pygame.font.Font(pygame.font.get_default_font(), 36)
date_message = font_cursive.render("Advance Happy Diwali", True, (255, 255, 255))
happy_diwali_date = datetime.date(2023, 11, 11)
today = datetime.date.today()

cracker_speed = 2.2

class Cracker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        color_choices = [(255, 223, 186), (255, 255, 186), (255, 150, 150)]  
        self.color = random.choice(color_choices)
        self.radius = random.randint(10, 20)  
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 2 * self.radius)
        self.rect.y = screen_height

    def update(self):
        self.rect.y -= cracker_speed

all_sprites = pygame.sprite.Group()
crackers = pygame.sprite.Group()
clicked_cracker = None  # Variable to store the clicked cracker

def create_cracker():
    cracker = Cracker()
    all_sprites.add(cracker)
    crackers.add(cracker)

def explode_cracker(cracker):
    cracker.kill()

display_diwali_message = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for cracker in crackers:
        if cracker.rect.collidepoint(mouse_x, mouse_y):
            crackers.remove(cracker)
            explode_cracker(cracker)
            if not today >= happy_diwali_date:
                display_diwali_message = True  

    if random.randint(0, 100) < 5:
        create_cracker()

    all_sprites.update()

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)

    if display_diwali_message:
        if today >= happy_diwali_date:
            text = "Happy Diwali"
        else:
            text = "Advance Happy Diwali"
        date_message = font_cursive.render(text, True, (255, 255, 255))
        screen.blit(date_message, (screen_width // 2 - date_message.get_width() // 2, screen_height // 2 - date_message.get_height() // 2))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()







































