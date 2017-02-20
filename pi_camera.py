# http://www.projetsdiy.fr/picamera-version-1-9-piloter-en-python-la-camera-du-raspberry-pi/#.WKsablXhAdU

import io, time, os, sys, picamera, pygame
 
# Display warning for deprecated Picamera functions (since v1.8) / affiche alerte si une fonction depreciee est utilisee 
import warnings
warnings.filterwarnings('default', category=DeprecationWarning)
 
pics_taken = 0
vid_taken = 0
 
# Init pygame and screen / initialise pygame et ecran
pygame.init()
res = pygame.display.list_modes() # return the resolution of your monitor / resolution du moniteur
width, height = res[0] # In case of trouble, set manually the resolution with: width, height = 1650, 1050
print "Screen resolution :", width, "x", height
screen = pygame.display.set_mode([width, height])
pygame.display.toggle_fullscreen()
pygame.mouse.set_visible = False
 
# Picamera object / objet Picamera
camera = picamera.PiCamera()
#camera.resolution = (1280, 720)
camera.framerate = float(24)
 
# Define functions / fonctions
def take_pic():
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
 
#Start camera preview / Demarre affichage en direct
camera.start_preview()
 
while(True):
  pygame.display.update()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit_app()
        elif event.key == pygame.K_SPACE:
          take_pic()
        elif event.key == pygame.K_RETURN:
          take_video()
        elif event.key == pygame.K_TAB:
           camera.start_preview()
