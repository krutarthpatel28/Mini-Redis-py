from datetime import datetime, timedelta

class DataStore:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, expiry_seconds: int | None = None):
        expiry = None
        if expiry_seconds:
            expiry = datetime.now() + timedelta(seconds=expiry_seconds)
        self.store[key] = (value, expiry)

    def get(self, key: str):
        entry = self.store.get(key)
        if not entry:
            return None
        value, expiry = entry
        if expiry and datetime.now() > expiry:
            del self.store[key]
            return None
        return value
