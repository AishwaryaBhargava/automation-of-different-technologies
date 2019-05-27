#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("\n")

cmd="sudo ansible-playbook client-staas.yml"

sp.getoutput(cmd)

print("storage successful")
