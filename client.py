#This is a simple client side logic 
import socket
import time

class Client:
	def __init__(self):
		self.host='host ip here' #replace this with our host ip
		self.port=8080 #The port we will use
	def connect(self):
		sock=socket.socket()
		sock.connect((self.host,self.port)) #connect to the host
		host_name=sock.getpeername()
		print(f'Host info: {host_name}')
		time.sleep(1)
		#Send a message to host
		message_s='Hello host....Nice connecting to you...'
		message_se=message_s.encode() #encode the message
		sock.send(message_se) #send the message
		time.sleep(1)
		#Receive a message form the host
		message_r=sock.recv(1024) #recv message
		message_rd=message_r.decode() #decode message
		legth=len(message_rd)
		print(f'Message  received from {self.host} saying {message_rd} message lenght : {length}')
		sock.close() #close the socket 

if __name__=='__main__':
	s=Client()
	s.connect()


