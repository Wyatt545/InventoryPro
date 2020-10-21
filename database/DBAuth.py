"""
	Created by Trenton Scott
	Created on 10.20.2020
	Purpose: 	The purpose of this class is to assist with database 
				interaction for authentication / registration 
"""

import sqlite3, random, hashlib
from database.DBHelper import DBHelper

class DBAuth:
	def __init__(self):
		self.db = DBHelper()

	def createUser(self, credentials):
		"""
			
			Created by Trenton D Scott
			Output: Boolean
			Description: Stores new user in the database. 
			Usage: DBHelper.createUser([username, password])
		
		"""

		CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		salt= ""
		for i in range(16):
			salt += random.choice(CHARS)
		
		encodedPass = (credentials[1] + salt).encode()
		sec_pass = hashlib.sha256(encodedPass)

		try:
			self.db.conn.execute("INSERT INTO Users (Username, Password, Salt) VALUES (?,?,?)", (credentials[0], str(sec_pass.hexdigest()), salt))
			self.db.conn.commit()
			return True
		except sqlite3.IntegrityError:
			return False
		
		self.db.disconnect()

	def authenticate(self, credentials):
		"""
			
			Created by Trenton D Scott
			Output: Boolean
			Description: Returns true on successful authentication 
			Usage: DBHelper.getUsernames()
		
		"""
		username = credentials[0]
		password = credentials[1]

		
		try: 
			try:
				self.db.curr.execute("SELECT Salt FROM Users WHERE Username=?", (username,))
				salt = self.db.curr.fetchone()[0]
				encodedPass = (password + salt).encode()
				testHash = hashlib.sha256(encodedPass).hexdigest()

				self.db.curr.execute("SELECT Password FROM Users WHERE Username=?", (username,))

				storedHash = self.db.curr.fetchone()[0]
			except:
				return False

			if (testHash == storedHash):
				return True
			else:
				return False

		except:
			print("Could not execute query on database. The database connection could be closed. ")

		self.db.disconnect()

	def getUsernameById(self, ID):
		"""
			
			Created by Trenton D Scott
			Output: String
			Description: Returns username from database based on ID. 
			Usage: DBHelper.getUserNameById(Integer)
		
		"""
		self.db.curr.execute("SELECT Username FROM Users WHERE ID=?", (ID,))
		try:
			return curr.fetchone()[0]
		except: 
			return "NoUserExists"
		
	def checkUserExists(self, username):
		"""
			
			Created by Trenton D Scott
			Output: String
			Description: Returns ID from database based on username. 
			Usage: DBHelper.getIdByUsername(String)
		
		"""
		
		try:
			self.db.curr.execute("SELECT * FROM Users WHERE UserName=?", (username,))
			if self.db.curr.rowcount < 1:
				return False
			else: 
				return True
		except Exception as err:
			print(err)

	