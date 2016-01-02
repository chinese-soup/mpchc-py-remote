#!/usr/bin/python3
# coding=utf-8
import sys, os, requests, argparse, json
 
def main(command, base_url):
	base_url = base_url or "http://192.168.0.105:3333" # temporary
	cmd = command  # temporary
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
	aparser = argparse.ArgumentParser()
	aparser.add_argument("--url", help="base url on which mpc-hc web iface is")
	aparser.add_argument("command")
	args = aparser.parse_args()
	if args.url:
		main(args.command, args.url)
	else:
		main(args.command, "")
