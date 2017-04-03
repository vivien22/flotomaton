import logging
import os

try:
    import gphoto2 as gp
except:
    print("WARN : no gphoto module detected !")

class gphoto(object):
  
    def __init__(self):

        logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
        gp.check_result(gp.use_python_logging())
        self.context = gp.gp_context_new()
        self.camera  = gp.check_result(gp.gp_camera_new())

        try:
            gp.check_result(gp.gp_camera_init(self.camera, self.context))
            self.isCameraPresent = True
        except:
            print("WARN : fail to init gphoto camera !")
            self.isCameraPresent = False

    def close(self):
        gp.gp_camera_exit(self.camera, self.context)

    def capture_image(self):
        return gp.check_result(gp.gp_camera_capture(self.camera, 
                                                    gp.GP_CAPTURE_IMAGE, 
                                                    self.context))

    def camera_capture_video(self, video_duration):
        file_path = gp.check_result(gp.gp_camera_capture(self.camera, 
                                                         gp.GP_CAPTURE_MOVIE, 
                                                         self.context))

        # TODO : see how it goes : video_duration

        return file_path
         
    def camera_file_get_and_save(self, file_path, target):
        camera_file = gp.check_result(gp.gp_camera_file_get(self.camera, 
                                                            file_path.folder, 
                                                            file_path.name, 
                                                            gp.GP_FILE_TYPE_NORMAL, 
                                                            self.context))

        gp.check_result(gp.gp_file_save(camera_file, target))

        return camera_file

    def capture_single_image(self, dst_file_path):
        print('Capturing image')
        file_path = self.capture_image()
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join(dst_file_path, file_path.name)
        print('Copying image to', target)
        self.camera_file_get_and_save(file_path, target)

        return file_path.name

    def capture_multiple_images(self, dst_file_path, image_to_take):

        for i in range(1, image_to_take):
            print('Capturing image')
            file_path     = self.capture_image()
            image_list[i] = file_path.name
            print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
            target = os.path.join(dst_file_path, file_path.name)
            print('Copying image to', target)
            self.camera_file_get_and_save(file_path, target)

        return image_list

    def capture_video(self, dst_file_path, video_duration):
        print('Capturing video')
        file_path = self.camera_capture_video(video_duration)
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join(dst_file_path, file_path.name)
        print('Copying image to', target)
        self.camera_file_get_and_save(file_path, target)

        return file_path.name

    def is_camera_present(self):
        return self.isCameraPresent

if __name__=="__main__":
    gplib = gphoto()
    test = gplib.capture_single_image('.')
    print(test)
    gplib.close()

