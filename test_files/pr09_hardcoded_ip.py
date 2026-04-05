DATABASE_HOST = "192.168.1.100"
DATABASE_PORT = 5432
SECRET_TOKEN = "my-super-secret-token-12345"

def connect():
    return connect_db(DATABASE_HOST, DATABASE_PORT)