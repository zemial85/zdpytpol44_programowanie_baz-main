# SELECT clause (raw sql)
from sqlalchemy import create_engine


conn_string = 'sqlite:///chinook.sqlite'
engine = create_engine(conn_string)

connection = engine.connect()

stmt = "SELECT * FROM artists"
result_proxy = connection.execute(stmt) # metoda execute zwraca ResultProxy
results = result_proxy.fetchall()

print(results)
print(type(results))

first_row = results[0]
print(first_row)
print(type(first_row))
print(dir(first_row))

print(first_row.keys())
print(first_row.values())
print(first_row.ArtistId)
print(first_row.Name)

#iterujemy po każdym wpisie
for item in results:
    print(item.Name)