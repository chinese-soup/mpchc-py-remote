# mpchc-py-remote
A cli-wrapper for Media Player Classic: Home Cinema's remote web interface using Python

## Usage
There are four modes of the remote control wrapper available:
* Send one command and quit (default, called none)
* Looped input command line for inputting commands until you want to quit (text)
* Instantly sent input command line using curses (no need to press the Enter key like with the mode above) (curses-line) (TODO)
* Curses interface (TODO) (curses)

```
usage: mpchc.py [-h] [--ip IP] [--ui UI] [--timeout TIMEOUT] command

positional arguments:
  command

optional arguments:
  -h, --help         show this help message and exit
  --ip IP            Base IP:PORT where a MPC-HC web interface is listening
  --ui UI            Available options: none (default)|text|curses-line|curses
  --timeout TIMEOUT  Force a non-default (3 second) timeout for the request.
                     (Use if you are running into timeout exceptions a lot.)
```

