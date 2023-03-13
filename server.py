"""
 This class implements a server program that can interact with the client from command line interfaces.
 Once a connection is established, the server sends a welcome message to the user and prints it on the screen.
 Meanwhile, after client enter commands at its terminal, the server will provide corresponding response.

 @Author Feng Long: fxl306@case.edu
 @Date 02/14/2022

"""

import threading
from threading import Thread
import socket
import re


class KeyValueServerThread(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.hashmap = {'a': 1, 'aaa a': 5, 'b': 1}
        self.sock = sock

    def run(self):
        # sending welcome message
        self.sock.send(b'Welcome to the KeyValue service.')
        while True:
            try:
                valid = True
                data = self.sock.recv(2048).decode()
                if not data:
                    break
                data = re.sub(' +', ' ', data)
                args = data.split()
                if len(args) == 0:
                    continue
                cmd = args[0].lower()
                if cmd == "bye":
                    self.sock.close()
                    break
                elif cmd == "help":
                    help_menu = "help\nget key\nput key value\nvalues\nkeyset\nmappings\nbye"
                    self.sock.send(help_menu.encode())
                    continue
                elif cmd == "keyset":
                    keys = [k for k in self.hashmap.keys()]
                    self.sock.send(str(keys).encode())
                    continue
                elif cmd == "values":
                    values = [v for v in self.hashmap.values()]
                    self.sock.send(str(values).encode())
                    continue
                elif cmd == "mappings":
                    msg = ''
                    for k, v in self.hashmap.items():
                        msg += str(k) + ' ' + str(v) + '\n'
                    self.sock.send(msg[:-1].encode())
                    continue
                elif cmd == "get":
                    key = data.replace(cmd + ' ', '')
                    if key == '' or key == data:
                        valid = False
                    else:
                        if key in self.hashmap:
                            msg = str(self.hashmap[key])
                        else:
                            msg = "Cannot find key: \"" + key + "\" in the data store."
                        self.sock.send(msg.encode())
                elif cmd == "put":
                    key_value = data.replace(cmd + ' ', '')
                    if key_value == '' or key_value == data:
                        valid = False
                    else:
                        try:
                            key, value = key_value.rsplit(' ', 1)
                            if value.isnumeric():
                                self.hashmap[key] = int(value)
                                msg = "Ok."
                            else:
                                msg = "Value \"" + value + "\" is not valid"
                        except ValueError:
                            msg = "Invalid command: \"" + data + "\""
                        self.sock.send(msg.encode())
                else:
                    valid = False
                if not valid:
                    msg = "Invalid command: \"" + data + "\""
                    self.sock.send(msg.encode())
                    continue
            except socket.error:
                data = ''


if __name__ == '__main__':
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('0.0.0.0', 50000))
    while True:
        server_sock.listen(10)
        conn_sock, _ = server_sock.accept()
        th = KeyValueServerThread(conn_sock)
        th.start()
