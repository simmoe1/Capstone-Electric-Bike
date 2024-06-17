from flask import Flask, render_template, request
from flask_cors import CORS
import socket


CONNECT_TIMEOUT = 10

SERVER_PORT = 50001
SERVER_ADDRESS = "0.0.0.0"
ADDRESS_PORT = (SERVER_ADDRESS, SERVER_PORT)


def connect_to_server():
    # Create an IPv4 TCP socket.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server using its socket address tuple.
    client_socket.connect(ADDRESS_PORT)
    print(f"Connected to {SERVER_ADDRESS} on port {SERVER_PORT}\n")

    return client_socket


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/button-clicked', methods=['POST'])
def buttonClicked():
    button = request.json['button']
    if button == 'button1':
        # execute function for Burst button

        # Send a single byte of data
        data = b'\x31'  # ASCII code for 'A'
        send_socket.sendall(data)
        print(f"Sent {len(data)} bytes of data: {data[0]}")

        print('Burst button pressed')
    elif button == 'button2':
        # execute function for Button 2

        # Send a single byte of data
        data = b'\x32'  # ASCII code for 'A'
        send_socket.sendall(data)
        print(f"Sent {len(data)} bytes of data: {data[0]}")

        print('Burst++ pressed')
    elif button == 'button3':
        # execute function for Button 3

        # Send a single byte of data
        data = b'\x33'  # ASCII code for 'A'
        send_socket.sendall(data)
        print(f"Sent {len(data)} bytes of data: {data[0]}")

        print('Uphill Burst pressed')
    elif button == 'button4':
        # execute function for Button 4

        # Send a single byte of data
        data = b'\x34'  # ASCII code for 'A'
        send_socket.sendall(data)
        print(f"Sent {len(data)} bytes of data: {data[0]}")

        print('Uphill Burst++ pressed')
    elif button == 'button5':
        # execute function for Button 5

        # Send a single byte of data
        data = b'\x35'  # ASCII code for 'A'
        send_socket.sendall(data)
        print(f"Sent {len(data)} bytes of data: {data[0]}")

        print('STOP pressed')
    return 'Button clicked: ' + button


if __name__ == '__main__':
    send_socket = connect_to_server()

    app.run(host='0.0.0.0', port=8089)
