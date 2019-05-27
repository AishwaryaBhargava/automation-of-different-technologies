#!/usr/bin/python2

import commands as s

print("content-type: text/html")

a="sudo yum install docker-ce -y "
install = s.getstatusoutput(a)
if install[0]==0:
	print("location: docker.py")

	print("")
else :
	print("")
	print("error")
