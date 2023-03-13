"""
 This class implements a client program that can interact with the server from command line interfaces.
 Once started, it will ask for the IP address or hostname of the server that user should type in.
 Once a connection is established, the client should receive a welcoming message from the server and prints it on the screen.
 Meanwhile, a prompt will show up for the user to enter commands.

 @Author Feng Long: fxl306@case.edu
 @Date 02/14/2022

"""
import socket
import ipaddress


def client_program():
    print("Welcome to the KeyValueService Client")
    while True:
        server_ip = input("Enter the IP address or Hostname of the server: ")
        if server_ip == '':
            continue
        valid = True
        try:
            server = ipaddress.ip_address(server_ip)
        except ValueError:
            try:
                server = ipaddress.ip_address(socket.gethostbyname(server_ip))
            except socket.gaierror:
                valid = False
            except:
                valid = False
        except:
            valid = False
        if not valid:
            print("IP address or Hostname \"", server_ip, "\" is not valid")
        else:
            break
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Please wait while I connect you...")
    client_socket.connect((str(server), 50000))
    data = client_socket.recv(2048).decode()
    print(data)

    while True:
        message = input("KeyValue service> ")
        args = message.split()
        if len(args) == 0:
            continue
        cmd = args[0].lower()
        if cmd == "bye":
            client_socket.send(b'bye')
            print("See you later.")
            client_socket.close()
            break
        else:
            client_socket.send(message.encode())
            data = client_socket.recv(2048).decode()
            print(data)
            continue
    client_socket.close()


if __name__ == '__main__':
    client_program()
