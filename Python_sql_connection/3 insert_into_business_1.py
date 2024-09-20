import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'test'
)

cur = db.cursor()

insert_business = """insert into business
                    values
                    (1,'virat',26,'banglore',123456),
                     (2,'rohit',40,'mumbai',4251635)"""

try:
    cur.execute(insert_business)
    db.commit()
    print("values are inserted")

except:
    db.rollback()
    print('values are not inserted')

db.close()