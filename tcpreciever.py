import socket 
import json
print "TCP Receiver"
print "first step : create socket"
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print " second step : bind"
ip_address = "localhost"
port_number = 50001
receiver_address = (ip_address, port_number)
sock.bind(receiver_address)
print "third step : listen"
sock.listen(1)
print "fourth step :accept"
print " wating for connection to come..."
while True :
    conn, sender_address = sock.accept()
    print "fifth step: recieve data"
    datax = conn.recv(1024)
    try:
        data = json.loads(datax)
        print "name: ", data["name"],
        print "nim: ", data["nim"],
        print "message:" , data["message"]
    except:
        "bukan data json"
    print "name: ", data["name"],
    print "nim: ", data["nim"],
    print "message:" , data["message"]
    print "received", data, "from ", sender_address

    conn.close()