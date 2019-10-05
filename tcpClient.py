"""
Created on Sun Oct  6 03:07:24 2019

@author: Taufiq_Sumadi
"""
import socket
#To get the name of host
host_name = socket.gethostbyname(input("Enter a server address: ")) 
port_number = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#The name of server to connect
print("The name of local machine",host_name)

host_port_pair = (host_name,port_number) #A tuple

#To actively intiate the TCP Server connection
sock.connect(host_port_pair)  

while True:

    msg_for_server = input("Message for server: ")
    if not msg_for_server:
        break
    sock.send(msg_for_server.encode('utf-8'))
   
    
    msg_from_server = sock.recv(2048)
    if not msg_from_server:
        print("<...No Reply from Server...>")
    else:
        print("From Server ==> ",msg_from_server.decode("utf-8"))

sock.close()

"""
    print type(sock.recv(2048)),sock.recv(2048) 
"""
