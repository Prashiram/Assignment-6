import socket
import random

IP = "127.0.0.1"
PORT = 5005

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET indicates IPV4, SOCK_STREAM indicates that the protocol used is TCP 

# bind the socket to IP address and a port
serversocket.bind((IP,PORT))

# become a server socket
serversocket.listen(100)


listdirectory = file.open("lisdir.txt", "r")
requests = file.open("requests.txt", "w")
lisdir = []
line = listdirectory.readline()

lisdir = line.split(",")

print("Server1 is running!")
print("IP address -"+str(IP)+", Port - "+ str(PORT))

while(1):
	(clientsocket,address) = serversocket.accept()
	print("Got a connection from ", address)

	for num in lisdir:
		clientsocket.send(bytes(str(num), 'utf8'))

	# clientsocket.send(data.encode()) #send query to client
	swaptuple = clientsocket.recv(1024).decode() # receive email id
	tup = swaptuple.split(",")

	requests.write(swaptuple)
	# temp = lisdir[i]
	# lisdir[j] = lisdir[i]
	# lisdir[i] = temp

	
clientsocket.close()
serversocket.close()