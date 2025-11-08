import socket
import threading
import time


def client_handler(conn,addr):
	print('[Thread] starting ...')
	time.sleep(1)
	#receive a message from the client
	print(f'Receiving message from {addr}....')
	message_r=conn.recv(1024) #receive  the message with a buffer size of 1024
	message_rd=message_r.decode() #decode the message for bytes to a string
	print(f'Message received: {addr} says {message_rd} message length: {len(message_rd)}')
	
	time.sleep(2) #pause for 5 seconds before sending message
	message_s='Hello client...nice connecting with you'
	message_se=message_s.encode() #encode the message to bytes before sending
	conn.send(message_se) #send the message to our client
	
	time.sleep(2) #pause for 2 seconds
	print('[Thread]Closing connection....')
	conn.close()

host='0.0.0.0' #listen to all interfaces
port=8080

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #This allows the socket to reuse the address even of an ongoing connection is  in TIME_WAIT or CLOSE_WAIT state
server.bind((host,port)) #Bind our host and port to the socket
server.listen(1) #Listen in an interval of every 1 second

all_threads=[] #This is a list of all threads running

try:
	while True:
		conn,addr=server.accept() #accept incoming connections and return conn,addr pair
		t=threading.Thread(target=client_handler,args=(conn,addr))
		t.start()
		all_threads.append(t)
except Exception as e:
	print(e)
finally:
	if s:
		s.close()
	for t in all_threads:
		t.join()


