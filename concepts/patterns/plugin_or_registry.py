class ConnectorRegistry:
    _connectors = {}

    @classmethod
    def register(cls, name, connector_class):
        cls._connectors[name] = connector_class

    @classmethod
    def create(cls, name, config):
        if name not in cls._connectors:
            raise ValueError(f"Unknown connector: {name}")
        return cls._connectors[name](config)


# Base connector interface
class BaseConnector:
    def __init__(self, config):
        self.config = config

    def connect(self):
        raise NotImplementedError


# Concrete implementations
class SQLConnector(BaseConnector):
    def connect(self):
        return f"Connected to SQL: {self.config['host']}"


class RedisConnector(BaseConnector):
    def connect(self):
        return f"Connected to Redis: {self.config['host']}"


# Registration
ConnectorRegistry.register('sql', SQLConnector)
ConnectorRegistry.register('redis', RedisConnector)

# Usage
connector = ConnectorRegistry.create('sql', {'host': 'localhost'})