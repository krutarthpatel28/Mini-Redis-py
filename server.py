import socket
import logging
from resp import RESPEncoder, RESPDecoder
from commands import COMMANDS

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

encoder = RESPEncoder()
decoder = RESPDecoder()

def handle_client(connection, addr):
    logging.info(f"Client connected from {addr}")
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break

            decoder.feed(data)
            commands = decoder.decode_all()

            for cmd in commands:
                if not isinstance(cmd, list) or not cmd:
                    connection.send(encoder.encode_error("ERR invalid command"))
                    continue

                command_name = cmd[0].upper()
                args = cmd[1:]

                handler = COMMANDS.get(command_name)
                if handler:
                    handler(args, connection)
                else:
                    connection.send(encoder.encode_error(f"ERR unknown command '{command_name}'"))
    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}")
    finally:
        connection.close()
        logging.info(f"Client {addr} disconnected")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 6379))
    server.listen(5)

    logging.info("Server started on port 6379...")

    while True:
        connection, addr = server.accept()
        handle_client(connection, addr)

if __name__ == "__main__":
    main()
