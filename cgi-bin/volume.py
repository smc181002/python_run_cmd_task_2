#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html\n')

queryData = cgi.FieldStorage()
voln = queryData.getvalue('voln')

output = subprocess.getoutput('sudo docker volume create {}'.format(voln))
print(output)
