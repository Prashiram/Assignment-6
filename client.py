import socket
import pickle
from datetime import datetime

clientsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP= "localhost"
PORT= 5008

clientsocket.connect((IP, 5008))
listofelements=[]
indices=[]
data=clientsocket.recv(1024)	# recieving list
listofelements=pickle.loads(data)
print(listofelements)

i=input("Enter i: ")
j=input("Enter j: ")

timestamp = datetime.now() # timestamp
indices.append(i)
indices.append(j)
indices.append(timestamp.year)
indices.append(timestamp.month)
indices.append(timestamp.day)
indices.append(timestamp.hour)
indices.append(timestamp.minute)
indices.append(timestamp.second)
indices.append(timestamp.microsecond)
indices_string= pickle.dumps(indices)	# sending indices and timestamp
clientsocket.send(indices_string)
clientsocket.close()
