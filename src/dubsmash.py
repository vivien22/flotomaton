import pygame, interface, picamera, capture

class init(object):
  
    def __init__(self, pygame, interface, picamera, capture):
        self.pygame    = pygame
        self.ihm       = interface
        self.pi_camera = picamera
        self.capture   = capture

    def start(self):
        # Sound test
        self.ihm.play_snapshot_sound()
        # Capture video
        video_name = self.capture.capture_video(5000)

        # TODO : montage video
        # TODO : replay video
