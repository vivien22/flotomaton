import os

try:
    import picamera
except:
    print("WARN : no pi camera module detected !")

class camera(object):
  
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.framerate = float(24)
        self.camera.hflip = True

    def capture_photo(self, image_name):
        self.camera.capture(image_name)

    def capture_video(self, video_name, duration):
        # os.system('raspivid -o ' + str(video_name) +  ' -t ' + str(duration))
        self.camera.start_recording(video_name)
        self.camera.wait_recording(duration/1000)
        self.camera.stop_recording()

    def start(self):
        self.camera.start_preview()
        # Set transparency
        self.camera.preview.alpha = 128

    def stop(self):
        self.camera.stop_preview()

    def close(self):
        self.camera.close()
