#!/usr/bin/python2

import commands as s
import cgi

print("content-type: text/html")
print("\n")

cmd=cgi.FieldStorage()
image=cmd.getvalue('imagename')
cname=cmd.getvalue('container_name')
gname=cmd.getvalue('gui')
con=cmd.getvalue('con')

if gname == "gui_no":
	cmd1="sudo docker run -dit --name {} {} ".format(cname, image)
	
else:
	cmd1="sudo docker run -dit --name {}  --ipc=host -e DISPLAY=:0  -v /tmp/.X11-unix/:/tmp/.X11-unix  {} ".format(cname, image)

	
output=s.getstatusoutput(cmd1)
print(output)
if output[0]==0:
	print("os is launched")
else:
	print("error")



