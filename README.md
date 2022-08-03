# Interfaz Sqlite
## _Una interfaz sencilla para trabajar con SQLite_

Interfaz SQLite permite abstraer el manejo de SQLite3 de manera sencilla, permitiendo acciones simples tanto de administración de base de datos (create table, drop table, ...) como consultas (select) o manejo de datos (insert, delete ...).

A través de los métodos que componen la clase se puede realizar las acciones comunes de base de datos sin tener en cuenta la conexión, cerrar la sesión o el cursor, ya que los métodos están preparados para acciones concretas. Además, no será necesario instalar ninguna otra clase adicional de python para que funciona correctamente. 

A través de ejemplos sencillos se mostrará el funcionamiento de esta clase que puede integrar en cualquier proyecto de Python. 

## Versión
| Versión | Fec. Publicación | Descripción |
| ------ | ------ | ------ |
| v1.0 | 03 - Agosto - 2022 | Versión inicial

## Cómo funciona

Simplemente importando la clase podemos ya hacer uso de ella. En el siguiente ejemplo, para el siguiente ejemplo, se ha creado un fichero llamada db_test.sqlite que será el fichero de base de datos. 

```python
from interfaz_sqlite import Interfaz_sqlite


# Database
database = 'db_test.sqlite'

# Create a data base, if not exists. 
m = Interfaz_sqlite(database)
```

## Ejemplos 

A partir de los ejemplos creados se pueden ir revisando el funcionamiento de la clase. Estos ejemplos están preparados para ir funcionando el orden, desde el primero 01.1 hasta el último 08.1. Por lo que se recomienda ir ejecutando los ejemplos uno a uno e ir revisando los resultados para comprender el funcionamiento. 

Estos se ejemplos se basan en un pequeño modelo compuesto por tres tablas: customer, order y shipment. Donde se van creando las tablas, a continuación se cargan, luego de borran y finalmente se eliminan de la base de datos. 


## Inventario de ficheros

 - interfaz_sqlite.py: Clase para el manejo de SQLite3. 
 - 01.1_create_table_customer.py: Ejemplo para crear una nueva tabla.
 - 01.2_create_table_ddl_cash_order.py: Ejemplo para crear una tabla a partir de un fichero con su definición.
 - 01.3_create_table_ddl_shipment.py: Otro emeplo para crear una tabla a partir de un fichero con su definición. 
 - 02.1_insert_new_row_customer.py: Ejemplo para insertar un nuevo registros en una tabla.
 - 03.1_bulk_load_all_tables.py: Ejemplo para la carga de registros contenidos en un fichero.
 - 04.1_table_to_csv_all_tables.py: Ejemplo para descargar tablas en un fichero. 
 - 05.1_select_all.py: Ejemplo para hacer un select sencillo, seleccionando todas las columnas de la tabla.
 - 05.2_select_by_columns.py: Ejemplo de select, seleccionando un subconjunto de columnas de una tabla. 
 - 06.1_select_with_where.py: Ejemplo de select, aplicando condiciones para la selección de registros (where).
 - 07.1_delete_where.py: Ejemplo de borrado (delete) aplicando condiciones para la selección de los registros a eliminar.
 - 07.2_delete_all.py: Ejemplo de borrado completo de tablas.
 - 08.1_drop_all.py: Eliminar tablas.
 - customer_order_shipment.pdf: Modelo de datos para estos ejemplos.
 - db_test.sqlite: Base de datos que contiene las tablas con la información.
 - cash_order.ddlite: DDL de la tabla cash_order.
 - customer.ddlite: DDL de la tabla customer.
 - shipment.ddlite: DDL de la tabla shipment.
 
## Lista de métodos

| Método | Descripción | Salida |
| ------ | ------ | ------ |
| create_table(table_name: str, fields: str) | Crea una tabla a partir de los campos indicados en el parámetro fields | Sin valor de retorno |
| create_table_ddl(file_ddl: str) | Crea una tabla a partir de un fichero con la definición de la tabla | Sin valor de retorno |
| drop_table(table_name: str) | Borra la tabla indicada | Sin valor de retorno |
| bulk_load_csv(table_name: str, file: str, header=None, delimiter=',') | Carga los registros de un fichero en una tabla. Si el parámetro header se deja a None, entonces tienen en cuenta que la primera línea del fichero contiene la cabecera. En caso contrario, se le puede pasar la cabecera como una tupla con los nombres de los campos. El delimitador, por defecto es la coma, pero se puede usar cualquier caracter.  | Sin valor de retorno |
| insert_new_row(table_name: str, new_row: dict) | Carga en la tabla indicada el registro pasado como parámetro | Sin valor de retorno |
| table_to_csv(table_name: str, csv_file_name: str) | Vuelca en un fichero el contenido de una tabla | Sin valor de retorno |
| select(table_name, columns=None, where=None) | Selecciona los registros de una tabla. Se puede seleccionar la columnas de la tabla y filtrar la salida | Devuelve una lista con el resultado |
| delete_all(table_name) | Elimina el contenido completo de una tabla | Sin valor de retorno |
| delete(table_name, where=None) | Elimina el contenido de una tabla, según las condiciones del parámetro where | Sin valor de retorno |

## Próximo pasos

## Licencia

Free Software, Hell Yeah!
