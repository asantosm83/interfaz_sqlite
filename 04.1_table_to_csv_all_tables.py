
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name_customer = 'customer'
table_name_cash_order = 'cash_order'
table_name_shipment = 'shipment'

# File with data to insert 
file_customer = 'output_csv/customer_out.csv'
file_cash_order = 'output_csv/cash_order_out.csv'
file_shipment = 'output_csv/shipment_out.csv'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

m.table_to_csv(table_name_customer,file_customer)
m.table_to_csv(table_name_cash_order,file_cash_order)
m.table_to_csv(table_name_shipment,file_shipment)
