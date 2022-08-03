
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'customer'

# Columns for select
columns = ['CUSTOMER_ID','CUSTOMER_NAME']

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

print(m.select(table_name=table_name,columns=columns))