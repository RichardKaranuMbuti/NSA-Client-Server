# client.py
import socket
import time

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data
    message = 'This is the message. It will be echoed back.'
    print('sending {!r}'.format(message))
    client_socket.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    start_time = time.time()
    while amount_received < amount_expected:
        data = client_socket.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

    end_time = time.time()
    print(f"Response time: {end_time - start_time} seconds")

finally:
    print('closing socket')
    client_socket.close()
