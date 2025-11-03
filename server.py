import socket
import threading

def handle_client(client_socket):
    try:
        message = client_socket.recv(1024).decode()
        print(f"Message received from client: {message}")
        
        parts = message.split(',')
        client_name = parts[0].strip()
        client_number = int(parts[1].strip())
        
        server_number = 50
        
        print(f"Received from {client_name}: {client_number}")
        
        total = client_number + server_number
        
        response = f"Server: {server_name}, Your number: {client_number}, Total: {total}"
        client_socket.send(response.encode())
    
    finally:
        client_socket.close()

def start_server():
    server_ip = '10.133.180.105'
    server_port = 1156
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_ip}:{server_port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection received from {client_address}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()

