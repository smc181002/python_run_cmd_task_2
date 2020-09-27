#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html\n')

queryData = cgi.FieldStorage()
resource = queryData.getvalue('resource')

output = subprocess.getoutput('sudo docker {} ls'.format(resource))
print(output)
