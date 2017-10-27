from socket import *
import random
import time

host = '127.0.0.1'
port = 35354
s = socket(AF_INET,SOCK_DGRAM)
s.connect((host,port))

for i in range(1,11,1):
    try:
        time1=time.localtime()
        formattime1 = time.strftime('%H:%M:%S', time1)
        # message="Ping " + i + time1
        message="ping"
        message=message + " " + str(i) + " " + str(formattime1)
        s.sendall(message)
        s.settimeout(8)
        data = s.recv(1024)
        time2 = time.localtime()
        print data + " " + str(time.mktime(time2) - time.mktime(time1))
    except timeout:
        print("Request timed out")
s.close()