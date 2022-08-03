
import os
import sqlite3
import csv
from sqlite3 import Error
from pathlib import Path

class Interfaz_sqlite():
    '''
    Interfaz SQLite

    Interfaz SQLite is a python class for working with the SQLite3 database. 
    This class abstracts the basic functionalities of SQLite3, both for 
    database administration and data management, since in addition to being 
    able to easily create and delete tables, it also allows inserts, deletes 
    or bulk uploads of data through a csv file.

    31-07-2022 - asantosm83 - v0.0 - Initial version
    '''

    def __init__(self,pth_db: str):
        """Initialize Mgn_sqlite variables"""
        try:
            self.pth_db=pth_db
        except Error as e:
            print(e)
        except Exception as e:
            print(e)

    def create_table(self, table_name: str, fields: str):
        """Create a table if it does not exist already"""
        try:
            # -- Open connection -- 
            connection = sqlite3.connect(self.pth_db)
            cur = connection.cursor()

            # -- Execute SQL command --
            cur.execute('CREATE TABLE ' + table_name + ' (' + fields + ') ')
             
            # -- Close connection -- 
            connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)
    
    def create_table_ddl(self, file_ddl: str):
        """Create a table if it does not exist already"""
        try:
            # -- Open connection -- 
            connection = sqlite3.connect(self.pth_db)
            cur = connection.cursor()
            # -- Obtain table name -- 
            table_name = Path(file_ddl).stem

            # -- Obtain fields -- 
            fields = ""
            with open(file_ddl, 'r+') as file:
                n = 0
                for line in file:
                    if n==0:
                        fields += line
                    else:
                        fields += ',' + line
                    n += 1
        
            # -- Generate SQL command -- 
            sql_command = 'CREATE TABLE %s ( %s )'  % (table_name, fields)
            
            # -- Execute SQL command --
            cur.execute(sql_command)

            # -- Close connection -- 
            connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)    

    def drop_table(self, table_name):

        try:
            connection = sqlite3.connect(self.pth_db)
            cur = connection.cursor()
            cur.execute('DROP TABLE IF EXISTS ' + table_name)
            connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)
    
    def bulk_load_csv(self, table_name: str, file: str, header=None, delimiter=','):
        try:
            self.connection = sqlite3.connect(self.pth_db)
            self.cur = self.connection.cursor()
            
            with open(file,'r') as fin:
                # csv.DictReader uses first line in file for column headings by default
                dr = csv.DictReader(fin,fieldnames=header,delimiter=delimiter) # comma is default delimiter
                to_db = [tuple(i.values()) for i in dr]
                fields=','.join(dr.fieldnames)
                num_values = "?, " * (len(dr.fieldnames)-1)
                num_values += "?"

            self.cur.executemany("INSERT INTO %s (%s) VALUES (%s);" % (table_name, fields, num_values), to_db)

            self.connection.commit()
            self.connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)    
    
    def insert_new_row(self, table_name: str, new_row: dict):
        try:
            fields = []
            values = []
            for key in new_row:
                fields.append(key)
                values.append("\'" + str(new_row[key]) + "\'" )
  
            sql_command = "INSERT INTO %s ( %s ) VALUES ( %s );" % (table_name, ','.join(fields), ','.join(values))
            self.connection = sqlite3.connect(self.pth_db)
            self.cur = self.connection.cursor()
            self.cur.execute(sql_command)
            self.connection.commit()
            self.connection.close()

        except Error as e:
            print(e)
        except Exception as e:
            print(e)
    
    def table_to_csv(self, table_name: str, csv_file_name: str):
        try:
            sql_command = "SELECT * FROM %s;" % (table_name)
            self.connection = sqlite3.connect(self.pth_db)
            self.cur = self.connection.cursor()
            self.cur.execute(sql_command)
            with open(csv_file_name, 'w',newline='') as csv_file: 
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in self.cur.description]) 
                csv_writer.writerows(self.cur)
            self.connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)
    
    def select(self, table_name, columns=None, where=None):
        try:
            
            if columns==None:
                columns_to_select = '*'
            else:
                columns_to_select = ','.join(columns)

            if where==None:
                where_to_select = ""
            else:
                # where_to_select = 'WHERE ' + ' and '.join(where)
                where_to_select = 'WHERE ' + where

            
            sql_command = "SELECT %s FROM %s %s ;" % (columns_to_select, table_name, where_to_select)
            self.connection = sqlite3.connect(self.pth_db)
            self.cur = self.connection.cursor()
            self.cur.execute(sql_command)
            result = list(self.cur.fetchall())
            self.connection.close()
            return result
        except Error as e:
            print(e)
        except Exception as e:
            print(e)
    
    def delete_all(self, table_name):
        try:
            sql_command = "DELETE FROM %s ;" % (table_name)
            self.connection = sqlite3.connect(self.pth_db)
            self.cur = self.connection.cursor()
            self.cur.execute(sql_command)
            self.connection.commit()
            self.connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)
    
    def delete(self, table_name, where=None):
        try:
            if where==None:
                where_complete=''
            else:
                where_complete = 'WHERE ' + where
            
            sql_command = "DELETE FROM %s %s;" % (table_name, where_complete)
            self.connection = sqlite3.connect(self.pth_db)
            self.cur = self.connection.cursor()
            self.cur.execute(sql_command)
            self.connection.commit()
            self.connection.close()
        except Error as e:
            print(e)
        except Exception as e:
            print(e)




