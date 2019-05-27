#!/usr/bin/python2

import commands as s
import cgi

print("content-type: text/html")

cmd="sudo docker rm -f $(sudo docker ps -a -q)"
output=s.getstatusoutput(cmd)

if output[0]==0:
	print("location: docker_manage.py")
	print("\n")

else:
	print("\n")
	print("error")
