import socket
import hashlib
# tạo client
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port = 1234


client.connect((host,port))
print("Connected")
# gửi thông điệp
id="B21DCAT227"
message="Hello I am "+id+" client"
client.send(message.encode())
print("Message sent")

#gửi mã băm
key='wrongkey'
h=hashlib.sha256((message+key).encode())
hashedmessage=h.hexdigest()
client.send(hashedmessage.encode())
print("Hash sent")
