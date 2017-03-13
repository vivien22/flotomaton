import io, time, os, sys, pygame, interface

try:
    pi_camera_pres = True
    import picamera
except:
    print("WARN : no pi camera module detected !")
    pi_camera_pres = False

#try:
#    gphoto_pres = True
#    import gphoto
#except:
#    print("WARN : gphoto module detected !")
#    gphoto_pres = False
gphoto_pres = False

# Display warning for deprecated Picamera functions (since v1.8)
import warnings
warnings.filterwarnings('default', category=DeprecationWarning)
 
pics_taken = 0
vid_taken  = 0
 
# Init pygame
pygame.init()

# Create interface
ihm = interface.init(pygame, "../images/fond.png")

# Intialize gphoto library
if gphoto_pres:
    gp  = gphoto.gphoto();

# Picamera object / objet Picamera
if pi_camera_pres:
    camera = picamera.PiCamera()
    camera.framerate = float(24)
 
# Define functions / fonctions
def take_pic():
    
    ihm.countdown_start()
    
    global pics_taken
    pics_taken += 1

    # default image displayed if not taken
    image_name = '../images/photo_test.png'
    
    if pi_camera_pres:
        image_name = '../image_' + str(pics_taken) + '.jpg'
        camera.capture(image_name)

    # Take picture with gphoto
    if gphoto_pres:
        image_name = gp.capture_single_image('/home/pi/flotomaton')

    if pi_camera_pres:
        camera.stop_preview()

    ihm.display_image(image_name)    

    pygame.time.wait(2000)

    ihm.reset_background()

    if pi_camera_pres:
        camera.start_preview()

 
def take_video() :
    global vid_taken
    vid_taken += 1
    
    if pi_camera_pres:
        camera.start_recording('video_' + str(vid_taken) + '.h264')
        # Recording duration / duree enregistrement (15s)
        camera.wait_recording(15)
        camera.stop_recording()
 
def quit_app():
    if pi_camera_pres:
        camera.close()
    pygame.quit()
    print("You've taken", pics_taken, " pictures ", vid_taken, " videos. Don't forget to back them up (or they'll be overwritten next time)")
    sys.exit(0)
 
# Start camera preview / Demarre affichage en direct
if pi_camera_pres:
    camera.start_preview()
    # Display selection menu
    camera.preview.alpha = 128

while(True):
    
    ihm.refresh()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_app()
            elif event.key == pygame.K_SPACE:
                take_pic()
