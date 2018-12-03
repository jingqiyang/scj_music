SCJ_MUSIC (name TBD)
=======
Have you ever had the urge to jam out with some friends, but you don’t have an instrument? Or maybe your bandmates are out of town and you can’t all get together? Our ‘concurrent garage band’ will allow people to have a jam session anytime, anywhere (as long as they can connect to the internet), with the options of playing
the piano, trumpet or flute.


## Installation

**Requirements:**

Pygame 

Python 2.7

For optimal play, PC is recommended.

## How to Use

**Start Server**
* `python music_server.py [host] [port]`
    * host = IP address
    * port = port number must be greater than or equal to 1024

**Join as Client**
* `python player_client.py [host] [port] [p | t | f]`
    * host = IP address where server is hosted
    * port = port number where server is running
    * [p | t | f]
        * p = piano
        * t = trumpet
        * f = flute

**Playing**
* Type using QWERTY keyboard
* 2 octaves currently available:
    * C4 - C5 = keys 1 - 8
    * D5 - C6 = keys Q - U

**Acknowledgements**





