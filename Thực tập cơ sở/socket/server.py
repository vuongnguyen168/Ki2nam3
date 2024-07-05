import socket
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
message=client.recv(1024).decode()
print(message)

# gửi phản hồi từ server
response=message.replace("client","server")
client.send(response.encode())
