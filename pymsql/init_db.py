import time

import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='db_zhu', charset='UTF8MB4')
# 创建游标
cursor = conn.cursor()

# 执行创建数据库的sql
# cursor.execute('drop table if exists users;')
# 创建表
# sql_create_table = '''CREATE TABLE `users`(
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `name` CHAR(10) ,
#   `time` TIME,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;
# '''
# cursor.execute(sql_create_table)

name = "dudu"
mTime = time.strftime("%Y-%m-%d %H:%M:%S")

sql_insert = "INSERT INTO users(name, time) VALUES (%s, %s);"

try:
    # 执行sql语句
    cursor.execute(sql_insert, [name, mTime])
    # 提交到数据库执行
    conn.commit()
except:
    # 出现错误 就回滚
    conn.rollback()

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
