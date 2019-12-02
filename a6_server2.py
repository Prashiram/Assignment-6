import socket
import random
import pickle
import datetime

IP = "localhost"
PORT = 5000

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP,PORT)) # act as a server
serversocket.listen(10) # listen to potential clients
serversocket.settimeout(5)

lisdir = [1,2,3,4,5,6,7,8,9,10]

print("Server1 is running!")
print("IP address -"+str(IP)+", Port - "+ str(PORT))

while(1):
	try:
		(clientsocket,address) = serversocket.accept()
		print("Got a connection from ", address)
		num_list = pickle.dumps(lisdir)
		clientsocket.send(num_list)
		swaptuple = clientsocket.recv(1024) # receive i,j tuple
		st = pickle.loads(swaptuple)
		t = datetime.datetime(st[2],st[3],st[4],st[5],st[6],st[7],st[8])
		centralsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		centralsocket.connect(("localhost", 5002)) # connect to central server
		centralsocket.send(swaptuple)
		clientsocket.close()
		centralsocket.close()

	except:
		try:
			(s1socket,address) = serversocket.accept()
			new_list = clientsocket.recv(1024)
			lisdir = pickle.loads(new_list)
			
		except socket.timeout:
			continue

serversocket.close()