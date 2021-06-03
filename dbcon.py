import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "thomas_ljl", "tt", charset='utf8')
#                     主机名称      用户名    用户密码   数据库名称
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# 批量插入数据库记录，一次性提交commit
number = 100      #插入库表的批量记录数
for i in range(number):
    numtoStr = str(i)
    sql = """INSERT INTO classinfo (className, classAddress, \
                       classMajor, studentCount, schCode)  \
      VALUES ('一年级五班', '北主楼105教室', '李子菊', '42', 'XUJINGXX')\
      """
    cursor.execute(sql)
'''
    sql = """INSERT INTO classinfo (classId, className, classAddress, \
                       classMajor, studentCount, schCode)  \
      VALUES ('10006', '一年级五班', '北主楼105教室', '马三四', '42', 'XUJINGXX')\
      """
'''

#cursor.execute("select * from classinfo")

#insert into表后，要执行commit，才能正式写入数据库
db.commit()

# 使用 fetchone() 方法获取一条数据
#data = cursor.fetchone()
data = cursor.fetchall()

for entry in data:
    print(entry)

#print(data[0])

#print('班级编号：', data[0])

# 关闭数据库连接
db.close()
