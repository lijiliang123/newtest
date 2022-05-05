import pymysql

"""
   启动mysql服务: net start mysql
   关闭mysql服务: net stop mysql
   mysql登陆:    mysql -u root -p  (输入管理员密码)
   查看数据库：   show databases;
   打开库表：     use xxx(database name); 
   查看库表：     show tables;
   查看库表结构：  desc xxx(table name);
"""

# 建立数据库连接实例
db = pymysql.connect(user="root", password="123", host='localhost', database="mytest")
# 获取数据库实例的游标
cur = db.cursor()

# SQL语句
query_sql = "select * from mybook_tbl"
ins_sql = '''INSERT INTO mybook_tbl \
             (book_title, book_author, publish_date)\
             VALUES ("天下无贼", "刘德华", "2022-5-5")
'''

"""
创建表语句
crt_sql ='''CREATE TABLE person_salary_tbl (
   id INT,
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   INCOME FLOAT )'''

cur.execute(crt_sql)
"""

# 游标执行SQL语句, 插入记录
for i in range(50):
    cur.execute(ins_sql)

# 将插入的记录提交数据库, 记录正式生效
db.commit()

# 游标执行SQL语句查询，返回记录数量int
rs = cur.execute(query_sql)
print('总记录数：', rs, '条')

# 利用查询结果（int），cur.fetchone 逐条输出数据库记录
for i in range(rs):
    print(cur.fetchone())
    print('*' * 50)

# 程序结束，关闭数据库实例的游标
cur.close()

# 程序结束，关闭数据库实例连接
db.close()
