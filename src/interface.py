import pygame

class init(object):
  
    def __init__(self, pygame):
        self.pygame = pygame
  
        # Start fullscreen, mask mouse
        res = pygame.display.list_modes()   # return the resolution of your monitor 
        self.width, self.height = res[0]
        print("Screen resolution :", self.width, "x", self.height)
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)

        #Font 3,2,1 for countdown
        font = pygame.font.SysFont("arial", 256)
        font_colour = (127, 127, 127)
        self.text_3 = font.render("3", True, font_colour)
        self.text_2 = font.render("2", True, font_colour)
        self.text_1 = font.render("1", True, font_colour)

        # Load, resize & display background
        self.fond = pygame.image.load("images/fond.png").convert()
        self.fond = pygame.transform.scale(self.fond, (self.width, self.height))

        self.screen.blit(self.fond, (0,0))
        self.pygame.display.flip()

    def countdown_start(self):
        
        self.screen.fill(self.pygame.Color("black")) # erases the entire screen surface
        self.screen.blit(self.text_3, ((self.width - self.text_3.get_width()) // 2, (self.height - self.text_3.get_height()) // 2))
        self.pygame.display.flip()
        self.pygame.time.wait(1000)

        self.screen.fill(self.pygame.Color("black")) # erases the entire screen surface
        self.screen.blit(self.text_2, ((self.width - self.text_2.get_width()) // 2, (self.height - self.text_2.get_height()) // 2))
        self.pygame.display.flip()
        self.pygame.time.wait(1000)

        self.screen.fill(self.pygame.Color("black")) # erases the entire screen surface
        self.screen.blit(self.text_1, ((self.width - self.text_1.get_width()) // 2, (self.height - self.text_1.get_height()) // 2))
        self.pygame.display.flip()
        self.pygame.time.wait(1000)

        self.screen.fill(self.pygame.Color("black")) # erases the entire screen surface
        self.pygame.display.flip()

    def countdown_end(self):
        self.screen.blit(self.fond, (0,0))
        self.pygame.display.flip()

    def refresh(self):
        self.pygame.display.update()    

def main():
    pygame.init()
    init(pygame)
  
if __name__ == "__main__":
    main()
