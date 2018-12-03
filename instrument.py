import pygame
import os

class  Instrument():

	def  __init__(self):
		self.keys = ["1", "2", "3", "4", "5", "6", "7", "8",
					 "q", "w", "e", "r", "t", "y", "u"]
		self.notes = ["c4", "d4", "e4", "f4", "g4", "a4", "b4", "c5",
					  "d5", "e5", "f5", "g5", "a5", "b5", "c6"]

		print "loading piano notes...."
		piano_notes = self.load_instrument_notes('piano', '16_piano-med-', '.ogg')
		self.PIANO_KEY_SOUNDS = dict(zip(self.keys, piano_notes))

		print "loading trumpet notes...."
		trumpet_notes = self.load_instrument_notes('trumpet', 'Trumpet.novib.ff.', '.stereo.ogg')
		self.TRUMPET_KEY_SOUNDS = dict(zip(self.keys, trumpet_notes))

		print "loading flute notes...."
		flute_notes = self.load_instrument_notes('flute', 'Flute.nonvib.ff.', '.stereo.ogg')
		self.FLUTE_KEY_SOUNDS = dict(zip(self.keys, flute_notes))

		self.instrument_notes = {
			"p": self.PIANO_KEY_SOUNDS,
			"t": self.TRUMPET_KEY_SOUNDS,
			"f": self.FLUTE_KEY_SOUNDS
		}

		print "done loading"

	def load_instrument_notes(self, instrument, file1, fextension):
		instrument_sounds = []
		for note in self.notes:
			instrument_sounds.append(pygame.mixer.Sound(\
			 	os.path.join('sounds/'+instrument,file1+note+fextension)))
		return instrument_sounds

	def play_key_sound(self, message, recording):
		instrument = message[0]
		print message
		if len(message) == 2:
			key = message[1]
			if instrument in self.instrument_notes:
				instr = self.instrument_notes[instrument]
				if key in self.keys:
					###############################
					sound_raw = instr[key].get_raw()
					recording.writeframes(sound_raw)
					###############################
					instr[key].play()
					instr[key].fadeout(800)


