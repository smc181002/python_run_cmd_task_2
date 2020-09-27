#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html\n')

queryData = cgi.FieldStorage()
netname = queryData.getvalue('netname')

output = subprocess.getoutput('sudo docker network create {}'.format(netname))
print(output)
