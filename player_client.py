#!/usr/bin/env python

"""
client for scj_music:
Allows individual users to join a music server and play along with
other users. 

run with: python player_client.py [host] [port] [p | t | f] username
for example: python player_client.py 127.0.0.1 65432 p Sam
"""

import pygame
import os
import sys
from instrument import Instrument

import socket
import threading

import wave
import datetime

#initialize pygame and the pygame mixer
pygame.mixer.pre_init(44100, -16, 8, 1024) # setup mixer to avoid sound lag
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((100, 500), 0, 32)

instrument = Instrument()

def main():
    """run client loop."""

    #receive command line arguments and use to connect to the server
    host, port, instrument, username = get_args()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    try:
        server.connect((host, port))
    except:
        print "Could not connect to the server."
        sys.exit(1)

    #setting up recording
    now = datetime.datetime.now()
    filename = username + "_" + instrument + "_" + str(now.year) +"_" + \
                str(now.month) + "_" + str(now.day) + "___" + str(now.hour) \
                + "_" + str(now.minute) + "_" + str(now.second) + ".wav"
    recording = wave.open(filename, 'w')
    recording.setframerate(44100)
    recording.setnchannels(2)
    recording.setsampwidth(2)
    
    #begin threads for client to receive sounds
    thread = threading.Thread(target = receive_keys, 
                              args = [server, recording])
    thread.daemon = True
    thread.start()

    while True:
        #the loop for a client to send sounds. Uses pygame to get keypress
        #events and sends the strings representing those keys to the server
        #for broadcasting
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
    """
    get host ip, port, client instrument, 
    and username from command line args.
    """
    if len(sys.argv) != 5:
        print "Correct usage: script, IP address, port number, " + \
              "instrument (piano (p), trumpet (t), or flute (f)), username"
        exit() 
      
    return (str(sys.argv[1]), int(sys.argv[2]), 
            str(sys.argv[3]), str(sys.argv[4]))


def send_key(note):
    """prints the key of the note being played to the client playing it"""
    print "playing note: "+ str(note)


def receive_keys(server, recording):
    """
    receive messages as string, call play_key_sound to play the received
    sound
    """

    while True:
        received_msg = server.recv(2)
        if len(received_msg) == 2:
            key = received_msg[1]
        if key != None:
            send_key(key)
            instrument.play_key_sound(received_msg, recording)


if __name__ == '__main__':
    main()
