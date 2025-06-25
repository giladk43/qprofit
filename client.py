import socket
import select
import sys
import argparse

BUFFER = 1024

def get_args():
    """
    Gets the ip and port from the cmd
    """
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('ip', help='The ip of the server address', type=str)
    parser.add_argument('port', help='The port of the server address', type=int)
    parser.add_argument('name', help='The name of the client', type=str)
    parser.add_argument('room_name', help='The room name', type=str)
    args = parser.parse_args()
    return args
    

def handle_client():
    my_sock = socket.socket()
    args = get_args()
    my_sock.connect((args.ip, args.port))
    


def main():
    handle_client()
    
if __name__ == "__main__":
    main()
