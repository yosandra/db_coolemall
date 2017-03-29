#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the version 3 of the GNU Lesser General Public License
#   as published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Copyright (c) NEC Deutschland GmbH, NEC HPC Europe
#
# $Id: mysql_database.py 516 2013-02-11 16:31:05Z $

import MySQLdb
import os
from direct_rpc_server import DirectRPCServer

# Constants
DB_DEFAULT = "coolemalldb"
DB_USER = "coolemall"
DB_PASSWORD = "coolemall"
DB_HOST = "localhost"

__all__ = [ "MysqlDatabase" ]

class LocalRemoteServer():
    """
    Helper class for the direct rpc server, providing remote access to the database.
    """
    def __init__( self, name ):
        self.name = name
        DirectRPCServer.register_rpc( name, self.server )

    def server( self, *args, **kwds ):
		return MysqlDatabase.localremotes[self.name].local_or_remote( *args, **kwds )

    def local_or_remote( self, *args, **kwds ):		
		db = MysqlDatabase( DB_HOST, DB_USER, DB_PASSWORD, DB_DEFAULT )
		return eval( "db.local_%s( *args, **kwds )" % self.name )        

class MysqlDatabase:

	localremotes = {}

	def __init__(self, host, username, password, database):
		self.host = host
		self.db = MySQLdb.connect(host=host, user=username, passwd=password, db=database)
		self.cursor = self.db.cursor()
		
	def query(self, sql):		
		return self.cursor.execute(sql)		
	
	def execute (self, sql):
		self.query(sql)
		return self
	
	def get_array (self, sql):
		self.cursor.execute (sql)
		result = self.cursor.fetchall()
		results = []
		for record in result:
			results.append(record)
		return results

	def __registerServers( self ):
		self.localremotes = {}

	def stopDB(self):
		self.db.commit()
		self.db.close()

	def str(self, v):
		"""Converts a Python variable into SQL string to insert it in a query."""
		if v is None:
			return "NULL"
		elif type(v)==type(str()):
			return "\""+self.db.escape_string(v)+"\""
		else:
			return str(v)
	
	def insert(self,sql):		
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except:
			self.db.rollback()
			
	def create_db(self, hostname, username, password, path_sql_file):
		command = "mysql -h %s -u %s -p%s < %s " % (hostname, username, password, path_sql_file)
		try:
			os.system(command)
		except:
			print "Error during database creation"
	
	###########################################################################
	#  Functions to included metric
	###########################################################################
	def addMetric(self, arg):
		
		sql = """INSERT INTO `metric` """		
		sql += "SET "+", ".join(["`%s`=%s" % (key, self.str(value)) for key, value in arg.items()])
		
		#print "Sentencia: "+sql
		self.insert (sql)
		
		
	###########################################################################
   	# Stuff below is the local and remote API
   	###########################################################################
	def local_getRecordsByMetricName(self, host_name, metric_name):
		""" 
		Return a list that contains records.
		Each record has two attributes time_ns (time in 10E-9 seconds) and value.		
		"""
		records = []
		#Prepare SQL query
		sql = """SELECT time, value FROM `metric` WHERE host = '%s' && name = '%s'""" % (host_name, metric_name)		
		records = self.get_array(sql)
		return records
	
	def local_getMetricNames(self, host_name):
		"""Look all metric names up for a particular host name.
		@param host_name:string specifying host name
		@return: list containing available metric names as string 
		"""
		hostnames = []
		#Prepare SQL query
		sql = """SELECT name FROM `metric` WHERE host = '%s' """ % (host_name)		
		hostnames = self.get_array(sql)		
		return hostnames			
	
	def local_getHostNames(self):
		""" """
		hosts = []
		#Prepare SQL query
		sql = """SELECT DISTINCT host FROM `metric` """
		hosts = self.get_array(sql)		
		return hosts
		
	def local_getLastMetricByHostName(self, host_name):
		metrics = []
		#Prepare SQL query
		sql = """SELECT * FROM `metric` WHERE host = '%s'  ORDER BY Id DESC LIMIT 0 , 1 """ % (host_name)		
		metrics = self.get_array(sql)
		return metrics
		

####################################################################################
# Magic for registering direct rpc servers for each function that starts with local_
####################################################################################
for m in dir( MysqlDatabase ):
    if m.startswith( "local_" ) and eval( "callable( MysqlDatabase.%s )" % m ):
        name = m.lstrip( "local_" )
        MysqlDatabase.localremotes[name] = LocalRemoteServer( name )
        exec( "MysqlDatabase.%s = staticmethod(MysqlDatabase.localremotes[name].local_or_remote)" % name )
			