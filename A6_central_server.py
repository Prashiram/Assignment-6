import socket
import random
import pickle
import concurrent.futures
from _thread import *
import threading 
from datetime import datetime
import datetime
from operator import itemgetter

p = 0
req = []
flag = 0
# requests = open("requests.txt", "w")

IP = "localhost" 
PORT = 5002

num_list = [1,2,3,4,5,6,7,8,9,10]

centralsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
centralsocket.bind((IP,PORT))
centralsocket.listen(100)
centralsocket.settimeout(5)

print("Central server is running!")
print("IP address -" + str(IP)+ ", Port - " + str(PORT))

def acceptrequest(serversocket):
	data = serversocket.recv(1024)
	req.append(pickle.loads(data)) # creating a list of requests
	print(req)

while(1):
	flag = 0
	while(1):
		print("Location 0")
		if(flag==0):
				time1 = datetime.datetime.now()
				flag = -1

		try:
			(serversocket,address) = centralsocket.accept()
			print("Location 1")
			print("Got a connection from ", address)
			start_new_thread(acceptrequest, (serversocket,))

		except socket.timeout:
			print("Location 2")

		time2 = datetime.datetime.now()
		if(time2.second>time1.second+10): 
			break

	time3 = datetime.datetime.now()
	while(1):
		final_list=[]
		temp_list=[]
		if(len(req)!=0):

			for r in req:
				tstamp=(datetime.datetime(r[2],r[3],r[4],r[4], r[5], r[6], r[7]))
				temp_list.append(r[0])
				temp_list.append(r[1])
				temp_list.append(tstamp)
				final_list.append(temp_list)
				temp_list=[]

			final_list.sort(key=itemgetter(2))
			for f in final_list:
				i = int(f[0])
				j = int(f[1])
				temp = num_list[i]
				num_list[i] = num_list[j]
				num_list[j] = temp
				p=p+1
			req = req[p:]

		time4 = datetime.datetime.now()
		if(time4.second>time3.second+10): 
			break

	print(num_list)
	new_list = pickle.dumps(num_list)
	
	s1socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s1socket.connect(("localhost", 4999)) # connect back to the three servers
	s1socket.send(new_list)

	s2socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2socket.connect(("localhost", 5000))
	s2socket.send(new_list)

	s3socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s3socket.connect(("localhost", 5001))
	s3socket.send(new_list)

serversocket.close()
