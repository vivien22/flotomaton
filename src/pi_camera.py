import os

try:
    import picamera
except:
    print("WARN : no pi camera module detected !")

class camera(object):
  
    def __init__(self):
        self.camera           = picamera.PiCamera()
        self.camera.framerate = float(24)
        self.camera.hflip     = False
        self.camera.vflip     = True

    def capture_photo(self, image_name):
        self.camera.capture(image_name)

    def capture_video(self, video_name, duration):
        # os.system('raspivid -o ' + str(video_name) +  ' -t ' + str(duration))
        self.camera.start_recording(video_name, format='mjpeg')
        self.camera.wait_recording(duration/1000)
        self.camera.stop_recording()

    def start(self):
        self.camera.start_preview()
        self.set_transparancy(0)

    def stop(self):
        self.camera.stop_preview()

    def set_transparancy(self, alpha):
        # Set transparency
        self.camera.preview.alpha = alpha

    def close(self):
        self.camera.close()
