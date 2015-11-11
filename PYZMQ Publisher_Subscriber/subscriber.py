import sys
import zmq

# Socket to talk to server

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.SUB)

print ("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

socket.setsockopt_string(zmq.SUBSCRIBE, "test")

# Process 5 updates
while(1):
    string = socket.recv()
    topic, messagedata = string.split()
    print (topic, messagedata)
