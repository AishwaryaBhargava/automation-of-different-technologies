#!/usr/bin/python

import commands as s

print("content-type: text/html")
print("")

cmd = "sudo ansible-playbook splunk_download.yml"
status = s.getstatusoutput(cmd)
if status[0] == 0:
	print("Splunk Software has been downloaded")
else:
	print("Error")
