#!/usr/bin/env python3.3

import socket, argparse, sys
UTF8 = 'utf-8'

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket created
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((args.host, args.port)) # socket bound
except OSError:
    sys.stderr.write("Oops\n")
    sys.exit(1)
s.listen(10) # listening, 10 in queue

client, addr = s.accept()
# print("Approached by {}:{}".format(*addr))
data = client.recv(4096)
decoded = data.decode(UTF8)
# print("Got '{}'".format(decoded))

client.sendall("{} to you too".format(decoded).encode(UTF8))