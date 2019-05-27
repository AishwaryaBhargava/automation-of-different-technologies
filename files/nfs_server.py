#!/usr/bin/python2
import commands as sp
print("content-type:text/html")
print("")
print("""
<form action='nfs_server_conf.py'>
your ip<input name='ip' />
</br>
passwd<input type='password' name='p' />
</br>
path of folder to be shared<input name='f' />
</br>
<input type='submit' />
</form>""")
