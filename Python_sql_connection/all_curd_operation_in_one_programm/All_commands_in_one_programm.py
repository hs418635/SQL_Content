
''' Database Creation '''

import pymysql
db=pymysql.connect(
    host='localhost',
    user = 'root',
    password = '1234',
    database = 'himani' #using himani as database to run the update command 
)
cur = db.cursor()
"""
cdatbase = '''create database himani'''
cur.execute(cdatbase)
print("Database created")
db.close  

#creating_table

import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'himani'
)
cur = db.cursor()
ct = '''create table company
        (prd_id integer(20),
        prd_name char(50),
        price char(20))'''
cur.execute(ct)
print("Table created")
db.close() 

#inserting values into the table

import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'himani'
)

cur = db.cursor()
insert = '''insert into company values
            (1,'charger','rs20'),
            (2,'mobile','rs50')'''
try:
    cur.execute(insert)
    db.commit()
    print("values inserted")
except:
    db.rollback()
    print("values are not inserted")
db.close() 

#updating the table

update = '''update company set price='rs100' where prd_id = 2'''
cur.execute(update)
db.commit()
print("updated")
db.close() 

#selecting the values
sel = '''select * from company'''
cur.execute(sel)
result=cur.fetchall()
print("the selected values are \n",result)
db.close()
"""
delete = '''delete from company where prd_id=2'''
cur.execute(delete)
db.commit()
print("deleted")
db.close()
