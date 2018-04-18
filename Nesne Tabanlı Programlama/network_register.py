
import pymysql

db = pymysql.connect("localhost","root","temp.35411","ceng302_hw2")

cursor = db.cursor()

cursor.execute("select * from PRODUCT")
data = cursor.fetchone()

cursor.execute("update PRODUCT set description='CCCBBB' where product_ID=1001 ")
db.commit()
print(data)

db.close()
