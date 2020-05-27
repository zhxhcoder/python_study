#!/usr/bin/python
# coding=utf-8
import hashlib;
import os
import time

from flask import Flask
from flask import jsonify
from flask import request

project_path = '/data/auto_install_apk/'
ip = '10.141.5.80'
url = 'http://10.141.5.80/auto_install_apk/'

app = Flask(__name__)


# 获取文件的md5值
def get_file_md5(file_path):
    file = None
    str_md5 = ''
    try:
        file = open(file_path, "rb")
        md5 = hashlib.md5()
        str_read = ''
        while True:
            str_read = file.read(8096)
            if not str_read:
                break
            md5.update(str_read)
        # read file finish
        str_md5 = md5.hexdigest()
    except:
        print(str('get md5 fail'))
    finally:
        if file:
            file.close()
    return str_md5;


# 遍历一个文件夹
def iter_browse(path):
    for home, dirs, files in os.walk(path):
        for filename in reversed(files):
            yield os.path.join(home, filename)


# 返回下载目录
@app.route('/mainController/listAndroidFile.action', methods=['POST'])
def list_android_file():
    print
    'request str:' + str(request)
    print
    'type:' + request.form.get('actionType')
    store_infos = []
    actiontype = request.form.get('actionType')
    for apk_path in iter_browse(project_path + actiontype):
        filename = os.path.basename(apk_path)
        statinfo = os.stat(apk_path)
        ctime = time.localtime(statinfo.st_ctime)
        store_info = {'fileName': filename, 'downloadUrl': url + actiontype + '/' + filename,
                      'fileMd5': get_file_md5(apk_path), 'fileTime': time.strftime('%Y-%m-%d %H:%M:%S', ctime),
                      'progress': 0, 'downFlag': False}
        store_infos.append(store_info)
        if len(store_infos) == 20:
            break
    print('store_infos:' + str(store_infos))
    return jsonify({'data': store_infos})

    if __name__ == '__main__':
        app.run(host=ip)
