#!/usr/bin/python2

import commands as s
import cgi

print("content-type: text/html")

data=cgi.FieldStorage()
name=data.getvalue('c')

cmd="sudo docker rm -f {}".format(name)

a=s.getstatusoutput(cmd)

if a[0]==0:
	print("location: docker_manage.py")
	print("\n")

else:
	print("\n")
	print("error")
