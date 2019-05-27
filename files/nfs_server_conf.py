#!/usr/bin/python2
print("content-type:text/html")


import cgi
import commands as sp

form=cgi.FieldStorage()
ip=form.getvalue('ip')
passwd=form.getvalue('p')
folder_name=form.getvalue('f')

#print(ip,passwd,folder_name)

f=open("/root/Desktop/automation\ work/exports",'w')
f.write("{} *(rw,no_root_squash)".format(folder_name))
f.close()

var=sp.getstatusoutput("sudo sshpass -p {} scp -o StrictHostKeyChecking=no /root/Desktop/automation\ work/exports {}:/etc/exports".format(passwd,ip))
print("location:nfs.py")
print("")

