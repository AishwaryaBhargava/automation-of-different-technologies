#!/usr/bin/python2
import commands as sp
print("content-type:text/html")

cmd="sudo yum install nfs-utils -y"
output=sp.getstatusoutput(cmd)
if output[0]==0:
	print("location:nfs.py")
	print("")
else:
	print("")
	print("not installed")

