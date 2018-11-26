import pygame
import os

class  Instrument():

	def  __init__(self):
		keys = ["1", "2", "3", "4", "5", "6", "7", "8"]
		notes = ["c4", "d4", "e4", "f4", "g4", "a4", "b4", "c5"]
		note_sounds = []
		for note in notes:
			 note_sounds.append(pygame.mixer.Sound(\
			 	os.path.join('piano_sounds','16_piano-med-'+note+'.ogg')))
		self.KEY_SOUNDS = dict(zip(keys, note_sounds))

		self.pygame_string = {
			pygame.K_1: "1",
			pygame.K_2: "2",
			pygame.K_3: "3",
			pygame.K_4: "4",
			pygame.K_5: "5",
			pygame.K_6: "6",
			pygame.K_7: "7",
			pygame.K_8: "8",
		}

	def play_key_sound(self, key):
		if key in self.pygame_string:
			key = self.pygame_string[key]
			self.KEY_SOUNDS[key].play()
			self.KEY_SOUNDS[key].fadeout(1000)