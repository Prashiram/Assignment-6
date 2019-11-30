import socket
import random
import pickle
from datetime import datetime
import datetime

IP = localhost 
PORT = 5006

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP,PORT))
serversocket.listen(100)

print("Central server is running!")
print("IP address -"+str(IP)+", Port - "+ str(PORT))


requests = open("requests.txt", "w")



p = 0
req = []

if((s1socket,address1) = serversocket.accept() or (s2socket,address2) = serversocket.accept() or (s3socket,address3) = serversocket.accept()):
	#print("Connected to ", address1, ", ", address2, "and ", address3)

	while(1):
		req = req[p:]
		time1 = datetime.datetime.now()
		while(1):
			if(data == (s1socket.recv(1024) or s2socket.recv(1024) or s3socket.recv(1024))):
				data.decode()
				req.append(pickle.loads(data)) #creating a list of requests
			time2 = datetime.datetime.now()
			if(time2.minute()>time1.minute()+1): 
				break 
		time1 = datetime.datetime.now()
		while(1):
			for r in req:
				t = listofele[2:]
				datetime.datetime(t[0],t[1],t[2],t[3], t[4], t[5], t[6])
				time2 = datetime.datetime.now()
				if(time2.minute()>time1.minute()+1): 
					if(req.index(r)!=(req.len()-1)):
						p = req.index(r) + 1
						break

	s1socket.close()
	s2socket.close()
	s3socket.close()				#shouldnt this be there instead of clientsocket ? Also It should be inside the outer while loop right?
serversocket.close()
