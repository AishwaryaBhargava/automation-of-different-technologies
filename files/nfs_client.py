#!/usr/bin/python2
print("content-type:text/html")
print("")
print("""
<form action='nfs_client_conf.py' >
ip<input name='ip' />
</br>
passwd<input type='password' name='p' />
</br>
server ip<input name='sip' />
</br>
path of shared folder<input name='f1' />
</br>
path of mount folder<input name='f' />
</br>
<input type='submit' />
</form> """)

