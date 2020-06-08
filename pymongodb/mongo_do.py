import pymongo

# - mongod --nojournal --dbpath #以控制台方式启动服务器
# - mongod --install #安装MongoDB以服务方式运行
# - mongod --help #显示所有的命令选项

client = pymongo.MongoClient(host='localhost', port=27017)
dblist = client.list_database_names()
print("db:", dblist)
