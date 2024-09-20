import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'test'
)
cur = db.cursor()
cur.execute("drop table if exists business")

create_table ="""create table business
                (id integer(10),
                name char(50),
                age char(3),
                city char(10),
                phone_num integer(10))"""

cur.execute(create_table)
print("Table created")
db.close()