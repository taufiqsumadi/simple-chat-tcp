"""
Created on Sun Oct  6 03:07:24 2019

@author: Taufiq_Sumadi
"""
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#To get the name of current host/server
host_name = socket.gethostname() 
port_number = 12345

#The name of local host/server
print("The name of local machine",host_name) 

host_port_pair = (host_name,port_number) #A tuple
print(host_port_pair)

#Bind address to the socket
sock.bind(host_port_pair) 

#listen for connection from client
sock.listen(10)
conn_obj,addr = sock.accept()
while True:
    print("Got a connection from ",addr,"...")
    msg_from_client = conn_obj.recv(2048)
    if not msg_from_client:
        print("Client just press 'Enter' ")
        break
    else:
        print("\nFROM CLIENT ===> ", msg_from_client.decode("utf-8"))
        conn_obj.send(input("TYPE A MESSAGE FOR CLIENT ==> ").encode("utf-8"))

conn_obj.close()    
#Closing the socket
sock.close()
