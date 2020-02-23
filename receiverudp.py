import socket

print ("start")
print ("start with prayer")
print ("first step : create socket")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("second step : bind")
ip_address = ("localhost")
port_number = 50000
receiver_address = (ip_address, port_number)
sock.bind((receiver_address))

print "third step : receiver from"
print "waiting for something to arrive..."
data,sender_address = sock.recvfrom(1024)

print "receiver data", data, "from", sender_address