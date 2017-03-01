import pygame

pygame.init()

# Get resolution
infoObject    = pygame.display.Info()
WINDOW_WIDTH  = infoObject.current_w
WINDOW_HEIGHT = infoObject.current_h

# Open pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

# Load, resize & display background
fond = pygame.image.load("fond.png").convert()
fond = pygame.transform.scale(fond, (WINDOW_WIDTH, WINDOW_HEIGHT))
window.blit(fond, (0,0))
pygame.display.flip()

# White background
white = [255, 255, 255]
#Font 3,2,1
font = pygame.font.SysFont("arial", 72)
text_3 = font.render("3", True, (0, 0, 0))
text_2 = font.render("2", True, (0, 0, 0))
text_1 = font.render("1", True, (0, 0, 0))

#Refresh display
pygame.display.flip()

while 1:

    window.blit(fond, (0,0))
    pygame.display.flip()
    pygame.time.wait(1000)

    window.fill(white)
    window.blit(text_3, ((WINDOW_WIDTH - text_3.get_width()) // 2, (WINDOW_HEIGHT - text_3.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    window.fill(white)
    window.blit(text_2, ((WINDOW_WIDTH - text_2.get_width()) // 2, (WINDOW_HEIGHT - text_2.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    window.fill(white)
    window.blit(text_1, ((WINDOW_WIDTH - text_1.get_width()) // 2, (WINDOW_HEIGHT - text_1.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            raise SystemExit
