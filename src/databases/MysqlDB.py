#!/usr/bin/python
import MySQLdb

class MysqlDB:
	def __init__(self, host, username, password, database):
        self.host = host
        self.db = MySQLdb.connect(host=host, user=username, passwd=password, db=database)
        self.cursor = self.db.cursor()

	def query(self, sql):
        return self.cursor.execute(sql)
    
    	def execute(self, sql):
        self.query(sql)
        return self
	
	def get_array(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        results = []
        for record in result:
            results.append(record)
        return results

class Database():
	def create_db( self, sql_file ):
