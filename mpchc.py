#!/usr/bin/python3
# coding=utf-8
import sys, os, requests, argparse, json
 
def main(command, base_url):
	cmd = command  # temporary
	print("CMD is", ord(cmd))
	cmds = {"p": 889, "n": 922, "b": 921, "f": 830, "jf": 900, "jb": 899}
	rcmd = cmds[cmd]
	rdata = {"wm_command": rcmd}
	try:
		r = requests.post("{0}/command.html".format(base_url), data=rdata, timeout=4)
	except requests.exceptions.ConnectTimeout:
		print("Error: Request timed out, check if the web interface is actually running on the URL you provided.")
	except:
		print("Unknown error.")

if __name__ == "__main__":
	# todo: config parse (baseurl + command prefs)
	# todo: cleanup
	# todo: optional curses
	aparser = argparse.ArgumentParser()
	aparser.add_argument("--url", help="Base url on which mpc-hc web iface is")
	aparser.add_argument("--ui", help="Available options: none (default)|text|curses")
	aparser.add_argument("command")
	args = aparser.parse_args()
	if args.url:
		if args.ui == "text":
			while True:
				acmd = input("Type a command or 'quit' and press Enter: ")
				if acmd != "quit":
					main(str(acmd), args.url)
				else:
					sys.exit(0)
		
		else:
			main(args.command, args.url)
	else:
		print("You need to specify a URL of the remote web interface using the --url argument.")
