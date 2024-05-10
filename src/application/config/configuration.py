from config.db_configuration import DBConfiguration

def db_config():
    return DBConfiguration("localhost", "postgres", "12345", "money_tracker")
