
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name_customer = 'customer'
table_name_cash_order = 'cash_order'
table_name_shipment = 'shipment'

# File with data to insert 
file_customer = 'input_csv/customer.csv'
file_cash_order = 'input_csv/cash_order.csv'
file_shipment = 'input_csv/shipment.csv'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

# Insert from file
m.bulk_load_csv(table_name_customer, file_customer, header=None, delimiter=',')
m.bulk_load_csv(table_name_cash_order, file_cash_order, header=None, delimiter=',')
m.bulk_load_csv(table_name_shipment, file_shipment, header=None, delimiter=',')
