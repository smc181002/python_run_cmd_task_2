#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html')

queryData = cgi.FieldStorage()
command = queryData.getvalue('q')

print('\n')
output = subprocess.getoutput('sudo man {0}'.format(command))
print(output)
