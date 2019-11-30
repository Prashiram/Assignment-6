import socket
import random
import pickle

s1socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1socket.connect(("127.0.0.1", 5005)) # connect to central server //change port

IP = "127.0.0.1"
PORT = 5005

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP,PORT))
serversocket.listen(100)

listdirectory = file.open("lisdir.txt", "r")

lisdir = []
line = listdirectory.readline()

lisdir = line.split(",")

print("Server1 is running!")
print("IP address -"+str(IP)+", Port - "+ str(PORT))

while(1):
	(clientsocket,address) = serversocket.accept()
	print("Got a connection from ", address)
	num_list = pickle.dumps(lisdir)
	clientsocket.send(num_list)
	swaptuple = clientsocket.recv(1024).decode() # receive i,j tuple
	s1socket.send(swaptuple.encode()) 

	
clientsocket.close()
serversocket.close()