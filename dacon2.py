import pymysql

# 建立数据库连接实例
db = pymysql.connect(user="root", password="123", host='localhost', database="mytest")
# 获取数据库实例的游标
cur = db.cursor()
# SQL语句
query_sql = "select * from mybook_tbl"
ins_sql = '''INSERT INTO mybook_tbl \
             (book_title, book_author, publish_date)\
             VALUES ("鬼吹灯", "无故天下", "2019-8-1")
'''
# 游标执行SQL语句, 插入记录
for i in range(10):
    cur.execute(ins_sql)

# 将插入的记录提交数据库, 记录正式生效
db.commit()

# 游标执行SQL语句查询，返回记录数量int
rs = cur.execute(query_sql)
print(rs)

# 利用查询结果（int），cur.fetchone 逐条输出数据库记录
for i in range(rs):
    print(cur.fetchone())
    print('*'*60)

# 程序结束，关闭数据库实例的游标
cur.close()

# 程序结束，关闭数据库实例连接
db.close()
