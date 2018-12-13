import pymysql
db=pymysql.connect("localhost","xzq","123456","xzq_test")

cursor=db.cursor()
# cursor.execute("select version()")
# data=cursor.fetchone()
# print("database version:%s" %data)
# db.close()

# cursor.execute("drop table if exists sites")
# sql="create table emp(first_name char(20) not null ,last_name char(20),age int,sex char(1),income float)"
# sql="""insert into emp(first_name,last_name,age,sex,income) values ("mac","mohan","20","M",2000)"""
# sql="update emp set age=age+1 where sex='%c' "%('M')
sql="delete from emp where age>%s"%(20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

# sql="select * from emp where income>%s"%(1000)
#
# try:
#     cursor.execute(sql)
#     results=cursor.fetchall()
#     for row in results:
#         fname=row[0]
#         lname=row[1]
#         age=row[2]
#         sex=row[3]
#         income=row[4]
#         print("fname=%s,lname=%s,age=%s,sex=%s,income=%s"%(fname,lname,age,sex,income))
# except:
#     print("error:unable to fetch data")
#
# db.close()