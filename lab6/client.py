import sys
import socket
import os.path
BUFFER_SIZE = 1024


my_file = sys.argv[1]
filename = str(my_file)
host = str(sys.argv[2])
port = int(sys.argv[3])

sock = socket.socket()
sock.connect((host, port))
sock.send(filename.encode())

f = open(filename, 'rb')

size = os.path.getsize(sys.argv[1])
bytes_transported = BUFFER_SIZE
byte = f.read(BUFFER_SIZE)
print(sock.recv(BUFFER_SIZE).decode())

percents = []
while byte:
	percent = bytes_transported * 100 // size
	if percent%10 == 0 and percent not in percents:
		percents.append(percent)
		print(f'{percent}%')
	bytes_transported += BUFFER_SIZE
	sock.send(byte)
	byte = f.read(BUFFER_SIZE)
f.close()
print('Completed')
sock.close()

