#!/usr/bin/python

import commands as s

print("content-type: text/html")
print("")

cmd = "sudo ansible-playbook jobtracker_setup.yml"
status = s.getstatusoutput(cmd)
if status[0] == 0:
	print("Jobtracker service has been started")
else:
	print("Error")
