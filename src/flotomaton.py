import io, time, os, sys, pygame, warnings, subprocess, multiprocessing
import photo_editor, storage, utils, interface, gpio, dubsmash, capture

class flotomaton(object):
  
    def __init__(self, photo_storage_path, video_storage_path):
        try:
            self.pi_camera_pres = True
            import pi_camera
        except:
            print("WARN : no pi camera library detected !")
            self.pi_camera_pres = False

        try:
            self.gphoto_lib_pres = True
            import gphoto
        except:
            print("WARN : no gphoto library detected !")
            self.gphoto_lib_pres = False

        # Display warning for deprecated Picamera functions (since v1.8)
        warnings.filterwarnings('default', category=DeprecationWarning)

        # Init pygame
        pygame.init()

        # GPIO
        self.gpio = gpio.init(self.gpio_callback_func)

        # Storage init
        self.photo_storage = storage.init(photo_storage_path)
        self.video_storage = storage.init(video_storage_path)

        # Intialize gphoto library
        if self.gphoto_lib_pres:
            self.gp = gphoto.gphoto();

        # Picamera object / objet Picamera
        if self.pi_camera_pres:
            self.pi_camera = pi_camera.camera()

        # Start camera preview / Demarre affichage en direct
        if self.pi_camera_pres:
            self.pi_camera.start()

        # Create interface
        self.ihm = interface.init(pygame, self.pi_camera, "../images/fond.png", "../sounds/snapshot.wav")

        self.capture = capture.init(self.photo_storage, self.video_storage, self.pi_camera)

        # Initialize dubsmash
        self.dubsmash = dubsmash.init(pygame, self.ihm, self.pi_camera, self.capture)

        # Internal flag
        self.led_garland_process_started = False
        self.protect_gpio_double_press   = False

    # Define functions / fonctions
    def take_and_diplay_pic(self, display):

        # Play snapshot sound
        self.ihm.play_snapshot_sound()

        # default image displayed if not taken
        image_name = '../images/photo_test.png'
        
        if self.pi_camera_pres and not self.gp.is_camera_present():
            # image_name = '../picam_image_' + date + '.jpg'
            image_name = '../picam_image_' + utils.get_time() + '.jpg'
            self.pi_camera.capture_photo(image_name)
            image_name = self.photo_storage.store(image_name)

        # Take picture with gphoto
        if self.gp.is_camera_present():
            image_name = self.gp.capture_single_image('.')
            image_name = utils.rename_with_time_suffix(image_name)
            image_name = self.photo_storage.store(image_name)

        if display == True:
            if self.pi_camera_pres:
                self.pi_camera.stop()

            self.ihm.display_image_and_clear(image_name, 2000)

            if self.pi_camera_pres:
                self.pi_camera.start()

        return image_name


    def take_pic(self, image_to_take, waiting_time_between_pic, display):
        image_name_tab = []

        # Take picture with gphoto
        for i in range(0, image_to_take):
            # Call take_pic method to take, display picture and reset ihm
            self.ihm.countdown_start()
            image_name_tab.append(self.take_and_diplay_pic(display))
            if image_to_take > 1:
                pygame.time.wait(waiting_time_between_pic)

        return image_name_tab

    def take_single_picture(self):
        self.take_pic(1, 0, True)
        self.ihm.reset_background_image()

    def take_photo_montage(self):

        image_name_tab = self.take_pic(4, 1000, False)

        if self.pi_camera_pres:
            self.pi_camera.stop()

        self.ihm.display_image('../images/attente.png', 0)

        image_name = '../montage_' + utils.get_time() + '.jpg'

        photo_editor.montage(image_name_tab[0],
                             image_name_tab[1],
                             image_name_tab[2],
                             image_name_tab[3],
                             image_name)

        image_name = self.photo_storage.store(image_name)

        self.ihm.display_image_and_clear(image_name, 10000)

        if self.pi_camera_pres:
            self.pi_camera.start()

        self.ihm.reset_background_image()
     
    def take_video(self):

        self.ihm.countdown_start()
        
        if self.pi_camera_pres:
            video_name = self.capture.capture_video(5000)
            self.pi_camera.stop()
            # Replay video 
            self.ihm.play_video(video_name)
            self.pi_camera.start()

        self.ihm.reset_background_image()

    def start_dubsmash(self):
        self.ihm.countdown_start()
        self.dubsmash.start()
        self.ihm.reset_background_image()

    def quit_app(self):
        if self.pi_camera_pres:
            self.pi_camera.close()
        if self.gphoto_lib_pres:
            self.gp.close()

        pygame.quit()
        sys.exit(0)
    
    def gpio_callback_func(self, pin):
        if (pin == gpio.button_1) or (pin == gpio.button_2) or (pin == gpio.button_3) or (pin == gpio.button_4):
            if self.protect_gpio_double_press == False:
                self.protect_gpio_double_press = True
                ev = pygame.event.Event(pygame.USEREVENT, {'pin': pin})
                pygame.event.post(ev)
                print("button event " + str(pin))
        else:
            print("unhandled gpio event")

    # def start_led_garland_process(self):
    #     print('Start led_garland_process')
    #     self.led_garland_process_started = True
    #     self.led_garland_process = multiprocessing.Process(name='led_garland', target=self.gpio.led_process)
    #     self.led_garland_process.start()

    # def terminate_led_garland_process(self):
    #     if self.led_garland_process_started:
    #         print('Terminate led_garland_process')
    #         self.led_garland_process.terminate()
    #         self.led_garland_process_started = False

    def main_loop(self):

        while(True):
        
            # if self.led_garland_process_started == False:
            #     # Start garland process
            #     self.start_led_garland_process()

            # Sleep 1/24 ms (framerate) to avoid 100% CPU load
            time.sleep(1/24)
            self.ihm.refresh()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # self.terminate_led_garland_process()
                        self.quit_app()
                    elif event.key == pygame.K_SPACE:
                        # self.terminate_led_garland_process()
                        self.gpio.clear_and_blink_selection(event.pin)
                        self.take_single_picture()
                    elif event.key == pygame.K_RETURN:
                        # self.terminate_led_garland_process()
                        self.gpio.clear_and_blink_selection(event.pin)
                        self.take_photo_montage()
                    elif event.key == pygame.K_v:
                        # self.terminate_led_garland_process()
                        self.gpio.clear_and_blink_selection(event.pin)
                        self.take_video()
                    elif event.key == pygame.K_d:
                        # self.terminate_led_garland_process()
                        self.gpio.clear_and_blink_selection(event.pin)
                        self.start_dubsmash()

                elif event.type == pygame.USEREVENT:
                    print('GPIO ' + str(event.pin) + ' pressed')
                    # self.terminate_led_garland_process()
                    self.gpio.clear_and_blink_selection(event.pin)

                    if   event.pin == gpio.button_1:
                        self.take_single_picture()
                    elif event.pin == gpio.button_2:
                        self.take_photo_montage()
                    elif event.pin == gpio.button_3:
                        self.take_video()
                    elif event.pin == gpio.button_4:
                        self.start_dubsmash()

                    self.protect_gpio_double_press = False

if __name__=="__main__":
    flotomaton = flotomaton('/home/pi/flotomaton/data/photos', '/home/pi/flotomaton/data/videos')
    flotomaton.main_loop()
