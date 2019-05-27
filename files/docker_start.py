#!/usr/bin/python2

import commands as s

print("content-type: text/html")


cmd="sudo systemctl restart docker"
service=s.getstatusoutput(cmd)
if service[0]==0:
	service_start="docker service is started"
	print("location: docker.py")
	print("")

else:
	print("")
	service_start="error"


