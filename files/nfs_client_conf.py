#!/usr/bin/python2
import commands as sp
print("content-type:text/html")


import cgi

form=cgi.FieldStorage()
ip=form.getvalue('ip')
passwd=form.getvalue('p')
server_ip=form.getvalue('sip')
shared_folder=form.getvalue('f1')
mount_folder_name=form.getvalue('f')

sp.getstatusoutput("sudo sshpass -p {} ssh -l root {} mkdir {}".format(passwd,ip,mount_folder_name))
sp.getstatusoutput("sudo sshpass -p {} ssh -l root {} mount {}:{} {}".format(passwd,ip,server_ip,shared_folder,mount_folder_name))
print("location:nfs.py")
print("")

