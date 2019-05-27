#!/usr/bin/python2

import commands as s

print("content-type: text/html")
print("\n")

cmd="sudo docker ps -a"
output=s.getoutput(cmd)

print("""
<a href='container_cleanall.py'>Click here</a> to clean all containers

<form action='container_service.py'>
<table border=5>
<tr>

<td>Container name</td>
<td>Container Id</td>
<td>Image</td>
<td>Status</td>
<td>Service Start</td>
<td>Service Stop</td>
<td>Clean</td>

</tr>
""")

for i in output.split("\n")[1:]:
	if "Up" in i:
		status="running"
	elif "Created" in i:
		status="created "
	elif "Exited" in i:
		status="stopped"
	a=i.split()
	print("""	
<tr>

<td>{0}</td>
<td>{1}</td>
<td>{2}</td>
<td>{3}</td>
<td><a href='container_start.py?c={0} '>start </a></td>
<td><a href='container_stop.py?c={0} '>stop </a></td>
<td><a href='container_clean.py?c={0} '>clean </a></td>

</tr

""".format(a[-1],a[0],a[1],status))
	

print("</table>")
print("</form>")
print("""
<a href='docker_menu.py'>Click here </a> to go back to docker menu
""")


