import subprocess
import socket
import winapps



hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

address = local_ip
res = subprocess.call(['ping', '-c', '3', address])
if res == 0:
   print (address," Address is active", "OK")
else:
   print ("IP" ,address," is not active")


item=['google','anaconda','android studio']
for i in item:
    for items in winapps.search_installed(i):
        print(items)