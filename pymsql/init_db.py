# python + pymysql 创建数据库
import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='db_name', charset='UTF8MB4')
# 创建游标
cursor = conn.cursor()

# 创建数据库的sql(如果数据库存在就不创建，防止异常)
sql_1 = "CREATE DATABASE IF NOT EXISTS db_name"
# 执行创建数据库的sql
cursor.execute(sql_1)

sql_2 = """drop table if exists employee;"""
cursor.execute(sql_2)

# 创建表
sql_3 = '''CREATE TABLE `employee`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `topic` INT ,
  `ptid` INT NOT NULL,
  `level` INT NOT NULL,
  `time` TIME,
  `consume` INT NOT NULL,
  `err` INT NOT NULL,
  `points` INT NOT NULL,
  `gid` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
cursor.execute(sql_3)
