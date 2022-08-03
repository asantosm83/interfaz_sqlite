
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'customer'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

# Create a new row
new_row_customer = {
  "CUSTOMER_ID":     10000,
  "CUSTOMER_NAME":   "James Rother"
}

# Insert new row
m.insert_new_row(table_name, new_row_customer)
