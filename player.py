#!/usr/bin/env python

import pygame
import os
import sys
from instrument import Instrument



pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 4096) # setup mixer to avoid sound lag

piano = Instrument()


def run():
	while 1:
		events = pygame.event.get()
		for event in events:
		    if event.type == pygame.KEYDOWN:
		    	if event.key == pygame.K_RETURN:
		    		sys.exit(0)
		    	else:
		    		send_key(event.key)
		    		piano.play_key_sound(event.key)


def send_key(num):
	print "send note: "+ str(num)
	





if __name__ == '__main__':
   	run()