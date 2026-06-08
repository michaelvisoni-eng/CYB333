import socket

SERVER_IP = "10.0.2.5"
PORT = 5000

def start_server():
    try:
        # Create TCP socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind to IP and port
        server.bind((SERVER_IP, PORT))

        # Listen for one connection
        server.listen(1)

        print(f"Server listening on {SERVER_IP}:{PORT}")

        # Accept a client connection
        client, address = server.accept()

        print(f"Connection received from {address}")

        # Receive message from client
        message = client.recv(1024).decode()
        print(f"Message received: {message}")

        # Send response back
        response = "Hello from the server!"
        client.send(response.encode())

        # Close connections
        client.close()
        server.close()

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    start_server()