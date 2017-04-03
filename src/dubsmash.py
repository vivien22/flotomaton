import pygame, interface, picamera

class init(object):
  
    def __init__(self, pygame, interface, picamera):
        self.pygame    = pygame
        self.ihm       = interface
        self.pi_camera = picamera

    def start(self):
        # Sound test
        self.ihm.play_snapshot_sound()
        # Capture video
        self.pi_camera.capture_video('../dubsmash_test_video.h264', 5000)

        # TODO : montage video
        # TODO : replay video
