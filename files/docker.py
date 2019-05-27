#!/usr/bin/python2

import commands as s

print("content-type: text/html")
print("")


print("<center><h1><u>Welcome to docker server </center></h1></u>")
print("<form action='create_container.py'>")
print("<br/>")

cmd="sudo rpm -q docker-ce"
status_output=s.getstatusoutput(cmd)
if status_output[0]==0:
	docker_status="installed"
else:
	docker_status="not installed"

cmd1="sudo systemctl is-active docker"
status_docker_service=s.getstatusoutput(cmd1)
if status_docker_service[1]=="active":
	service_status="running"
else:
	service_status="stopped"


print("""<table border='5'>

<tr>
<td>status of docker</td>
<td>{}</td>
</tr>

<tr>
<td>Install docker</td>
<td><a href='docker_install.py'>click here to install docker</a></td>
</tr>

<tr>
<td>status of docker service </td>
<td>{}</td>
</tr>

<tr>
<td>start  docker service</td>
<td><a href='docker_start.py'>click here to start docker service</a></td>
</tr>

<tr>
<td> docker images</td>
<td><select name='imagename'>""".format(docker_status, service_status))

cmd3="sudo docker images"
a=s.getoutput(cmd3)
image_output=a.split("\n")
for i in image_output[1:]:
	print("<option>" + i.split()[0] + ":" + i.split()[1] + "</option>")

print("""
</select></td>
</tr>

<tr>
<td>name of docker container you want to create</td>
<td><input type='text' name='container_name'/> </td>
</tr>


<tr>
<td>do you require GUI</td>
<td>
yes <input type='radio' name='gui' value='gui_yes' />
no <input type='radio' name='gui' value='gui_no'/>
</td>
</tr>


<tr>
<td>submit if you want to create container</td>
<td><input type='submit'/></td>
</tr>

<tr>
<td>to manage docker</td>
<td><a href='docker_manage.py'>click here </a></td>
</tr>



<table>
""")

print("</form>")




