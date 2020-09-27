#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html\n')

queryData = cgi.FieldStorage()
imgname = queryData.getvalue('imgname')
imgv = queryData.getvalue('imgv') or 'latest'

output = subprocess.getoutput('sudo docker pull {}:{}'.format(imgname, imgv))
print(output)
