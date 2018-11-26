"""
commands to run:
    erl -env ERL_LIBS modules/erlport
    {ok, Pid} = python:start([{python_path, "."}]).
    python:call(Pid, python_test, test, []).

    ...

    python:stop(Pid).

* "modules/erlport" should be replaced with path to erlport folder
* "." should be replaced with path to python files

notes:
* to call erlang module functions from python functions, you need to
compile the erlang module and call the python function from erlang shell
* the files must either directly be placed inside erlport folder, or
the erlport folder must be inside an enclosing folder. in this case,
i just named the enclosing folder "modules". this is because there's
some issue with the path to the folder being just the folder itself
and also being named "erlport" i think
* edits to python file will not appear after python:call is called
* if python function is void, it will return the atom 'undefined' to
the erlang shell
* python file doesn't need a main, all functions in file are considered
part of the module
"""

from erlport.erlterms import Atom
from erlport.erlang import call
import pygame
import os
import sys
from instrument import Instrument

def main():
    print erlang_call()

def test():
    name = sys.stdin.read()
    sys.stdout.write("Hello, " + name)
    return "ok"

def printing():
    sys.stdout.write("alskdfj")
    return "ok"

def erlang_call():
    return call(Atom("erlport_test"), Atom("test"), [])


def run():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 4096) # setup mixer to avoid sound lag

    piano = Instrument()
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
    main()
