import socket
import random
import pickle
import datetime
from _thread import *
import threading 
lock = threading.Lock() 

IP = "localhost"
PORT = 5008

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP,PORT)) # act as a server
serversocket.listen(10) # listen to potential clients

def sendtoclient(clientsocket):
	num_list = pickle.dumps(lisdir)
	clientsocket.send(num_list)
	swaptuple = clientsocket.recv(1024) # receive i,j tuple
	st = pickle.loads(swaptuple)
	t = datetime.datetime(st[2],st[3],st[4],st[5],st[6],st[7],st[8])
	centralsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	centralsocket.connect(("localhost", 5007)) # connect to central server
	centralsocket.send(swaptuple)
	lock.release()	
	clientsocket.close()
	centralsocket.close()

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
	#sendtoclient(clientsocket)

serversocket.close()