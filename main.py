from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine


conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)


#print(engine)
#print(type(engine))
#print(dir(engine))
#print(engine.table_names())


metadata = MetaData()

print(metadata)
print(dir(metadata))
print(metadata.tables) # przed odbiciem

artists = Table('artists', metadata, autoload=True, autoload_with=engine) # odbicie

print(artists)
print(repr(artists))
print(metadata.tables) # po odbiciu