"""
commands to run:
    erl -env ERL_LIBS modules/erlport
    {ok, Pid} = python:start([{python_path, "."}]).
    python:call(Pid, python_test, function_name, []).

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

# from erlport.erlterms import Atom
# from erlport.erlang import call
import sys

def main():
    print erlang_call()

def test():
    while (True):
        print "loop"
    return "ok"

def erlang_call():
    return call(Atom("erlport_test"), Atom("test"), [])

if __name__ == '__main__':
    main()
