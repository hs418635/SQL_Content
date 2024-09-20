import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'test'
)

cur = db.cursor()
cur.execute("drop table if exists office")
create_table ="""create table office
                (first_name char(50),
                last_name char(50),
                emp_id integer(10),
                age char(3),
                address char(30))"""

cur.execute(create_table)
print("table created")
db.close()