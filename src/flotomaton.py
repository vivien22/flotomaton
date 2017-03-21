import io, time, os, sys, pygame
import photo_editor, storage, utils, interface

try:
    pi_camera_pres = True
    import picamera
except:
    print("WARN : no pi camera module detected !")
    pi_camera_pres = False

try:
    gphoto_pres = True
    import gphoto
except:
    gphoto_pres = False

print("gphoto_pres = " + str(gphoto_pres))

# Display warning for deprecated Picamera functions (since v1.8)
import warnings
warnings.filterwarnings('default', category=DeprecationWarning)
 
pics_taken = 0
vid_taken  = 0
 
# Init pygame
pygame.init()

# Storage init
photo_storage = storage.init('/home/pi/flotomaton/data/photos')
video_storage = storage.init('/home/pi/flotomaton/data/videos')

# Create interface
ihm = interface.init(pygame, "../images/fond.png")

# Intialize gphoto library
if gphoto_pres:
    gp          = gphoto.gphoto();
    gphoto_pres = gp.is_camera_present()

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
    
    if pi_camera_pres and not gphoto_pres:
        # image_name = '../picam_image_' + date + '.jpg'
        image_name = '../picam_image_' + utils.get_time() + '.jpg'
        camera.capture(image_name)
        image_name = photo_storage.store(image_name)

    # Take picture with gphoto
    if gphoto_pres:
        image_name = gp.capture_single_image('.')
        image_name = utils.add_date_suffix(image_name)
        image_name = photo_storage.store(image_name)

    if pi_camera_pres:
        camera.stop_preview()

    ihm.display_image(image_name, 2000)

    if pi_camera_pres:
        camera.start_preview()
        # Display selection menu
        camera.preview.alpha = 128

    return image_name


def take_pic(image_to_take):
    image_name_tab = []

    # Take picture with gphoto
    for i in range(0, image_to_take):
        # Call take_pic method to take, display picture and reset ihm
        image_name_tab.append(take_and_diplay_pic())

    return image_name_tab

def take_single_picture():
    ihm.countdown_start()
    take_pic(1)
    ihm.reset_background()

def take_photo_montage():

    ihm.countdown_start()

    image_name_tab = take_pic(4)

    image_name = '../montage_' + utils.get_time() + '.jpg'

    photo_editor.montage(image_name_tab[0],
                         image_name_tab[1],
                         image_name_tab[2],
                         image_name_tab[3],
                         image_name)

    image_name = photo_storage.store(image_name)
    ihm.display_image(image_name, 2000)
    ihm.reset_background()
 
def take_video():

    ihm.countdown_start()

    global vid_taken
    vid_taken += 1
    
    if pi_camera_pres and not gphoto_pres:
        video_name = 'video_' + utils.get_time() + '.h264'
        camera.start_recording(video_name)
        video_name = video_storage.store(video_name)
        # Recording duration / duree enregistrement (15s)
        camera.wait_recording(5)
        camera.stop_recording()

    if gphoto_pres:
        # 5 seconds video capture
        video_name = gp.capture_video('.', 5)
        video_name = video_storage.store(video_name)
 
    ihm.reset_background()

def quit_app():
    # gp.close()
    if pi_camera_pres:
        camera.close()
    if gphoto_pres:
        gp.close()

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
                take_single_picture()
            elif event.key == pygame.K_RETURN:
                take_photo_montage()
            elif event.key == pygame.K_v:
                take_video()
