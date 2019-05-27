#!/usr/bin/python2
import commands as sp
import cgi
import os
print("content-type:text/html")
print("")

print("<marquee><h1>WELCOME TO NFS CONFIGURATION</h1></marquee>")

cmd="sudo rpm -q nfs-utils"
output=sp.getstatusoutput(cmd)

if output[0]==0:
	nfs_status_check="installed"
else:
	nfs_status_check="not installed"

nfs_service_status_cmd="sudo systemctl is-active nfs"
ds_output=sp.getstatusoutput(nfs_service_status_cmd)

if ds_output[1] == "active":
	nfs_service_status="running"
else:
	nfs_service_status="stopped"


print("""
<table border='5'>
<tr>
<td>check nfs software</td>
<td>{}</td>
</tr>


<tr>
<td>Install nfs</td>
<td><a href='nfs_install.py'>click here to install nfs</a></td>
</tr>


<tr>
<td>nfs server configure</td>
<td><a href='nfs_server.py'>click here to configure</a></td>
</tr>

<tr>
<td>nfs export check</td>
<td><a href='nfs_export.py'>click here</a></td>
</tr>


<tr>
<td>nfs service status</td>
<td>{}</td>
</tr>


<tr>
<td>nfs service manager</td>
<td><a href='nfs_start.py'>click here to start</a></td>
</tr>

<tr>
<td>nfs_client</td>
<td><a href='nfs_client.py'>click here</a></td>
</tr>

</table>""".format(nfs_status_check,nfs_service_status))


os.system(" sshpass -p {} scp -r /root/exports root@{}:/etc/exports".format(passwd,ip))

