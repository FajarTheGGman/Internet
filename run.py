# PLease Don't Recode My program because i take a long time to complete this project
# Copyright© 2019 By Fajar Firdaus

from core import module
from core.search_engine import *
from core.wiki import *
from core.track import *
import os

os.getcwd()

class Run:
    def banner():
        print("+-------[Internet]-------+\n")
        print("{")
        print("   Coder : Fajar Firdaus,")
        print("   FB : Fajar Firdaus,")
        print("   IG : fajar_firdaus_7,")
        print("   YT : iTech7732")
        print("} \n")

    def main():
        def help():
            print("[Commands Help]")
            print("- track (Track IP)")
            print("- wiki (Wikipedia in cli )")
            print("- search --no-agent (Search Engine Without User Agent)")
            print("- search --user-agent (Search Engine With User Agent)")
            print("- whois (see website information)")
            print("- help (Show all commands)")
        
        cmd = str(input("[I] >_ "))
        if cmd == "search --no-agent":
            s = Search.net()
        elif cmd == "search --user-agent":
            s = Search.userAgent()
        elif cmd == "wiki":
            d = Wiki.main()
        elif cmd == "track":
            v = Track.main()
        elif cmd == "whois":
            b = Whois.main()
        elif cmd == "help":
            help()
        else:
            print("[!] Wrong Commands")
            help()


a = Run.banner()
a = Run.main()
