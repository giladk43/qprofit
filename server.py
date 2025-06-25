import socket
import select
import sys
import argparse
from collections import defaultdict


BUFFER = 1024
TIMEOUT = 1
FINISH = "/exit"

def get_address():
    """
    Gets the ip and port from the cmd
    """
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('ip', help='The ip of the server address', type= str)
    parser.add_argument('port', help='The port of the server address', type=int)
    args = parser.parse_args()
    return args

def connect_server(server_sock, address):
    try:
        server_sock.bind(address)
        server_sock.listen(1)
        server_sock.setblocking(False)
    except socket.gaierror:
        print("This is not a valid address")

def handle_rooms(session, data, client_list):
    for client_session in client_list:
        if session != client_session:
            client_session.send(data.encode())
    
    
def get_room(session, clients_in_rooms):
    for room, client_list in clients_in_rooms:
        if session in client_list:
            return room

def handle_clients(session_list, clients_in_rooms):
    readable, _, _ = select.select(session_list, [], []) 
    
    for session in readable:
        room_name = get_room(session, clients_in_rooms)
        recv_data = session.recv(BUFFER).decode()
        if recv_data == FINISH:
            session_list.remove(session)
            clients_in_rooms[room_name].remove(session)
            session.close()
        else:
            handle_rooms(session, data, clients_in_rooms[room_name])
            
        
def handle_server():
    session_list = []
    first = True
    clients_in_rooms = defaultdict(list) #Will hold a dict with each session in a room
    address = get_address()
    server_sock = socket.socket()
    handle_server(server_sock, address)
    while session_list != [] or first:
        if first:
            first = False
        conn, addr = server_socket.accept()
        session_list.append(conn)
        clients_in_rooms["test"].append(session) #Need to receive the room 
        handle_clients(session_list)
    
    server_sock.close()


def main():
    handle_server()
    
if __name__ == "__main__":
    main()


#functions that still need to be added, transfer -> Use default dict and remove to change where it is
#Get room name from client at the start
#admin
