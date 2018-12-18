import socket


def main():
	host ='127.0.0.1'
	port =5004

	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))

	message = input("Enter message :   ").encode('ASCII')
	while message !='q':
		s.send(message)
		data = s.recv(1024)
		print("Recieved from server:" + data.decode('ASCII'))
		message=input("Enter another message:  ").encode('ASCII')
	s.close()

if __name__=='__main__':
	main()