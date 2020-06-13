import socket
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET=IP
#socket.SOCK_STREAM=FTP
host=socket.gethostname() #method that retrieves name of the host machine
port=8080
cs.connect((host,port)) #its a client so we connect method
msg=cs.recv(1024) #print recieved message on console
print(msg.decode('UTF-8'))
# loop is used to make chatting between two machine
while True:
    msg1=input('Send Message to server=>') # sends message to server,while sending message is encoded
    if msg1:
        cs.send(msg1.encode('UTF-8'))

    msg2=cs.recv(1024) # recieves message from server,while recieveing message is decoded
    if msg2:
        print('\n')
        print(msg2.decode('UTF-8'))

