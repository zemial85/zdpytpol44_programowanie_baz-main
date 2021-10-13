from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

connection = engine.connect()

metadata = MetaData()
artists = Table('artists', metadata, autoload=True, autoload_with=engine)

stmt = select([artists])
print(stmt)

results = connection.execute(stmt).fetchall()
print(results)