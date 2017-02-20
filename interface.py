import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

pygame.init()

# Open pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#Load & display background
fond = pygame.image.load("fond.png").convert()
pygame.display.flip()

#Font 3,2,1
font = pygame.font.SysFont("arial", 72)
text_3 = font.render("3", True, (0, 0, 0))
text_2 = font.render("2", True, (0, 0, 0))
text_1 = font.render("1", True, (0, 0, 0))

#Refresh display
pygame.display.flip()

while 1:

    window.blit(fond, (0,0))
    window.blit(text_3, ((WINDOW_WIDTH - text_3.get_width()) // 2, (WINDOW_HEIGHT - text_3.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    window.blit(fond, (0,0))
    window.blit(text_2, ((WINDOW_WIDTH - text_2.get_width()) // 2, (WINDOW_HEIGHT - text_2.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    window.blit(fond, (0,0))
    window.blit(text_1, ((WINDOW_WIDTH - text_1.get_width()) // 2, (WINDOW_HEIGHT - text_1.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)
