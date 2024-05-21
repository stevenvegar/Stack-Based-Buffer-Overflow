import socket
import traceback

target = "172.16.0.199"
t_port = 90
buff = b"A" * 1773
# Fuzzing with 1773 bytes


while True:
	try:
		payload = b"GET /" + buff + b" HTTP/1.1\r\n\r\n"
		print("Fuzzing with %s bytes" % len(buff))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, t_port))
		s.sendall(payload)
		s.recv(1024)
		s.close()
		buff = buff + b"A"

	except:
		traceback.print_exc()
		break
