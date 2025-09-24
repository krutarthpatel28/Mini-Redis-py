class RESPEncoder:
    def encode_simple_string(self, value: str) -> bytes:
        return f"+{value}\r\n".encode()

    def encode_error(self, message: str) -> bytes:
        return f"-{message}\r\n".encode()

    def encode_integer(self, number: int) -> bytes:
        return f":{number}\r\n".encode()

    def encode_bulk_string(self, value: str | None) -> bytes:
        if value is None:
            return b"$-1\r\n"
        return f"${len(value)}\r\n{value}\r\n".encode()

    def encode_array(self, items: list[str]) -> bytes:
        arr = f"*{len(items)}\r\n"
        arr += "".join(self.encode_bulk_string(item).decode() for item in items)
        return arr.encode()


class RESPDecoder:
    def __init__(self):
        self.buffer = b""

    def feed(self, data: bytes):
        self.buffer += data

    def decode_all(self) -> list:
        commands = []
        while self.buffer:
            if self.buffer[0:1] == b"*":
                cmd, used = self._decode_array(self.buffer)
                if not cmd:
                    break
                commands.append(cmd)
                self.buffer = self.buffer[used:]
            else:
                break
        return commands

    def _decode_array(self, data: bytes):
        try:
            newline = data.index(b"\r\n")
        except ValueError:
            return None, 0

        n = int(data[1:newline])
        items = []
        i = newline + 2
        for _ in range(n):
            if data[i:i+1] != b"$":
                return None, 0
            newline = data.index(b"\r\n", i)
            length = int(data[i+1:newline])
            start = newline + 2
            end = start + length
            items.append(data[start:end].decode())
            i = end + 2
        return items, i
