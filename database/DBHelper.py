"""
	Created by Trenton Scott
	Created on 10.20.2020
	Purpose: The purpose of this class is to assist with database interaction 
"""

import sqlite3, random, hashlib

class DBHelper:
	global conn
	global curr 
	global keepConnOpen
	
	def __init__(self, active = False):
		"""
			
			Created by Trenton D Scott
			Output: N/A
			Description: Initializes DBHelper
			Usage: DBHelper(active)
				active	--	if True the database connection will stay open until
							closed. If false, the database connection will close 
							after 1 transaction. 
		
		"""
	
		try:
			self.db_connect()
		except sqlite3.Error:
			#if the above throws an error, the table does not exist and will be created. 
			#this should only occurs during initial setup. 
			print("Error connecting to DB. ")

		global conn, curr
		self.conn = conn
		self.curr = curr
				
		global keepConnOpen
		keepConnOpen = active
		
		
	def db_connect(self):
		"""
			
			Created by Trenton D Scott
			Output: N/A
			Description: Connected to database
			Usage: This function should only be called by 
		"""
		#connect to the database. 
		try:
			global conn
			conn = sqlite3.connect('database/database.db')
		except:
			print("An error was encountered while trying to connect to the database. ")
		global curr
		curr = conn.cursor()	
			
	def dump_table(self):
		"""
			
			Created by Trenton D Scott
			Output: List [String, ...]
			Description: Returns username from database based on ID. 
			Usage: DBHelper.getUsernames()
		
		"""
		curr.execute("SELECT * from Users")
		data = curr.fetchall()
		print(data)
		
	def disconnect(self):
		conn.close()