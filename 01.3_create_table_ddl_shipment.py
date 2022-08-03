
from interfaz_sqlite import Interfaz_sqlite

# Database
database = 'db_test.sqlite'

# Table name
table_name = 'shipment'

# file with ddl
file_ddl = 'ddlite/shipment.ddlite'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)

# Drop table (if it exits)
m.drop_table(table_name)

# Create a new table. The table defition must be included in file sales.ddlite.
m.create_table_ddl(file_ddl)
