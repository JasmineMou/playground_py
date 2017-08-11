import socket
import sys
import thread

# create a socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	# AF_INET: ipv4; AF_INET6: ipv6
	# SOCK_STREAM: tcp; SOCK_DGRAM: udp
	print("socket created")
except socket.error as err:
	print("socket creation failed with error {}".format(err))

### connect to a local server
def client_thread(conn):
	'''send msg to connected conn'''
	conn.send("Welcome to the server! Type and hit enter\n")
	while True:
		data = conn.recv(1024)
		reply = "Got your msg: " + data
		if not data:
			break
		conn.sendall(data)
	conn.send("Close the connection")
	conn.close()


def connection_local():
	host = ''
	port = 1234
	try:
		s.bind((host,port))
		print("Socket binded.")
	except socket.error,msg:
		print("Bind failed. Error Code: {} Message: {}".format(msg[0],msg[1]))
		sys.exit()

	s.listen(3) 
	# 3 connections are kept waiting is the server is busy, and if a 11th socket tries to connect, then the connection is refused.
	print("Socket is now listening")

	while 1:
		# wait to accept a connection
		conn,addr = s.accept()
		print("Connect with {}:{} with client on connection {}".format(addr[0],addr[1],conn))

		thread.start_new_thread(client_thread, (conn,))


	s.close()
connection_local()


## Terminal 1
# > python web_output.py 
# socket created
# Socket binded.
# Socket is now listening

## Terminal 2, opens a new terminal and type:
# > telnet localhost 1234
# Trying ::1...
# telnet: connect to address ::1: Connection refused
# Trying 127.0.0.1...
# Connected to localhost.
# Escape character is '^]'.
# Thank you for connecting
## Types in "helloworld" after
# helloworld
# Connection closed by foreign host.

## Terminal 1
# Connect with 127.0.0.1:57935 with client on connection <socket._socketobject object at 0x10a0caa60>



### connect to a remote server
def connection_remote():
	host = 'www.google.com'
	port = 80
	try:
		ip = socket.gethostbyname(host)
		print(ip)
	except socket.gaierror:
		# host cannot be resolved
		print("There was an error resolving the host.")
		sys.exit()

	s.connect((ip,port))
	print("The socket has successfully connected to {} on ip {} on port {}".format(host,ip,port))
# connection_remote()


