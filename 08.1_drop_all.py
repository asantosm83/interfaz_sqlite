
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name_customer = 'customer'
table_name_cash_order = 'cash_order'
table_name_shipment = 'shipment'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

m.drop_table(table_name_customer)
m.drop_table(table_name_cash_order)
m.drop_table(table_name_shipment)
