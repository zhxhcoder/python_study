# 导入数据库驱动
import sqlite3

# 连接到数据库
# 数据库文件是“sqlite_tst.db”
# 如果数据库不存在的话，将会自动创建一个 数据库
conn = sqlite3.connect("sqlite_tst.db")

# 创建一个游标 cursor
cursor = conn.cursor()

# 执行一条语句,创建 user表
# sql = "create table login (id varchar(20) primary key, name varchar(30), password varchar(30))"
# cursor.execute(sql)


# 插入一条记录
sql = "insert into login (name, password) values ('hehe', '222222')"
cursor.execute(sql)


# 查询一条记录：
sql = "select * from login"
cursor.execute(sql)
# sql = "select * from login where id=?"
# cursor.execute(sql, ("2",))


# 获取查询结果：
values = cursor.fetchall()
print(values)


# 通过rowcount获得插入的行数:
# cursor.rowcount()

# 关闭游标：
cursor.close()

# 提交事物
conn.commit()

# 关闭连接
conn.close()
