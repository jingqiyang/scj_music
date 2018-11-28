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
from instrument import Instrument

import socket
import threading

from get_key import get_key

pygame.mixer.pre_init(44100, -16, 2, 1024) # setup mixer to avoid sound lag
pygame.mixer.init()
pygame.init()

piano = Instrument()

def main():
    """run client loop."""
    host, port = get_args()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    server.connect((host, port))

    thread = threading.Thread(target = receive_keys, args = [server])
    thread.daemon = True
    thread.start()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sys.exit(0)
                else:
                    # convert to string
                    server.send(pygame.key.name(event.key))


def get_args():
    """get host ip and port from command line args."""
    if len(sys.argv) != 3:
        print "Correct usage: script, IP address, port number"
        exit() 
      
    return (str(sys.argv[1]), int(sys.argv[2]))


def send_key(num):
    print "send note: "+ str(num)


def receive_keys(server):
    """receive messages as string, convert back to pygame key."""
    while True:
        received_key = get_key(server.recv(1))
        if received_key != None:
            send_key(received_key)
            piano.play_key_sound(received_key)


if __name__ == '__main__':
    main()
