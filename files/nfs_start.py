#!/usr/bin/python2
import commands as sp
print("content-type:text/html")

cmd1="sudo systemctl restart nfs"
output1=sp.getstatusoutput(cmd1)
if output1[0]==0:
	print("location:nfs.py")
	print("")
else:
	print("")
	print("stopped")
