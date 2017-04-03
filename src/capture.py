import storage, utils, pi_camera

class init(object):
  
    def __init__(self, photo_storage, video_storage, pi_camera):
        self.photo_storage = photo_storage
        self.video_storage = video_storage
        self.pi_camera     = pi_camera

    def capture_video(self, duration):
        video_name = 'video_' + utils.get_time() + '.h264'
        # Recording duration (ms)
        self.pi_camera.capture_video(video_name, duration)
        video_name = self.video_storage.store(video_name)
        
        return video_name     
