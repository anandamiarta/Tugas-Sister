import socket
import json

print "creating a RTCP Sender"
print "first step : create socket"
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "second step : connect"
ip_address = "192.168.43.39"
port_number = 50001
receiver_address= (ip_address, port_number)
sock.connect(receiver_address)

print "third step : send data"
data = {"name":" Ananda Miarta", "nim":1301174616,"message":"Hadir Pak"}
datax = json.dumps(data)
sock.send(datax)
print "data", datax,"sent to ", receiver_address
print "fourth step:close"
sock.close()