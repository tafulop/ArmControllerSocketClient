import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    
	for request in range(30):
		topic = "test"
		print ("%s %d" % (topic, 90))
		socket.send_string("%s %d" % (topic, 90))
		time.sleep(0.1)

	for request in range(30):
		topic = "test"
		print ("%s %d" % (topic, 0))
		socket.send_string("%s %d" % (topic, 0))
		time.sleep(0.1)

	for request in range(30):
		topic = "test"
		print ("%s %d" % (topic, -90))
		socket.send_string("%s %d" % (topic, -90))
		time.sleep(0.1)

	for request in range(30):
		topic = "test"
		print ("%s %d" % (topic, 0))
		socket.send_string("%s %d" % (topic, 0))
		time.sleep(0.1)