#!/usr/bin/python3
# coding=utf-8
import sys, os, requests, argparse, json

# p = play
# n = next (ch)
# b = previous (ch)
# f = toggle fullscreen
# jf = small jump forwards
# jb = small jump backwards

cmds = {"p": 889, "n": 922, "b": 921, "f": 830, "jf": 900, "jb": 899, "s": 890, "+": 907, "-": 908, "m": 909} # todo: parse from a config 
cmds_t = {"p": "Play/Pause", "n": "Next (Chapter/File)", "b": "Prev (Chapter/File)", "f": "Toggle fullscreen", "jf": "Small forward jump", "jb": "Small backward jump", "s": "Stop", "+": "Volume up", "-": "Volume down", "m": "Volume mute (toggle)"}

def main(command, base_ip):
	cmd = command  # temporary
	rcmd = cmds[cmd]
	rcmd_t = cmds_t[cmd]
	rdata = {"wm_command": rcmd}
	
	print("Requested: {0}".format(rcmd_t))

	try:
		r = requests.post("http://{0}/command.html".format(base_ip), data=rdata, timeout=3)
		print("Response: {0}".format("OK (200)" if r.status_code == 200 else "Probably failed."))
	except requests.exceptions.ConnectTimeout:
		print("Request error: Timed out, check if the web interface is actually running on the URL you provided or try raising the timeout period using --timeout.")
	except requests.exceptions.RequestException as e:
		print("Request error: Error.", e)
	except Exception as e:
		print("Unknown error.", e)

if __name__ == "__main__":
	# todo: config parse (baseurl + command prefs)
	# todo: cleanup
	# todo: optional curses
	aparser = argparse.ArgumentParser()
	aparser.add_argument("--ip", "-c", help="Base IP:PORT where a MPC-HC web interface is listening")
	aparser.add_argument("--ui", "-i", help="Choose an interface. Available options: none (default)|text|curses-line|curses")
	aparser.add_argument("--timeout", "-t", help="Force a non-default (3 second) timeout for the request. (Use if you are running into timeout exceptions a lot.)")
	aparser.add_argument("command") # TODO: flag this as optional when using --ui text | curses ofc
	args = aparser.parse_args()

	if args.ip:
		if args.ui == "text":
			print("Type either a command or 'quit' and submit using Enter.")
			while True:
				acmd = input("> ")
				if acmd != "quit":
					if(acmd in cmds):
						main(str(acmd), args.ip)
					else:
						print("Command not found (locally).")
				else:
					print("Exiting.")
					sys.exit(0)
		
		elif args.ui is None or args.ui == "none":
			main(args.command, args.ip)
	else:
		print("You need to specify an IP of the remote web interface using the --ip argument.")
