import pymysql

db=pymysql.connect(host='localhost',user='root',password='1234',database='test')#server,username,pass,database

cur=db.cursor()

sql="""SELECT * FROM business"""

try:
    cur.execute(sql)
    result=cur.fetchall()
    print("selected values are",result)
except:
    print("values not selected")
db.close()