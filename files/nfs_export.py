#!/usr/bin/python2
import commands as sp
print("content-type:text/html")
print("")

cmd="sudo exportfs -v"
print(sp.getstatusoutput(cmd))
