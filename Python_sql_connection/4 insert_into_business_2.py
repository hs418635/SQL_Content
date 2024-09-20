import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'test'
)
cur = db.cursor()
values = """insert into business values
        (10,"sikhar",50,"punjab",825635),
        (20,"pawan",60,"kkr",524524)"""

try:
    cur.execute(values)
    db.commit()
    print("values are inserted")

except:
      db.rollback()
      print("values are not inserted")

db.close()