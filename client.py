import socket
import select
import sys
import argparse
import time

TIMEOUT = 1
BUFFER = 1024
FINISH = "/exit"

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
   
def connect_client(my_sock, address):
    try:
        my_sock.connect(address)
    except socket.gaierror:
        print("This is not a valid address")
    
    
def handle_input_output(my_sock, name):
    data_list = [sys.stdin, my_sock]
    
    readable, _, _ = select.select(data_list, [], [])
    
    for data in readable:
        if data == my_sock:
            data_recv = my_sock.recv(BUFFER)
            print(data_recv.decode())
        else:
            message = input()
            if message == FINISH:
                my_sock.send(FINISH.encode())
                data_recv = my_sock.recv(BUFFER)
                print(data_recv.decode())
                return False
            my_sock.send(f"{name}: {message}".encode())
    return True

def handle_client():
    my_sock = socket.socket()
    args = get_args()
    end_convo = True
    connect_client(my_sock, (args.ip, args.port))
    message = args.room_name
    print(message)
    my_sock.send(message.encode())
    print("Type /exit to stop the connection")
    print(f"{args.name} you are in the chat! ")
    while end_convo:
        end_convo = handle_input_output(my_sock, {args.name})
        
    
    my_sock.close()
    


def main():
    handle_client()
    
if __name__ == "__main__":
    main()
