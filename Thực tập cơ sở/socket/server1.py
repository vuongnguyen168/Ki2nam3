import socket
import hashlib
# tạo server
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port = 1234
server.bind((host,port))
server.listen()
print("Listening......")


# Nhận kết nối từ server
client,add=server.accept()
print("Connected")

# nhận message
message=client.recv(1024).decode()
print("message taken")
# tính giá trị băm 
key='mykey'
h=hashlib.sha256((message+key).encode())
hashedmessage=h.hexdigest()
print("Done calculating")
#nhận giá trị băm
newhash=client.recv(1024).decode()
print("Hash taken") 
if newhash==hashedmessage:
    print("Data integrity verified")
else:
    print("The received message has lost its integrity")

