import pygame, os

class init(object):
  
    def __init__(self, pygame, background_image_path, snapshot_sound_path):
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
        self.background = self.display_image(background_image_path, 0)

        # Load sounds
        self.snapshot_sound = pygame.mixer.Sound(snapshot_sound_path)

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

    def reset_background_image(self):
        # erases the entire screen surface
        self.screen.fill(self.pygame.Color("black"))
        # then diplay background
        self.screen.blit(self.background, (0,0))
        self.pygame.display.flip()

    def clear_barckground(self):
        # erases the entire screen surface
        self.screen.fill(self.pygame.Color("black"))
        self.pygame.display.flip()

    def refresh(self):
        self.pygame.display.update()    

    def display_image(self, image_path, display_time_ms):

        # Clear before display
        self.clear_barckground()

        # Load, resize & display image
        image = pygame.image.load(image_path).convert()
        image = pygame.transform.scale(image, (self.width, self.height))

        self.screen.blit(image, (0,0))
        self.pygame.display.flip()
        self.pygame.time.wait(display_time_ms)

        return image

    def display_image_and_clear(self, image_path, display_time_ms):
        image = self.display_image(image_path, display_time_ms)
        self.clear_barckground()
        return image

    def play_snapshot_sound(self):
        self.snapshot_sound.play()

    def play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        sound.play()
        return (sound.get_length()*1000)

    def play_video(self, video_path):
        # Clear before display
        self.clear_barckground()
        os.system('omxplayer -p -o hdmi ' + video_path)

def main():
    pygame.init()
    init(pygame)
  
if __name__ == "__main__":
    main()
