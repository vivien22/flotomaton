import pygame, interface, picamera, capture, random

class init(object):
  
    def __init__(self, pygame, interface, picamera, capture):
        self.pygame    = pygame
        self.ihm       = interface
        self.pi_camera = picamera
        self.capture   = capture

        # Load list of sounds for dubsmash
        self.dubsmash_sound_list = []
        self.dubsmash_sound_list.append('../sounds/dubsmash/There-Has-Been-An-Awakening.wav')
        self.dubsmash_sound_list_size = len(self.dubsmash_sound_list)

    def start(self):

        random_dubsmash_sound = random.randint(0, self.dubsmash_sound_list_size-1)

        print('Play ' + self.dubsmash_sound_list[random_dubsmash_sound] + ' dubsmash sound')

        # Sound test
        duration = self.ihm.play_sound(self.dubsmash_sound_list[random_dubsmash_sound])

        # Capture video
        video_name = self.capture.capture_video(duration)

        # Replay video with sound
        self.pi_camera.stop()
        self.ihm.play_sound(self.dubsmash_sound_list[random_dubsmash_sound])
        self.ihm.play_video(video_name)
        self.pi_camera.start()
