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

IP = "localhost" 
PORT = 5007

num_list = [1,2,3,4,5,6,7,8,9,10]

centralsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
centralsocket.bind((IP,PORT))
centralsocket.listen(100)

print("Central server is running!")
print("IP address -" + str(IP)+ ", Port - " + str(PORT))

def acceptrequest(serversocket):
	data = serversocket.recv(1024)
	# data.decode()
	req.append(pickle.loads(data)) # creating a list of requests
	lock.release()
	# serversocket.close()

while(1):
	print("hi from here")
	while(1):
		req = req[p:]

		t1 = datetime.datetime.now()
		(serversocket,address) = centralsocket.accept() # issue
		print("hi from here2")
		if(flag==0):
			time1 = datetime.datetime.now()
			flag = -1

		lock.acquire()
		print("Got a connection from ", address)
		start_new_thread(acceptrequest, (serversocket,))

		time2 = datetime.datetime.now()
		if(time2.second>time1.second+1): 
			break


	# while(1):
	lock.acquire()
	time1 = datetime.datetime.now()
	final_list=[]
	temp_list=[]
	# indices = []
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

	print(num_list)
		# time2 = datetime.datetime.now()
		# if(time2.second>time1.second+30): 
		# 	string = pickle.dumps(num_list)	# sending indices and timestamp
		# #??????????????	serversocket.send(string) # send to all servers??????????????
		# 	if(req.index(r)!=(req.len()-1)):
		# 		p = req.index(r) + 1
		# 		break

# 	s1socket.close()
# 	s2socket.close()
# 	s3socket.close()
serversocket.close()
