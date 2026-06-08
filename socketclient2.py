import socket

SERVER_IP = "10.0.2.5"
PORT = 5000

def start_client():
    try:
        # Create TCP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to server
        client.connect((SERVER_IP, PORT))

        print("Connected to server.")

        # Send message to server
        message = "Hello from Michael's client."
        client.send(message.encode())

        # Receive response from server
        response = client.recv(1024).decode()
        print(f"Server response: {response}")

        # Close connection
        client.close()

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    start_client()