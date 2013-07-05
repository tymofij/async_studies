#!/usr/bin/env python3.3

import socket, argparse

UTF8 = 'utf-8'

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
parser.add_argument('message', type=str)
args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((args.host, args.port))
except OSError:
    sys.stderr.write("Oops\n")
    sys.exit(1)

s.sendall(args.message.encode(UTF8))

received_data = s.recv(4096)
print(received_data.decode(UTF8))
