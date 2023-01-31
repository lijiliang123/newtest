# 创建数据库表 sales_analysis_tbl

import pymysql

"""
   启动mysql服务: net start mysql
   关闭mysql服务: net stop mysql
   mysql登陆:    mysql -u root -p  (在mysql\bin目录下运行，输入管理员密码)
   查看数据库：   show databases;
   打开库表：     use xxx(database name); 
   查看库表：     show tables;
   查看库表结构：  desc xxx(table name);
   python data migrate to this new computer on 2022-9-8
"""

# 建立数据库连接实例
db = pymysql.connect(user="root", password="123", host='localhost', database="mytest")
# 获取数据库实例的游标
cur = db.cursor()

# SQL语句
query_sql = "select * from mybook_tbl"
count_sql = "select count(*) from mybook_tbl"
ins_sql = '''INSERT INTO mybook_tbl \
             (book_title, book_author, publish_date)\
             VALUES ("风雨无阻", "刘德华", "2022-9-7")
'''

create_sql = '''
CREATE TABLE IF NOT EXISTS `sales_analysis_tbl` (
  `id` BIGINT NOT NULL AUTO_INCREMENT  COMMENT 'ID',
  `region` VARCHAR(30) COMMENT '所属区域',
  `province` VARCHAR(10) COMMENT '所属省市',
  `custName` VARCHAR(30) COMMENT '客户名称',
  `saleName` VARCHAR(15) COMMENT '销售人员',
  `firstIndex` VARCHAR(25) COMMENT '一级线索',
  `secondIndex` VARCHAR(25) COMMENT '二级线索',
  `indexDate` DATE  COMMENT '线索日期',
  `indexMonth` INT COMMENT '线索月份',
  `isNewtheMoth` VARCHAR(10) COMMENT '是否当月新增',
  `indexName`  VARCHAR(30) COMMENT '线索名称',
  `curStage`  VARCHAR(30) COMMENT '目前阶段',
  `commuNum` INT COMMENT '交流次数',
  `winRate` FLOAT COMMENT '赢单率',
  `bidResult` VARCHAR(10) COMMENT '中标结果',
  `bidFlag` INT COMMENT '中标标识',
  `bidAmount` FLOAT COMMENT '中标金额',
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4
'''

cur.execute("DROP TABLE IF EXISTS sales_analysis_tbl")
cur.execute(create_sql)

# 将插入的记录提交数据库, 记录正式生效
db.commit()

# 程序结束，关闭数据库实例的游标
cur.close()

# 程序结束，关闭数据库实例连接
db.close()


