class DatabaseConnection:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.connection_string = "localhost:5432"
            self.connected = False
            self._initialized = True

    def connect(self):
        if not self.connected:
            print(f"Connecting to database at {self.connection_string}")
            self.connected = True
        return "Connected"


# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance? {db1 is db2}")  # True
db1.connect()
