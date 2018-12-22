import socket
import select
import threading
import csv

def Main():
    host  = '10.1.135.140'
    port = 5008

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        print ('connection from : '+ str(addr))
        threading.Thread(target = attend, args = (c, addr)).start()

def attend(c, addr):
    file_name = "data.csv"
    lines = []

    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            lines.append(line)
    List = []
    for line in lines:
        for i in range(0, 3):
            List.append(line[i])


    Flag= True
    a = 0
    while Flag:
        data = c.recv(1024).decode()
        if not data:
            break
        print ("Connected : " + str(data))
        for i in List:
            if i == data:
                a = List.index(i)
                question = List[a+1]
                answer = List[a+2]
                c.send(str(question).encode())
                user_input = c.recv(1024).decode()
            else:

                print("Roll Number not found")
        if(answer == user_input):
            c.send(str('ATTENDANCE-SUCCESS').encode())
            Flag=False
            break
        else:
            c.send(str('ATTENDANCE FAILUR').encode())
    
    c.close()



if __name__ == '__main__':
    Main()
