#!/usr/bin/env python

"""
# run with ./player_client.py [host] [port]
for example: ./player_client.py 127.0.0.1 65432

problems:
* finicky with key presses
* EXTREMELY laggy
* doesn't kill receive thread
"""

import pygame
import os
import sys
from instrument2 import Instrument

import socket
import threading

#################
import wave
import datetime
#################

pygame.mixer.pre_init(44100, -16, 2, 1024) # setup mixer to avoid sound lag
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((100, 500), 0, 32)

instrument = Instrument()

def main():
    """run client loop."""
    host, port, instrument, username = get_args()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    server.connect((host, port))

    ##################
    now = datetime.datetime.now()
    filename = username + "_" + instrument + "_" + str(now.year) +"_" + str(now.month) + "_" + str(now.day) + "___" + str(now.hour) +"_" + str(now.minute) + "_" + str(now.second) + ".wav"
    recording = wave.open(filename, 'w')
    recording.setframerate(44100)
    recording.setnchannels(2)
    recording.setsampwidth(2)
    ##################


    thread = threading.Thread(target = receive_keys, args = [server, recording])
    thread.daemon = True
    thread.start()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    recording.close()
                    sys.exit(0)
                else:
                    # convert to string
                    server.send(instrument+pygame.key.name(event.key))


def get_args():
    """get host ip and port from command line args."""
    if len(sys.argv) != 5:
        print "Correct usage: script, IP address, port number, instrument (piano (p), trumpet (t), or flute (f)), username"
        exit() 
      
    return (str(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))


def send_key(num):
    print "send note: "+ str(num)


def receive_keys(server, recording):
    """receive messages as string, convert back to pygame key."""
    while True:
        received_msg = server.recv(2)
        if len(received_msg) == 2:
            key = received_msg[1]
        if key != None:
            send_key(key)
            instrument.play_key_sound(received_msg, recording)


if __name__ == '__main__':
    main()
