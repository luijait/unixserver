import socket
import os
PATH = "/var/lib/tor/tor.sock"
if os.path.exists(PATH)
servidor = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
servidor.bind = (PATH)

print ("Escucha ON")

while True:
	datagrama = server.recv(1024)
	if not datagrama:
	 break
	else:
	    print("-" * 10)
	    print(datagrama.decode('utf-8'))
	    if "DONE" == datagrama.decode('utf-8'):
	        break
print ("-" * 20)
print ("Terminado")
servidor.close()
#os.remove("/directorio/del/socket") 1er
