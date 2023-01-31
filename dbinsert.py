# 数据库表 sales_analysis_tbl创建后，将excel数据导入MySql数据库表
# 2023-1-30 by thomas

import pymysql
import xlrd
# import pandas as pd
# from sqlalchemy import create_engine

# 创建数据库连接
conn = pymysql.connect(user="root", password="123", host='localhost', database="mytest")
cur = conn.cursor()
# filepath = "D:\华腾售前支持部门\战略规划\区域商机看板模板 v1.1.xlsx"
filepath2 = "D:\华腾售前支持部门\战略规划\区域商机看板模板.xls"
# engine = create_engine('mysql+pymysql://root:123@localhost/mytest?charset=utf8')
# data = pd.read_excel(filepath)

# 打开excel表
data2 = xlrd.open_workbook(filepath2)
# 读取excel表的数据，index(0)代表sheet1
sheet = data2.sheet_by_index(0)
# values变量声明
values = ()
# 插表sql语句
query = "insert into sales_analysis_tbl (region,province,custName,saleName,firstIndex," \
        "secondIndex,indexDate,indexMonth,isNewtheMoth,indexName,curStage,commuNum,winRate,bidResult," \
        "bidFlag,bidAmount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# print('导入记录共有'+str(sheet.nrows)+'行！')

delquery = "delete from sales_analysis_tbl"
# 插表之前先将表中的数据全部清除
cur.execute(delquery)
print('插表之前，表中数据已全部清理！')

# 依次读取excel表sheet1的数据记录，并插入数据库
for r in range(1, sheet.nrows):         # 从第二条数据开始读取，因为第一条为表头（即第0行）
    region = sheet.cell(r, 0).value     # sheet.cell(r,0), r为行，0代表第1个字段
    province = sheet.cell(r, 1).value
    custName = sheet.cell(r, 2).value
    saleName = sheet.cell(r, 3).value
    firstIndex = sheet.cell(r, 4).value
    secondIndex = sheet.cell(r, 5).value
    indexDate = sheet.cell(r, 6).value
    indexMonth = sheet.cell(r, 7).value
    isNewtheMoth = sheet.cell(r, 8).value
    indexName = sheet.cell(r, 9).value
    curStage = sheet.cell(r, 10).value
    commuNum = sheet.cell(r, 11).value
    winRate = sheet.cell(r, 12).value
    bidResult = sheet.cell(r, 13).value
    bidFlag = sheet.cell(r, 14).value
    bidAmount = sheet.cell(r, 15).value
    values = (region, province, custName, saleName, firstIndex, secondIndex, indexDate, indexMonth,
              isNewtheMoth, indexName, curStage, commuNum, winRate, bidResult, bidFlag, bidAmount)
    print(values)
    # 执行sql语句，将读取的excel行数据，插入库表
    cur.execute(query, values)

print('导入数据库成功！')

# 数据库数据，正式提交
conn.commit()
# 关闭游标
cur.close()
# 关闭数据库连接
conn.close()

# 最后打印
colums = str(sheet.ncols)
rows = str(sheet.nrows)
print("导入"+colums+"列"+rows+"行，到mysql数据库")




