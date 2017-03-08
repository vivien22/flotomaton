import io, time, os, sys, picamera, pygame
 
# Display warning for deprecated Picamera functions (since v1.8) / affiche alerte si une fonction depreciee est utilisee 
import warnings
warnings.filterwarnings('default', category=DeprecationWarning)
 
pics_taken = 0
vid_taken = 0
 
# Init pygame and screen / initialise pygame et ecran
pygame.init()
res = pygame.display.list_modes()   # return the resolution of your monitor 
width, height = res[0]              # In case of trouble, set manually the resolution with: width, height = 1650, 1050
print "Screen resolution :", width, "x", height
screen = pygame.display.set_mode([width, height])
pygame.display.toggle_fullscreen()
pygame.mouse.set_visible = False

#Font 3,2,1 for countdown
font = pygame.font.SysFont("arial", 256)
font_colour = (127, 127, 127)
text_3 = font.render("3", True, font_colour)
text_2 = font.render("2", True, font_colour)
text_1 = font.render("1", True, font_colour)

# Load, resize & display background
fond = pygame.image.load("fond.png").convert()
fond = pygame.transform.scale(fond, (width, height))
 
# Picamera object / objet Picamera
camera = picamera.PiCamera()
camera.framerate = float(24)
 
# Define functions / fonctions
def take_pic():
    
    screen.fill(pygame.Color("black")) # erases the entire screen surface
    screen.blit(text_2, ((width - text_2.get_width()) // 2, (height - text_2.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill(pygame.Color("black")) # erases the entire screen surface
    screen.blit(text_1, ((width - text_1.get_width()) // 2, (height - text_1.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill(pygame.Color("black")) # erases the entire screen surface
    pygame.display.flip()
    
    global pics_taken
    pics_taken += 1
    camera.capture('image_' + str(pics_taken) + '.jpg')
 
def take_video() :
    global vid_taken
    vid_taken += 1
    camera.start_recording('video_' + str(vid_taken) + '.h264')
    #Recording duration / duree enregistrement (15s)
    camera.wait_recording(15)
    camera.stop_recording()
 
def quit_app():
    camera.close()
    pygame.quit()
    print "You've taken", pics_taken, " pictures ", vid_taken, " videos. Don't forget to back them up (or they'll be overwritten next time)"
    sys.exit(0)
 
# Start camera preview / Demarre affichage en direct
camera.start_preview()

# Display selection menu
camera.preview.alpha = 128
screen.blit(fond, (0,0))
pygame.display.flip()

while(True):
  pygame.display.update()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit_app()
        elif event.key == pygame.K_SPACE:
          take_pic()
        elif event.key == pygame.K_TAB:
           camera.start_preview()
