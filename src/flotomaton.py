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
def take_and_diplay_pic():

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
        # TODO : renaming
        # os.rename('/home/pi/flotomaton' + image_name, '/home/pi/flotomaton' + image_name + '_' + str(pics_taken))

    if pi_camera_pres:
        camera.stop_preview()

    ihm.display_image(image_name)    

    pygame.time.wait(2000)

    if pi_camera_pres:
        camera.start_preview()


def take_pic(image_to_take):
    ihm.countdown_start()

    # Take picture with gphoto
    for i in range(0, image_to_take):
        # Call take_pic method to take, display picture and reset ihm
        take_and_diplay_pic()

    ihm.reset_background()

 
def take_video() :

    ihm.countdown_start()

    global vid_taken
    vid_taken += 1
    
    if pi_camera_pres:
        camera.start_recording('../video_' + str(vid_taken) + '.h264')
        # Recording duration / duree enregistrement (15s)
        camera.wait_recording(5)
        camera.stop_recording()

    if gphoto_pres:
        # 5 seconds video capture
        video_name = gp.capture_video('/home/pi/flotomaton', 5)
 
    ihm.reset_background()

def quit_app():
    # gp.close()
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
                take_pic(1)
            elif event.key == pygame.K_RETURN:
                take_pic(4)
            elif event.key == pygame.K_v:
                take_video()

