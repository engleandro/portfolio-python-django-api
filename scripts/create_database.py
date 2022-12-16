import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def set_db_url(
    username: str,
    password: str,
    database: str = None,
    rdbms: str = "postgresql",
    hostname: str = "localhost",
    port: int = 5432,
):
    if not database:
        return f"{rdbms}://{username}:{password}@{hostname}:{port}"
    return f"{rdbms}://{username}:{password}@{hostname}:{port}/{database}"


db_url = set_db_url(
    username=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    rdbms=os.getenv("DATABASE_RDBMS"),
    hostname=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT", 5432),
)

print("running create_database.py")

connection = psycopg.connect(db_url, autocommit=True)
with connection.cursor() as cursor:
    sql = (
        f"SELECT 'CREATE DATABASE {os.getenv('DATABASE_NAME')}' "
        f"WHERE NOT EXISTS ( "
        f"SELECT * FROM pg_database WHERE datname='{os.getenv('DATABASE_NAME')}' );"
    )
    cursor.execute(sql)
    connection.commit()
connection.close()

print("create_database.py finished")
