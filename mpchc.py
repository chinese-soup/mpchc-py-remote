#!/usr/bin/python3
# coding=utf-8

import sys, os, requests, argparse, json
try:
	import config
except:
	print("Config file could not be imported.")

try:
	import command_names
except:
	print("Command names file could not be imported, this means the commands you put in won't appear as readable text and will only appear as the MPC-HC command numbers.")


def main(command, base_ip, port):
	cmds = config.cmds
	
	cmd = command  # temporary
	rcmd = cmds[cmd]
	rcmd_t = command_names.cmds_t[rcmd]
	rdata = {"wm_command": rcmd}
	
	print("Requested: {0} ({1})".format(rcmd_t, rcmd))

	try:
		r = requests.post("http://{0}:{1}/command.html".format(base_ip, port), data=rdata, timeout=config.settings["timeout"])
		print("Response: {0} ({1})".format("OK (200)" if r.status_code == 200 else "Probably failed.", r.headers["Server"]))
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
	aparser.add_argument("--ip", "-c", help="Specify the IP/hostname where a MPC-HC web interface is listening. Use this to override the config values.")
	aparser.add_argument("--port", "-p", help="Specify the PORT on which MPC-HC web interface is listening on. Use this to override the config values.")#, default=13579)
	aparser.add_argument("--ui", "-i", help="Choose an interface. Available options: none (default)|text|curses.")
	aparser.add_argument("--timeout", "-t", help="Force a non-default (3 second) timeout for the request. (Use if you are running into timeout exceptions a lot.)")
	aparser.add_argument("command") # TODO: flag this as optional when using --ui text | curses ofc
	args = aparser.parse_args()

	#if args.ip:
	if args.ui == "text":
		print("Type either a command or 'quit' and submit using Enter.")
		while True:
			acmd = input("> ")
			if acmd.startswith("sleep"):
				t_sleep = float(acmd.split(" ")[1])
				time.sleep(t_sleep)
			elif acmd != "quit":
				if(acmd in config.cmds):
					main(str(acmd), args.ip or config.settings["ip"], args.port or config.settings["port"])
				else:
					print("Command not found (locally).")
			else:
				print("Exiting.")
				sys.exit(0)
	
	elif args.ui is None or args.ui == "none":
		main(args.command, args.ip or config.settings["ip"], args.port or config.settings["port"])
	#else:
	#	print("You need to specify an IP of the remote web interface using the --ip argument.")
