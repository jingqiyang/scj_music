import pygame
import os
from get_key import get_key

class  Instrument():

	def  __init__(self):
		self.keys = ["1", "2", "3", "4", "5", "6", "7", "8"]
		self.notes = ["c4", "d4", "e4", "f4", "g4", "a4", "b4", "c5"]

		print "loading piano notes...."
		self.PIANO_KEY_SOUNDS = dict(zip(self.keys, self.load_piano_notes()))

		print "loading trumpet notes...."
		self.TRUMPET_KEY_SOUNDS = dict(zip(self.keys, self.load_trumpet_notes()))

		print "loading flute notes...."
		self.FLUTE_KEY_SOUNDS = dict(zip(self.keys, self.load_flute_notes()))

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

		self.instrument_notes = {
			"p": self.PIANO_KEY_SOUNDS,
			"t": self.TRUMPET_KEY_SOUNDS,
			"f": self.FLUTE_KEY_SOUNDS
		}

		print "done loading"

	def load_instrument_notes(self, path, file1, fextension):
		instrument_sounds = []
		for note in self.notes:
			instrument_sounds.append(pygame.mixer.Sound(\
			 	os.path.join('sounds/'+instrument,file1+note+fextension)))
		return instrument_sounds

	def load_piano_notes(self):
		piano_sounds = []
		for note in self.notes:
			 piano_sounds.append(pygame.mixer.Sound(\
			 	os.path.join('sounds/piano','16_piano-med-'+note+'.ogg')))
		return piano_sounds

	def load_trumpet_notes(self):
		trumpet_sounds = []
		for note in self.notes:
			trumpet_sounds.append(pygame.mixer.Sound(\
				 	os.path.join('sounds/trumpet','Trumpet.novib.ff.'+note+'.stereo.ogg')))
		return trumpet_sounds

	def load_flute_notes(self):
		flute_sounds = []
		for note in self.notes:
			flute_sounds.append(pygame.mixer.Sound(\
				 	os.path.join('sounds/flute','Flute.nonvib.ff.'+note+'.stereo.ogg')))
		return flute_sounds

	def play_key_sound(self, message, recording):
		instrument = message[0]
		if len(message) == 2:
			key = get_key(message[1])
			if instrument in self.instrument_notes:
				instr = self.instrument_notes[instrument]
				if key in self.pygame_string:
					key = self.pygame_string[key]
					###############################
					sound_raw = instr[key].get_raw()
					recording.writeframes(sound_raw)
					###############################
					instr[key].play()
					instr[key].fadeout(800)


