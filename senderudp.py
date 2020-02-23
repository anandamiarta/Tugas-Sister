import socket

print ("first step : create socket")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("no neet to bind")
print ("second step: send data")
ip_address = "localhost"
port_number = 50000
receiver_address = (ip_address, port_number)
data = "hello"
sock.sendto(data, receiver_address)
print "data", data, "send to", receiver_address