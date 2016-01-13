# mpchc-py-remote
A cli-wrapper for Media Player Classic: Home Cinema's remote web interface using Python3

## Depencies
Currently the only depency is [python-requests](http://docs.python-requests.org/en/latest/user/install/), which you can install using pip or easy_install:
```
pip3 install requests
```

## Usage
There are four modes of the remote control wrapper available:
* Send one command and quit (default, called none)
* Looped input command line for inputting commands until you want to quit (text)
* Curses interface (TODO) (curses)

```
usage: mpchc.py [-h] [--ip IP] [--port PORT] [--ui UI] [--timeout TIMEOUT]
                command

positional arguments:
  command

optional arguments:
  -h, --help            show this help message and exit
  --ip IP, -c IP        Specify the IP/hostname where a MPC-HC web interface
                        is listening. Use this to override the config values.
  --port PORT, -p PORT  Specify the PORT on which MPC-HC web interface is
                        listening on. Use this to override the config values.
  --ui UI, -i UI        Choose an interface. Available options: none
                        (default)|text|curses.
  --timeout TIMEOUT, -t TIMEOUT
                        Force a non-default (3 second) timeout for the
                        request. (Use if you are running into timeout
                        exceptions a lot.)

```

