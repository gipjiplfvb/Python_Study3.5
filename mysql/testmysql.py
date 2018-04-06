import pymysql

db = pymysql.connect("localhost", "root", "1.2.3.", "test1")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s" % data)
db.close()

