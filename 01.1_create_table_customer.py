
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'customer'

# A string of characters separated by commas
fields = 'CUSTOMER_ID INTEGER NOT NULL, CUSTOMER_NAME TEXT NOT NULL, PRIMARY KEY (CUSTOMER_ID)'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

# Drop table (if it exits)
m.drop_table(table_name)

# # Create a new table. 
m.create_table(table_name, fields)
