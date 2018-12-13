import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="xzq",
    passwd="123456",
    database="xzq_test"
)
mycursor=mydb.cursor()
# mycursor.execute("create database xzq_test")
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
# mycursor.execute("create table sites (name VARCHAR(255),url varchar(255)) ")
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# mycursor.execute("alter table sites add column id int auto_increment primary key ")

# sql="insert into sites (name,url) values (%s,%s)"
# val=("zhihu","www.zhihu.com")
# mycursor.execute(sql,val)
# val=[("xzq","www.baidu.com"),("shuyi","www.google.com"),("taobao","www.taobao.com")]
# mycursor.executemany(sql,val)

# mydb.commit()
# print("1条记录插入成功，ID：",mycursor.lastrowid)

mycursor.execute("select * from sites")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)