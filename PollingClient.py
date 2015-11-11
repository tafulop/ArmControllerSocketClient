import zmq
import time
import sys
import random


def launchSocket():
	
	port_sub = 5558
	context = zmq.Context()

	socket_sub = context.socket(zmq.SUB)
	socket_sub.connect ("tcp://localhost:%s" % port_sub)
	socket_sub.setsockopt_string(zmq.SUBSCRIBE, "motor")
	print ("Connected to server.")

	# Initialize poll set
	poller = zmq.Poller()
	poller.register(socket_sub, zmq.POLLIN)
	socks = dict(poller.poll())

	while(1):

		print ("running")


		if 	socket_sub == zmq.POLLIN:
			
			string = socket_sub.recv(flags=zmq.NOBLOCK)
	
			topic, messagedata = string.split()
			print ("Processing ... ", topic, messagedata)

		time.sleep(1)	
		
		

launchSocket()