#!/usr/bin/env python2
import argparse
import zmq
import socket
import json


def get_local_ip():
    """
    Retrieve the clients local ip address and return it as a string

    :returns IpAddress as String
    """
###    ip = socket.gethostbyname(socket.gethostname())
    return "172.16.2.17"

context = zmq.Context()

socket = context.socket(zmq.DEALER)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect-address', default='tcp://127.0.0.1:5555')

args = parser.parse_args()

socket.connect(args.connect_address)
port = 5555
msg = "HELLO {} {}".format(get_local_ip(), port)
socket.send(msg)
res = socket.recv()
print res
js = json.load(res)
print js




