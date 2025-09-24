# PyRedis - A Mini Redis Clone in Python

A lightweight, educational implementation of Redis written in Python. This project recreates core Redis functionality including the RESP protocol, TCP networking, and fundamental data operations with key expiration support.

## Features

• **RESP Protocol Implementation** - Full Redis Serialization Protocol (RESP) encoder and decoder
• **TCP Socket Server** - Multi-client TCP server with connection handling
• **Core Commands** - PING, SET, GET operations with Redis-compatible syntax
• **Key Expiration** - TTL support with EX parameter for automatic key expiry
• **Client Interface** - Built-in command-line client for testing and interaction
• **Memory Storage** - In-memory key-value store with expiration management

## Installation

Clone the repository:

```bash
git clone https://github.com/krutarthpatel28/Mini-Redis-py
cd pyredis
```

No additional dependencies required - uses only Python standard library.

## Usage

### Starting the Server

```bash
python server.py
```

The server will start on `localhost:6379` by default.

### Using the Client

In a separate terminal, run the client:

```bash
python client.py
```

### Example Commands

```bash
# Test server connectivity
PING

# Set a key-value pair
SET mykey "Hello World"

# Set a key with expiration (10 seconds)
SET session:123 "user_data" EX 10

# Retrieve a value
GET mykey

```

## RESP Protocol Examples

### Request/Response Flow

**PING Command:**
```
Client sends: *1\r\n$4\r\nPING\r\n
Server responds: +PONG\r\n
```

**SET Command:**
```
Client sends: *3\r\n$3\r\nSET\r\n$5\r\nmykey\r\n$5\r\nvalue\r\n
Server responds: +OK\r\n
```

**GET Command:**
```
Client sends: *2\r\n$3\r\nGET\r\n$5\r\nmykey\r\n
Server responds: $5\r\nvalue\r\n
```

**GET Non-existent Key:**
```
Client sends: *2\r\n$3\r\nGET\r\n$7\r\nmissing\r\n
Server responds: $-1\r\n
```

## Project Structure

```
app/
├── server.py          # Main Redis server implementation
├── client.py          # Command-line client
├── resp.py            # RESP encoder/decoder
├── datastore.py       # Key-value storage with TTL
├── commands.py        # All commands i.e SET, GET
└── README.md
```

## Why This Project?

This project was built to explore and understand:

• **Redis Internals** - How Redis handles commands, storage, and client communications
• **Network Programming** - TCP socket programming and handling multiple client connections
• **Protocol Implementation** - Deep dive into the Redis Serialization Protocol (RESP)
• **Systems Design** - Building a concurrent server with proper resource management
• **Data Structures** - Implementing efficient key-value storage with expiration

Understanding these concepts provides valuable insights into database systems, caching mechanisms, and high-performance server architecture.

## Roadmap

### Phase 1 - Additional Basic Commands
• `DEL` - Delete keys
• `EXISTS` - Check if key exists
• `TTL` - Get remaining time to live
• `EXPIRE` - Set expiration on existing keys

### Phase 2 - Data Types
• `INCR`/`DECR` - Increment/decrement integers
• `APPEND` - Append to string values
• `STRLEN` - Get string length

### Phase 3 - Advanced Features
• List operations (`LPUSH`, `RPUSH`, `LPOP`, `RPOP`)
• Hash operations (`HSET`, `HGET`, `HDEL`)
• Set operations (`SADD`, `SREM`, `SMEMBERS`)

### Phase 4 - Performance & Persistence
• Persistence to disk
• Configuration file support
• Performance optimizations
• Memory usage statistics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Krutarth Patel 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

**Note:** This is an educational project and is not intended for production use. For production applications, please use the official Redis server.
