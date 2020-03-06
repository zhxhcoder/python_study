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
    cursor.execute(sql_insert, [name+name, mTime])
    # 提交到数据库执行
    conn.commit()
except:
    # 出现错误 就回滚
    conn.rollback()

# 读取数据库中的数据
sql_query = 'select * from users'
cursor.execute(sql_query)

# 查询所有数据，返回结果默认以元组形式，所以可以进行迭代处理
for i in cursor.fetchall():
    print(str(i[0]) + "-" + str(i[1]) + "-" + str(i[2]))
print('共查询到：', cursor.rowcount, '条数据。')

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
