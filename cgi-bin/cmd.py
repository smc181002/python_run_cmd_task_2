#!/usr/bin/python3

import subprocess, cgi

print('content-type: text/html')

queryData = cgi.FieldStorage()
command = queryData.getvalue('q')

if "google" in command:
    print('Location: http://google.com')
    print('\n')
elif "github" in command:
    print('Location: http://github.com')
    print('\n')
elif "reddit" in command:
    print('Location: http://reddit.com')
    print('\n')
elif "insta" in command or "insta" in command:
    print('Location: http://instagram.com')
    print('\n')
elif "stackoverflow" in command:
    print('Location: http://stackoverflow.com')
    print('\n')
elif "linkedin" in command:
    print('Location: http://linkedin.com')
    print('\n')
elif "facebook" in command:
    print('Location: http://facebook.com')
    print('\n')
elif "whatsapp" in command:
    print('Location: http://web.whatsapp.com')
    print('\n')
else: 
    print('\n')
    output = subprocess.getoutput('sudo {0}'.format(command))
    print(output)
