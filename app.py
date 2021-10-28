#!/usr/bin/python3
import subprocess
import cgi


print("content-type: text/html")
print()

output = subprocess.getoutput("/usr/games/fortune")

print(output + '<br>')
print("<a href='/cgi-bin/app.py'>TAKE NEXT PHRASE</a><br>")


# For task 3
addRows = subprocess.getoutput("/usr/games/fortune >> /fortune/file.txt")
countRows = subprocess.getoutput("wc -l /fortune/file.txt")

print("<p>Add phrase to storage file...</p>" + addRows)
print("<p>Number of rows in storage file is: </p>" + countRows)
