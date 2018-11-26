#!/usr/bin/env python

"""
# run with ./music_server.py [host] [port]
for example: ./music_server.py 127.0.0.1 65432

notes:
* don't know how to kill server + kill client threads
* server prints out notes sent from any client to terminal
"""

import socket
import threading
import sys

clients = []

def main():
    """run server."""
    host, port = get_args()
    global clients

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((host, port))
    server.listen(20)  # 20 is max connections

    while True:
        # accept a connection request and stores two parameters  
        # conn is a socket object for that user
        # addr contains the IP of the client at addr[0]
        conn, addr = server.accept()

        clients.append(conn)    # add to list of clients

        print addr[0] + " connected"

        # start client thread
        thread = threading.Thread(target = start_client, args = [conn, addr])
        thread.start()

    conn.close()
    server.close()


def get_args():
    """get host ip and port from command line args."""
    if len(sys.argv) != 3:
        print "Correct usage: script, IP address, port number"
        exit() 
      
    return (str(sys.argv[1]), int(sys.argv[2]))


def start_client(conn, addr):
    """client receive/send messages loop."""
    global clients

    while True:
        try:
            # 2048 is buffer size (should be small power of 2)
            message = conn.recv(2048)

            # print msg on server terminal, then send to all clients
            if message:
                print message
                broadcast(message, conn) 
            else:
                clients.remove(conn)    # connection is broken

        except: 
            continue


def broadcast(message, conn):
    """send message to all clients."""
    global clients
    for client in clients:
        try: 
            client.send(message)
        except: 
            client.close()
            client.remove(conn)    # connection is broken


if __name__ == '__main__':
    main()
