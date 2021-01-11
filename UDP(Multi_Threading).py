import socket
import threading
import os
print("                                    ======================================")
print("                                                    WINDOW 10")
print("                                    ======================================")
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverip="192.168.0.105"
serverport=307
s.bind(("192.168.0.104",1234))
def send():
	print("Type here....")
	while True:
		data=input()
		data=data.encode()
		print("SENT!!!!")
		s.sendto(data,(serverip,serverport))
		print("==============")
		print("WINDOW 10")
		print("==============")
		
def recv():
	while True:
		x=s.recvfrom(256)
		data=x[0].decode()
		print("\t\t\t\t\t\t\t\t",data)
		print("\t\t\t\t\t\t\t\t RECEIVED!!!")
		print("\t\t\t\t\t\t\t\t")
		print("\t\t\t\t\t\t\t\t============")
		print("\t\t\t\t\t\t\t\t  RHEL8 ")
		print("\t\t\t\t\t\t\t\t============")
x1=threading.Thread(target=send)
x2=threading.Thread(target=recv)
x1.start()
x2.start()