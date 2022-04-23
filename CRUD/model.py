import mysql.connector as mysql 

class Model:
	def __init__(self):
		self.db = mysql.connect(
			host="127.0.0.1",
			user="root",
			password="",
			database="flaskdb_178"
			)
		self.cursor = self.db.cursor()

	def read(self):
		self.cursor.execute("SELECT * FROM `player_178`;")
		self.show = self.cursor.fetchall()
		return self.show

	def create(self, ID_178, Name_178, Level_178, Classes_178, Build_178, Bio_178):
		self.cursor.execute("INSERT INTO `player_178` VALUES (%s, %s, %s, %s, %s, %s);",(ID_178, Name_178, Level_178, Classes_178, Build_178, Bio_178, ))
		return self.db.commit()
	
	def update(self, ID_178, Name_178, Level_178, Classes_178, Build_178, Bio_178):
		self.cursor.execute("UPDATE `player_178` SET Name_178=%s, Level_178=%s, Classes_178=%s, Build_178=%s, Bio_178=%s WHERE ID_178=%s;",(Name_178, Level_178, Classes_178, Build_178, Bio_178, ID_178, ))
		return self.db.commit()
	
	def delete(self, ID_178):
		self.cursor.execute("DELETE FROM `player_178` WHERE ID_178=%s;", (ID_178, ))
		return self.db.commit()

