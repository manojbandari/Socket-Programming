import socket
def main():
    host  = '10.1.135.140'
    port = 5008
    s = socket.socket()
    s.connect((host,port))
    
    message = input("Roll Number: ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        if(data.decode() == "Roll Number not found"):
            print("Roll Number not found")
            break
        else:
            print('Question: ' + data.decode())
            data = input("Answer: ")
            s.send(data.encode())
            output = s.recv(1024).decode()
            if(output == 'Attendence-Success'):
                print('Attendence-Success')
                break
    s.close()

if __name__ == "__main__":
    main()
