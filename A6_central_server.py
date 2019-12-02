import socket
import random
import pickle
import concurrent.futures
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
	# data.decode()
	req.append(pickle.loads(data)) # creating a list of requests
	print(req)
	lock.release()

while(1):
	flag = 0
	while(1):
		print("hi!")
		if(flag==0):
				time1 = datetime.datetime.now()
				flag = -1

		try:
			(serversocket,address) = centralsocket.accept()
			lock.acquire()
			print("hi from here2")
			print("Got a connection from ", address)
			start_new_thread(acceptrequest, (serversocket,))

		except socket.timeout:
			print("hi from here3")

		time2 = datetime.datetime.now()
		if(time2.second>time1.second+10): 
			break
	
	print("we outta here")
	time3 = datetime.datetime.now()
	while(1):
		final_list=[]
		temp_list=[]
		# indices = []
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
# print('Swapped : ',i,j)

		time4 = datetime.datetime.now()
		# print(time4)
		if(time4.second>time3.second+5): 

			print("we're done here")
			break

	print(num_list)

serversocket.close()
