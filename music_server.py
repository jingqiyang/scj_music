#!/usr/bin/env python

"""
server for scj_music
run with: python music_server.py [host] [port]
for example: python music_server.py 127.0.0.1 65432
port number should be greater than or equal to 1024
"""

import socket
import threading
import sys

clients = []

def main():
    """
    get ip and port, start server, run loop that adds new connections
    to list of clients, and starts thread for each client.
    each thread receives messages and broadcasts to all clients.
    """
    host, port = get_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(20)  # 20 is max connections

    print "Server running at host " + host + " and port " + str(port)

    while True:
        conn, addr = server.accept()

        clients.append(conn)    # add to list of clients

        # start client thread
        thread = threading.Thread(target = start_client, args = [conn, addr])
        thread.daemon = True
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
    """
    function run by client thread for receive/send messages loop.
    for each message received from client, broadcast to all clients
    in server.
    """
    while True:
        try:
            # buffer size is 2 for 2 character message (instrument + key)
            message = conn.recv(2)
            broadcast(message)
        except: 
            continue


def broadcast(message):
    """
    send message to all clients. if a client cannot get a message,
    remove client from server.
    """
    for client in clients:
        try: 
            client.send(message)
        except: 
            client.close()
            clients.remove(client)    # connection is broken


if __name__ == '__main__':
    main()
