#!/usr/bin/python3
import subprocess
import cgi


print("content-type: text/html")
print()

output = subprocess.getoutput("/usr/games/fortune")
print(output + '<br>')
print("<a href='/cgi-bin/app.py'>TAKE NEXT PHRASE</a>")