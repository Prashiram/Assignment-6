import socket
import random
import pickle
import datetime

from _thread import *
import threading 
lock = threading.Lock() 

IP = "localhost"
PORT = 5005

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP,PORT))
serversocket.listen(10)

def sendtoclient(clientsocket):
	num_list = pickle.dumps(lisdir)
	clientsocket.send(num_list)
	swaptuple = clientsocket.recv(1024) # receive i,j tuple
	st = pickle.loads(swaptuple)
	t = datetime.datetime(st[2],st[3],st[4],st[5],st[6],st[7],st[8])
	print("received!")
	print(st[0],st[1],t)
	lock.release()
	# clientsocket.send(swaptuple.encode()) 

# s1socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s1socket.connect(("127.0.0.1", 5006)) # connect to central server //change port

listdirectory = open("lisdir.txt", "r")
lisdir = []
line = listdirectory.readline()
lisdir = line.split(",")

print("Server1 is running!")
print("IP address -"+str(IP)+", Port - "+ str(PORT))

while(1):
	(clientsocket,address) = serversocket.accept()
	lock.acquire()
	print("Got a connection from ", address)
	start_new_thread(sendtoclient, (clientsocket,)) 

		
# clientsocket.close()		#client terminates after one request so it should be terminated inside the loop right?
# serversocket.close()
