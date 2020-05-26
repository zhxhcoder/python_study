#!/usr/bin/python
# coding=utf-8
import json
import os
import shutil
import subprocess
import sys
import time
import zipfile

import MultipartPostHandler
import cookielib
import urllib2

# 项目文件目录
project_path = '/data/jenkins/workspace/ydyandroid_auto_package-test/'
# gradle命令集合
gradle_cmd_release_list = ['gradlew assembleRelease', 'gradlew aR']
gradle_cmd_beta_list = ['gradlew assembleBeta', 'gradlew aB']
gradle_cmd_dev_list = ['gradlew assembleDev', 'gradlew aD']
gradle_cmd_gray_list = ['gradlew assembleGray', 'gradlew aG']
gradle_cmd_test_list = ['gradlew assembleAppTest']
gradle_cmd_dark_list = ['gradlew assembleDark']
# 执行的gradle命令
gradle_cmd_release = project_path + 'gradlew assembleRelease'
gradle_cmd_beta = project_path + 'gradlew assembleBeta'
gradle_cmd_dev = project_path + 'gradlew assembleDev'
gradle_cmd_gray = project_path + 'gradlew assembleGray'
gradle_cmd_test = project_path + 'gradlew assembleAppTest'
gradle_cmd_dark = project_path + 'gradlew assembleDark'
# 渠道列表文件
channel_list_path_release = project_path + 'channelInfo/releaseChannelList.txt'
channel_list_path_beta = project_path + 'channelInfo/betaChannelList.txt'
channel_list_path_dev = project_path + 'channelInfo/devChannelList.txt'
channel_list_path_gray = project_path + 'channelInfo/grayChannelList.txt'
channel_list_path_test = project_path + 'channelInfo/testChannelList.txt'
channel_list_path_dark = project_path + 'channelInfo/darkChannelList.txt'
# 生成的apk文件夹
apk_path_release = project_path + 'archive/Release/'
apk_path_beta = project_path + 'archive/Beta/'
apk_path_dev = project_path + 'archive/Dev/'
apk_path_gray = project_path + 'archive/Gray/'
apk_path_test = project_path + 'archive/AppTest/'
apk_path_dark = project_path + 'archive/Dark/'
# 生成的apk文件名
apk_name_release = project_path + 'archive/Release/MobileMoneyAndroid_Release_'
apk_name_beta = project_path + 'archive/Beta/MobileMoneyAndroid_Beta_'
apk_name_dev = project_path + 'archive/Dev/MobileMoneyAndroid_Dev_'
apk_name_gray = project_path + 'archive/Gray/MobileMoneyAndroid_Gray_'
apk_name_test = project_path + 'archive/AppTest/MobileMoneyAndroid_AppTest_'
apk_name_dark = project_path + 'archive/Dark/MobileMoneyAndroid_Dark_'
# 渠道文件
src_channel_file = project_path + 'channelInfo/channel.txt'
# 加固
url_reinforce = 'http://10.106.144.13:8000/'
url_batch_apk_reinforce = url_reinforce + 'batch_apk_reinforce'
url_batch_find_apkinfos = url_reinforce + 'batch_find_apkinfos'
url_batch_apk_download = url_reinforce + 'batch_apk_download'
reinforce_username = 'yrd'
reinforce_password = 'yrd12#$'
reinforce_tactics_id = '6'
query_time = 5
reinforce_unsigned_apk_name = 'Unsigned.apk'
reinforce_signed_apk_name = 'Signed.apk'
reinforce_complete_apk_name = 'Complete.apk'
# 签名
keystore_path = project_path + 'app/creditwealth.dat'
keystore_password = '123456'
keyalias = 'creditwealth'
jarsigner_path = '/opt/yrd_soft/java/bin/'
zipalign_path = '/opt/build_tools/android-sdk-linux/build-tools/23.0.2/'


# 执行一个bat文件并打印信息
def process_cmd_bat(cmd):
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    returncode = p.poll()
    while returncode is None:
        line = p.stdout.readline()
        returncode = p.poll()
        line = line.strip()
        print(line)


# 执行shell脚本
def process_shell(cmd):
    output = os.popen(cmd)
    print(output.read())


# 根据渠道号重新打包
def build_package(channel, gradleinfo):
    print("begin build package:" + channel)
    # 创建一个空文件（不存在则创建）
    f = open(src_channel_file, 'w')
    f.close()
    # 拷贝建立新apk
    target_apk = gradleinfo.get_apk_name() + channel + ".apk"
    shutil.copy(gradleinfo.get_apk_name() + reinforce_complete_apk_name, target_apk)
    # zip获取新建立的apk文件
    zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
    # 初始化渠道信息
    empty_channel_file = "META-INF/channel_{target_channel}".format(target_channel=channel)
    # 写入渠道信息
    zipped.write(src_channel_file, empty_channel_file)
    # 关闭zip流
    zipped.close()
    print('build package:' + channel + ' succ')


# 根据输入命令获得编译信息
def get_gradle_info(cmd):
    print(cmd)
    gradleinfo = None
    if cmd in gradle_cmd_release_list:
        gradleinfo = GradleInfo(gradle_cmd_release, channel_list_path_release, apk_path_release, apk_name_release)
    elif cmd in gradle_cmd_beta_list:
        gradleinfo = GradleInfo(gradle_cmd_beta, channel_list_path_beta, apk_path_beta, apk_name_beta)
    elif cmd in gradle_cmd_dev_list:
        gradleinfo = GradleInfo(gradle_cmd_dev, channel_list_path_dev, apk_path_dev, apk_name_dev)
    elif cmd in gradle_cmd_gray_list:
        gradleinfo = GradleInfo(gradle_cmd_gray, channel_list_path_gray, apk_path_gray, apk_name_gray)
    elif cmd in gradle_cmd_test_list:
        gradleinfo = GradleInfo(gradle_cmd_test, channel_list_path_test, apk_path_test, apk_name_test)
    elif cmd in gradle_cmd_dark_list:
        gradleinfo = GradleInfo(gradle_cmd_dark, channel_list_path_dark, apk_name_dark, apk_name_dark)
    else:
        gradleinfo = GradleInfo(gradle_cmd_beta, channel_list_path_beta, apk_path_beta, apk_name_beta)
    return gradleinfo


# 请求服务器
def request_url(url, params):
    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies), MultipartPostHandler.MultipartPostHandler)
    try:
        print('request url:' + url)
        print('request params:' + str(params))
        response = opener.open(url, params)
        return response.read()
    except Exception as e:
        print(str(e))


# 上传文件到服务器
def upload_file(url, apkpath):
    params = {'username': reinforce_username, 'password': reinforce_password, 'apk': open(apkpath, 'rb'),
              'tactics_id': reinforce_tactics_id}
    response = request_url(url, params)
    data = json.loads(response)
    return data


# 判断字符串是否为json
def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


# 下载apk
def download_apk(url, upload_result, apkpath):
    if_download = True
    while if_download:
        params = {'username': reinforce_username, 'password': reinforce_password,
                  'apkinfo_id': str(upload_result['apkinfo']['apk_id'])}
        download_result = request_url(url, params)
        # 判断返回是否是json字符串
        if is_json(download_result):
            dowanload_result_json = json.loads(download_result)
            # 如果state为1，代表加固未完成
            if str(dowanload_result_json['state']) == '1':
                # 隔断时间查询一次
                time.sleep(query_time)
            else:
                print('download error; state:' + str(dowanload_result_json['state']))
                if_download = False
        else:
            out = open(apkpath, 'w')
            out.write(download_result)
            out.close()
            if_download = False


# 删除可能存在的以前打包的apk
def remove_apk(apk_path):
    cmd = 'rm -rf ' + apk_path
    process_shell(cmd)


# gradle info类
class GradleInfo:
    gradle_cmd = ''
    channel_list_path = ''
    apk_path = ''
    apk_name = ''

    def __init__(self, gradle_cmd, channel_list_path, apk_path, apk_name):
        self.gradle_cmd = gradle_cmd
        self.channel_list_path = channel_list_path
        self.apk_path = apk_path
        self.apk_name = apk_name

    def get_gradle_cmd(self):
        return self.gradle_cmd

    def get_channel_list_path(self):
        return self.channel_list_path

    def get_apk_path(self):
        return self.apk_path

    def get_apk_name(self):
        return self.apk_name


if __name__ == '__main__':
    start = time.clock()
    gradleinfo = get_gradle_info(sys.argv[1])
    # 先删除可能存在的以前打的包
    remove_apk(gradleinfo.get_apk_path())
    # 执行gradle
    process_shell(gradleinfo.get_gradle_cmd())
    # 上传包
    upload_result = upload_file(url_batch_apk_reinforce, gradleinfo.get_apk_name() + 'Origin.apk')
    print('upload_apk_result:' + str(upload_result))
    # 下载加固包
    download_apk(url_batch_apk_download, upload_result, gradleinfo.get_apk_name() + reinforce_unsigned_apk_name)
    # 签名
    sign_cmd = jarsigner_path + 'jarsigner -digestalg SHA1 -sigalg MD5withRSA -verbose -keystore ' + keystore_path + ' -storepass ' + keystore_password + ' -signedjar ' + gradleinfo.get_apk_name() + reinforce_signed_apk_name + ' ' + gradleinfo.get_apk_name() + reinforce_unsigned_apk_name + ' ' + keyalias
    process_shell(sign_cmd)
    # 内存优化
    zipalign_cmd = zipalign_path + 'zipalign -v 4 ' + gradleinfo.get_apk_name() + reinforce_signed_apk_name + ' ' + gradleinfo.get_apk_name() + reinforce_complete_apk_name
    process_shell(zipalign_cmd)
    # 打渠道包
    if len(sys.argv) < 3:
        # 取channel列表
        f = open(gradleinfo.get_channel_list_path())
        channel_list = f.readlines()
        # 循环打包
        for channel in channel_list:
            build_package(channel.strip(), gradleinfo)
        # 输出时间
        print('')
        print('')
        print('')
        print('')
        print('build package:' + str(len(channel_list)))
        print('build time: %f s' % (time.clock() - start))
    else:
        build_package(sys.argv[2], gradleinfo)
