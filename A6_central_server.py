import socket
import random
import pickle
from _thread import *
import threading 
lock = threading.Lock() 
from datetime import datetime
import datetime
from operator import itemgetter

p = 0
req = []
flag = 0
requests = open("requests.txt", "w")

IP = localhost 
PORT = 5006

centralsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
centralsocket.bind((IP,PORT))
centralsocket.listen(100)

print("Central server is running!")
print("IP address -" + str(IP)+ ", Port - " + str(PORT))

def acceptrequest(serversocket):
	data = serversocket.recv(1024)
	data.decode()
	req.append(pickle.loads(data)) # creating a list of requests
	lock.release()
	# serversocket.close()

while(1):
	
	while(1):
		req = req[p:]
		(serversocket,address) = centralsocket.accept() # issue
		
		if(flag==0):
			time1 = datetime.datetime.now()
			flag = -1

		lock.acquire()
		print("Got a connection from ", address)
		start_new_thread(acceptrequest, (serversocket,))

		time2 = datetime.datetime.now()
		if(time2.minute()>time1.minute()+1): 
			break


	while(1):
		lock.acquire()
		time1 = datetime.datetime.now()
		final_list=[]
		temp_list=[]
		# indices = []
		for r in req:
			tstamp=(datetime.datetime(r[2],r[3],r[4],r[4], r[5], r[6], r[7]))
			temp_list.append(r[0],r[1],tstamp)
			final_list.append(temp_list)
			temp_list=[]

		final_list.sort(key=itemgetter(2))
		for f in final_list:
			i = f[0]
			j = f[1]
			temp = num_list[i]
			num_list[i] = num_list[j]
			num_list[j] = temp

		time2 = datetime.datetime.now()
		if(time2.minute()>time1.minute()+1): 
			string = pickle.dumps(num_list)	# sending indices and timestamp
		#??????????????	serversocket.send(string) # send to all servers??????????????
			if(req.index(r)!=(req.len()-1)):
				p = req.index(r) + 1
				break

	s1socket.close()
	s2socket.close()
	s3socket.close()
serversocket.close()
