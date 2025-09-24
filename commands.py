from resp import RESPEncoder
from datastore import DataStore

encoder = RESPEncoder()
store = DataStore()

COMMANDS = {}

def command(name):
    def wrapper(fn):
        COMMANDS[name] = fn
        return fn
    return wrapper

@command("PING")
def handle_ping(args, conn):
    conn.send(encoder.encode_simple_string("PONG"))

@command("SET")
def handle_set(args, conn):
    if len(args) < 2:
        conn.send(encoder.encode_error("ERR wrong number of arguments for 'SET'"))
        return

    key, value = args[0], args[1]
    expiry = None

    if len(args) >= 4 and args[2].upper() == "EX":
        try:
            expiry = int(args[3])
        except ValueError:
            conn.send(encoder.encode_error("ERR invalid expire time"))
            return

    store.set(key, value, expiry)
    conn.send(encoder.encode_simple_string("OK"))

@command("GET")
def handle_get(args, conn):
    if len(args) < 1:
        conn.send(encoder.encode_error("ERR wrong number of arguments for 'GET'"))
        return

    key = args[0]
    value = store.get(key)
    conn.send(encoder.encode_bulk_string(value))
