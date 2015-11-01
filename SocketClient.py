#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import re

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response

while True:

	#print("Sending request %s ")
	socket.send(b"I am here.")

	#  Get the reply.
	message = socket.recv()
	print("Received reply [%s]" % (message))

	#match = re.match(b'.*', message)
	match = re.match(b'.*(M\d+):(\d+.?\d*)', message)


	print ("Found: ", match.group())
	print ("Motor: ", match.group(1))
	print ("Angle: ", match.group(2))
