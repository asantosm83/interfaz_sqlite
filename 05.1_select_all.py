
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'customer'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

# Print result
print(m.select(table_name))
