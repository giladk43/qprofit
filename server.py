import socket
import select
import sys
import argparse
from collections import defaultdict


BUFFER = 1024
TIMEOUT = 1

def get_address():
    """
    Gets the ip and port from the cmd
    """
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('ip', help='The ip of the server address', type= str)
    parser.add_argument('port', help='The port of the server address', type=int)
    args = parser.parse_args()
    return args


def handle_rooms():
    


def handle_clients(session_list):
    readable, _, _ = select.select(session_list, [], []) 
    
    for session in readable:
        if 

def handle_server():
    session_list = []
    clients_in_rooms = defaultdict(list)
    address = get_address()
    server_sock = socket.socket()
    server_sock.bind(address)
    server_sock.listen(1)
    while session_list != []:
        conn, addr = server_socket.accpet()
        session_list.append(conn)
        handle_clients(session_list)
    
    server_sock.close()


def main():
    handle_server()
    
if __name__ == "__main__":
    main()
