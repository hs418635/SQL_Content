import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'test'
)

cur = db.cursor()
updt = """update business set name= 'bhuvneshwar kumar ' where id=20"""

try:
    cur.execute(updt)
    db.commit()
    print("updated")
except:
    db.rollback()
    print("not updated")
db.close()