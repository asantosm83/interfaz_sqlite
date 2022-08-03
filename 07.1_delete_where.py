
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'cash_order'

# Where
where = 'CUSTOMER_ID=10006'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

m.delete(table_name=table_name, where=where)
