import pymysql
db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'home' #mentioning database after creation
)
cur = db.cursor()
"""
# create database home
cd = '''create database home'''
cur.execute(cd)
db.close()



# Create table nrzb
ct = '''create table nrzb
        (city_id integer(10),
        city_name char(50),
        district char(50))'''

cur.execute(ct)
print("table created")
db.close() 

# insert values 
iv = '''insert into nrzb values
        (2,'shahdol','umaria'),
        (3,'katni','indore')'''
try:
    cur.execute(iv)
    db.commit()
    print("values are inserted")

except:
    db.rollback()
    print("values are not inserted")
db.close() 

# update table
up = '''update nrzb
        set district='katni'
        where city_id = 3'''
cur.execute(up)
db.commit()
print("values are updated")
db.close() 

#selecting the values from the table
sv = '''select * from nrzb'''
cur.execute(sv)
result=cur.fetchall()
print('the selected values are:',result)
db.close() 

#
dl = '''delete from nrzb where city_id = 3'''
cur.execute(dl)
db.commit()
db.close() """