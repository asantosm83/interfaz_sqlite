
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'cash_order'

# Columns for select
columns = None

# Conditions for where
where = 'DATE=20220730'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

print(m.select(table_name=table_name,columns=columns,where=where))