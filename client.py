import socket
from resp import RESPEncoder, RESPDecoder, format_resp_response

encoder = RESPEncoder()
decoder = RESPDecoder()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 6379))

while True:
    query = input("Write your message here: ").strip()
    if not query:
        continue

    # Encode the user input as RESP
    resp_bytes = encoder.encode_command(query)
    client.send(resp_bytes)

    # Receive server response
    data = client.recv(1024)
    decoder.feed(data)
    messages = decoder.decode_all()

    for msg in messages:
        print("Server says:", format_resp_response(msg))