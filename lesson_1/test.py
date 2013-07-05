#!/usr/bin/env python3.3

import subprocess, unittest

class TestAsync1(unittest.TestCase):

    def test_hello(self):
        p = subprocess.Popen(["./server.py", "localhost", "7777"])
        out = subprocess.check_output(
            ["./client.py", "localhost", "7777",  "'ku ku'"]
            ).decode('utf-8')

        self.assertEqual(out, "'ku ku' to you too\n")
        p.terminate()

    def test_noserver(self):
        self.assertEqual(
            subprocess.call(["./server.py", "localhost", "1"], stderr=subprocess.DEVNULL),
            1)

    def test_noclient(self):
        self.assertEqual(
            subprocess.call(["./client.py", "localhost", "1", "msg"], stderr=subprocess.DEVNULL),
            1)

if __name__ == '__main__':
    unittest.main()













