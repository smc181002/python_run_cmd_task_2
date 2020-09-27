#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html\n')

queryData = cgi.FieldStorage()
imgname = queryData.getvalue('imgname')
imgv = queryData.getvalue('imgv') or 'latest'
contname = queryData.getvalue('contname')
volname = queryData.getvalue('volname')
contmnt = queryData.getvalue('contmnt')
net = queryData.getvalue('net') or 'bridge'

cId = ''
dRun = 'sudo docker run -dit'
isContname = ''
isVol = ''

if contname:
    isContname = '--name {}'.format(contname)

if contmnt and volname :
    isVol = '-v {}:{}'.format(volname, contmnt)

cId = subprocess.getoutput('{} -P {} --net {} {} {}:{}'.format(
    dRun, isContname, net, isVol, imgname, imgv))
print(cId)
