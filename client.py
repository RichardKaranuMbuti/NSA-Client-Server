import socket
import time

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Prepare the message
    message = 'This is the message. It will be echoed back.'
    print('sending {!r}'.format(message))

    # Start the timer and send data
    start_time = time.time()
    client_socket.sendall(message.encode())

    # Initialize variables for receiving response
    amount_received = 0
    amount_expected = len(message)
    
    # Receive the response
    while amount_received < amount_expected:
        data = client_socket.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

    # Stop the timer
    end_time = time.time()

    # Calculate and print the response time
    response_time = end_time - start_time
    print(f"Response time: {response_time:.4f} seconds")

finally:
    # Close the socket
    print('closing socket')
    client_socket.close()
