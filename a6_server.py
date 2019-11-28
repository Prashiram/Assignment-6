import socket
import random

IP = "127.0.0.1"
PORT = 5005

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET indicates IPV4, SOCK_STREAM indicates that the protocol used is TCP 

# bind the socket to IP address and a port
serversocket.bind((IP,PORT))

# become a server socket
serversocket.listen(100)


listdirectory = file.open("lisdir.txt", "r")
requests = file.open("requests.txt", "w")
lisdir = []
line = listdirectory.readline()

lisdir = line.split(",")

print("Server1 is running!")
print("IP address -"+str(IP)+", Port - "+ str(PORT))

while(1):
	(clientsocket,address) = serversocket.accept()
	print("Got a connection from ", address)

	for num in lisdir:
		clientsocket.send(bytes(str(num), 'utf8'))

	# clientsocket.send(data.encode()) #send query to client
	swaptuple = clientsocket.recv(1024).decode() # receive email id
	i, j = swaptuple.split(",")


	for e in email:
		if(reply == e):
			p = email.index(e)
			q = 0 	# flag = 0 => found email address

	if(q==-1): # flag = -1 => email address not found
		clientsocket.send("Invalid email address or user not enrolled in course".encode())
		clientsocket.close()
		serversocket.close()
		exit()

	else:
		clientsocket.send(flag[p].encode())
		if(flag[p] == '0'):
			reply = clientsocket.recv(1024).decode() # receive number to continue
			rn = 0
			while(rn<3): #generating random unique password
				num = random.randint(10000, 99999) 
				for psw in password:
					if(num!=psw):
						rn=rn+1

			password[p] = str(num) 
			data = "Welcome, "+ name[p] +"! This is your first time. Your password is: "+str(num)+". Use this to login."
			clientsocket.send(data.encode())
			flag[p] = '1' # has to be updated on the file
			new_entry = p

		reply = clientsocket.recv(1024).decode() # receive number to continue
		data = name[p] +", you are a registered user." # Registered user
		clientsocket.send(data.encode())
		reply = clientsocket.recv(1024).decode() #receive number to continue
		data = "Enter password: " #query to get password
		clientsocket.send(data.encode())
		reply = clientsocket.recv(1024).decode() #receive password
		if(reply == password[p]): #verifying if password is correct and sending score
			data = "Your score is: "+grade[p]
		else: 
			data = "Incorrect password!"
		clientsocket.send(data.encode())

	cgd.seek(0,0)
	if(new_entry!=-1):
		for i in range(len(lines)):
			rd = []
			if(i==new_entry):
				cgd.write(flag[i])
			rd = cgd.readline() #to seek to the right location

	login.seek(0,0)
	for i in range(len(lines)):
		if(i<(len(lines)-1)):
			login.write(str(password[i])+",")
		else:
			login.write(str(password[i]))
	
clientsocket.close()
serversocket.close()