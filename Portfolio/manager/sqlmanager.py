import sqlite3

#class for handling sql methods
class SQL:
    def __init__(self):
        try:
            self.__db_connection = sqlite3.connect("database.db")
        except sqlite3.Error as e:
            print(e)

    def __del__(self):
        try:
            self.__db_connection.commit()
        except sqlite3.Error as e:
            print(e)
        self.__db_connection.close()

    def execute(self, sql):
        try:
            self.__db_connection.execute(sql)
        except sqlite3.Error as e:
            print(e)
        del self

    def execute_return(self, sql):
        try:
            cursor = self.__db_connection.cursor()
            cursor.execute(sql)
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(e)
        del self

    def fetchone(self, sql):
        cursor = self.__db_connection.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
        except sqlite3.Error as e:
            result = None
            print(e)

        del self
        return result
    
    def fetchall(self, sql):
        cursor = self.__db_connection.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except sqlite3.Error as e:
            result = None
            print(e)

        del self
        return result
        
