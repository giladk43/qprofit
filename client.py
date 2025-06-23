import socket
import select
import sys
import argparse

BUFFER = 1024

def get_address():
    """
    Gets the ip and port from the cmd
    """
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('ip', help='The ip of the server address', type= str)
    parser.add_argument('port', help='The port of the server address', type=int)
    args = parser.parse_args()
    return args
    

def handle_client():
    my_sock = socket.socket()
    address = get_address()
    my_sock.connect(address)
    


def main():
    handle_client()
    
if __name__ == "__main__":
    main()
