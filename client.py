import socket
import pickle

clientsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP=(input('Enter the IP Address of the server: ')).rstrip()
PORT=(input('Enter the Port of the server: ')).strip()
PORT=int(PORT)
clientsocket.connect((IP, PORT))

listofelements=[]
indices=[]
data=clientsocket.recv(1024)										#recieving list
listofelements=pickle.loads(data)
print(listofelements)
i,j=input('Choose indices i and j you want to swap')
indices.append(i)
indices.append(",")
indices.append(j)
indices_string= pickle.dumps(indices)							#sending indices
clientsocket.send(indices)
clientsocket.close()