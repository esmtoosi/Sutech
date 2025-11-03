
#inthe name of god !!!!

import socket

def start_client():
    server_ip = '10.133.180.105'
    server_port = 1156
    print(f"Connecting to server at {server_ip}:{server_port}...")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Connected to the server.")

    while True:
        try: 
            number = int(input("Enter a Number between 1 - 100 :  "))
            if 1 <= number <= 100:
                break
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Dear user; Please enter a valid number.")

    client_name = input("Enter your Name  : ")
    print(f"Sending message to server: {client_name}, {number}")
    message = f"{client_name}, {number}"
    client_socket.send(message.encode())

    print("Waiting for response from server...")
    response = client_socket.recv(1024).decode()
    print("Message from the server:", response)

    print("Closing the connection...")
    client_socket.close()

if __name__ == "__main__":
    start_client()
