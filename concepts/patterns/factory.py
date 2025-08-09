class DatabaseFactory:
    @staticmethod
    def create_connection(db_type, connection_string):
        if db_type == 'postgresql':
            return PostgreSQLConnection(connection_string)
        elif db_type == 'mysql':
            return MySQLConnection(connection_string)
        elif db_type == 'mongodb':
            return MongoConnection(connection_string)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")


# Client code doesn't need to know about specific classes
db = DatabaseFactory.create_connection('postgresql', 'postgres://...')
