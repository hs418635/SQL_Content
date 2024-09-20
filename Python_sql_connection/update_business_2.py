import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'test'
)

cur = db.cursor()
upt = """update business set age=30 where id=20"""

try:
    cur.execute(upt)
    db.commit()
    print("updated")
except:
    db.rollback("not updated")
db.close()