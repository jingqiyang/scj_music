-module(erlport_test).
-export([python_call/0, test/0]).

python_call() ->
    {ok, Pid} = python:start([{python_path, "."}]),
    Result = python:call(Pid, python_test, test, []),
    Result.

test() ->
    "hello world! inside erlang function".
