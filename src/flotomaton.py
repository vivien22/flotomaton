import io, time, os, sys, pygame, warnings
import photo_editor, storage, utils, interface

sys.path.insert(0, os.getcwd() + '/../games/pacman')
sys.path.insert(0, os.getcwd() + '/../games/pacman/layouts')
import pacman

class flotomaton(object):
  
    def __init__(self, photo_storage_path, video_storage_path):
        try:
            self.pi_camera_pres = True
            import pi_camera
        except:
            print("WARN : no pi camera library detected !")
            self.pi_camera_pres = False

        try:
            self.gphoto_pres = True
            import gphoto
        except:
            print("WARN : no gphoto library detected !")
            self.gphoto_pres = False
   
        # Display warning for deprecated Picamera functions (since v1.8)
        warnings.filterwarnings('default', category=DeprecationWarning)

        # Init pygame
        pygame.init()

        # Storage init
        self.photo_storage = storage.init(photo_storage_path)
        self.video_storage = storage.init(video_storage_path)

        # Create interface
        self.ihm = interface.init(pygame, "../images/fond.png")

        # Intialize gphoto library
        if self.gphoto_pres:
            self.gp = gphoto.gphoto();
            # gphoto lib is there but we need to check if a camera is plugged (well initialized)
            self.gphoto_pres = self.gp.is_camera_present()

        # Picamera object / objet Picamera
        if self.pi_camera_pres:
            self.pi_camera = pi_camera.camera()

        # Start camera preview / Demarre affichage en direct
        if self.pi_camera_pres:
            self.pi_camera.start()

     
    # Define functions / fonctions
    def take_and_diplay_pic(self):

        # default image displayed if not taken
        image_name = '../images/photo_test.png'
        
        if self.pi_camera_pres and not self.gphoto_pres:
            # image_name = '../picam_image_' + date + '.jpg'
            image_name = '../picam_image_' + utils.get_time() + '.jpg'
            self.pi_camera.capture_photo(image_name)
            image_name = self.photo_storage.store(image_name)

        # Take picture with gphoto
        if self.gphoto_pres:
            image_name = self.gp.capture_single_image('.')
            image_name = utils.add_date_suffix(image_name)
            image_name = self.photo_storage.store(image_name)

        if self.pi_camera_pres:
            self.pi_camera.stop()

        self.ihm.display_image(image_name, 2000)

        if self.pi_camera_pres:
            self.pi_camera.start()

        return image_name


    def take_pic(self, image_to_take):
        image_name_tab = []

        # Take picture with gphoto
        for i in range(0, image_to_take):
            # Call take_pic method to take, display picture and reset ihm
            image_name_tab.append(self.take_and_diplay_pic())

        return image_name_tab

    def take_single_picture(self):
        self.ihm.countdown_start()
        self.take_pic(1)
        self.ihm.reset_background()

    def take_photo_montage(self):

        self.ihm.countdown_start()

        image_name_tab = self.take_pic(4)

        image_name = '../montage_' + utils.get_time() + '.jpg'

        photo_editor.montage(image_name_tab[0],
                             image_name_tab[1],
                             image_name_tab[2],
                             image_name_tab[3],
                             image_name)

        image_name = self.photo_storage.store(image_name)
        self.ihm.display_image(image_name, 2000)
        self.ihm.reset_background()
     
    def take_video(self):

        self.ihm.countdown_start()
        
        if self.pi_camera_pres and not self.gphoto_pres:
            video_name = 'video_' + utils.get_time() + '.h264'
            # Recording duration (5 sec)
            self.pi_camera.capture_video(video_name, 5)
            video_name = self.video_storage.store(video_name)

        if self.gphoto_pres:
            # 5 seconds video capture
            video_name = self.gp.capture_video('.', 5)
            video_name = self.video_storage.store(video_name)
     
        self.ihm.reset_background()


    def start_pacman(self):
        if self.pi_camera_pres:
            self.pi_camera.close()
        if self.gphoto_pres:
            self.gp.close()

        pygame.quit()

        os.chdir(os.getcwd() + '/../games/pacman')
        args = pacman.readCommand( sys.argv[1:] ) # Get game components based on input
        pacman.runGames( **args )
        os.chdir(os.getcwd())
        import flotomaton

    def quit_app(self):
        if self.pi_camera_pres:
            self.pi_camera.close()
        if self.gphoto_pres:
            self.gp.close()

        pygame.quit()
        sys.exit(0)

    def main_loop(self):
        while(True):
            self.ihm.refresh()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit_app()
                    elif event.key == pygame.K_SPACE:
                        self.take_single_picture()
                    elif event.key == pygame.K_RETURN:
                        self.take_photo_montage()
                    elif event.key == pygame.K_v:
                        self.take_video()
                    elif event.key == pygame.K_g:
                        self.start_pacman()

if __name__=="__main__":
    flotomaton = flotomaton('/home/pi/flotomaton/data/photos', '/home/pi/flotomaton/data/videos')
    flotomaton.main_loop()
