#!/usr/bin/python

import commands as s

print("content-type: text/html")
print("")

cmd = "sudo ansible-playbook slave_setup.yml"
status = s.getstatusoutput(cmd)
if status[0] == 0:
	print("Datanode service has been started")
else:
	print("Error")
