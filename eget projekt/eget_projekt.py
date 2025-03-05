import pygame
pygame.init()
score = 0
font = pygame.font.Font(None, 32)
text = font.render('score: 0', True, WHITE, BLACK)
textRect = text.get_rect()
textRect.center = (700 // 2, 50)
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tryck på bollen")

circle_x = 50
circle_y = 50
circle_radius = 25
circle_speed_y = 1
circle_speed_x = 1
 
done = False

clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    circle_x += circle_speed_x
    circle_y += circle_speed_y
    if circle_y > 475:
      circle_speed_y = -100
    if circle_x > 675:
      circle_speed_x = -100
    if circle_y < 25:
      circle_speed_y = 100
    if circle_x < 25:
      circle_speed_x = 100
 
    screen.fill(BLACK)
 
    pygame.draw.circle(screen, RED, [circle_x, circle_y], circle_radius)
 
    pygame.display.flip()
 
    clock.tick(120)