#!/usr/bin/python
# coding=utf-8
import os
import subprocess
import sys
import time

# 项目文件目录
project_path = '/home/bugfree/jenkinsFile/workspace/ydyandroid_auto_package_Online/'
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
# 生成的apk文件名
apk_name_release = project_path + 'archive/Release/MobileMoneyAndroid_Release_'
apk_name_beta = project_path + 'archive/Beta/MobileMoneyAndroid_Beta_'
apk_name_dev = project_path + 'archive/Dev/MobileMoneyAndroid_Dev_'
apk_name_gray = project_path + 'archive/Gray/MobileMoneyAndroid_Gray_'
apk_name_test = project_path + 'archive/AppTest/MobileMoneyAndroid_AppTest_'
apk_name_dark = project_path + 'archive/Dark/MobileMoneyAndroid_Dark_'
# 渠道文件
src_channel_file = project_path + 'channelInfo/channel.txt'
# java命令文件夹
jarsigner_path = '/opt/yrd_soft/java/bin/'


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


def process_shell(cmd):
    output = os.popen(cmd)
    print(output.read())


# 根据渠道号重新打包
def build_package(channel, gradleinfo):
    print("begin build package:" + channel)
    target_apk = gradleinfo.get_apk_name() + channel + ".apk"
    walle_cmd = jarsigner_path + 'java -jar walle-cli-all.jar put -c ' + channel + ' ' + gradleinfo.get_apk_name() + 'Origin.apk' + ' ' + target_apk
    process_shell(walle_cmd)
    print('build package:' + channel + ' succ')


def get_gradle_info(cmd):
    print(cmd)
    gradleinfo = None
    if cmd in gradle_cmd_release_list:
        gradleinfo = GradleInfo(gradle_cmd_release, channel_list_path_release, apk_name_release)
    elif cmd in gradle_cmd_beta_list:
        gradleinfo = GradleInfo(gradle_cmd_beta, channel_list_path_beta, apk_name_beta)
    elif cmd in gradle_cmd_dev_list:
        gradleinfo = GradleInfo(gradle_cmd_dev, channel_list_path_dev, apk_name_dev)
    elif cmd in gradle_cmd_gray_list:
        gradleinfo = GradleInfo(gradle_cmd_gray, channel_list_path_gray, apk_name_gray)
    elif cmd in gradle_cmd_test_list:
        gradleinfo = GradleInfo(gradle_cmd_test, channel_list_path_test, apk_name_test)
    elif cmd in gradle_cmd_dark_list:
        gradleinfo = GradleInfo(gradle_cmd_dark, channel_list_path_dark, apk_name_dark)
    else:
        gradleinfo = GradleInfo(gradle_cmd_beta, channel_list_path_beta, apk_name_beta)
    return gradleinfo


class GradleInfo:
    gradle_cmd = ''
    channel_list_path = ''
    apk_name = ''

    def __init__(self, gradle_cmd, channel_list_path, apk_name):
        self.gradle_cmd = gradle_cmd
        self.channel_list_path = channel_list_path
        self.apk_name = apk_name

    def get_gradle_cmd(self):
        return self.gradle_cmd

    def get_channel_list_path(self):
        return self.channel_list_path

    def get_apk_name(self):
        return self.apk_name


if __name__ == '__main__':
    start = time.clock()
    gradleinfo = get_gradle_info(sys.argv[1])
    # 执行gradle
    process_shell(gradleinfo.get_gradle_cmd())
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

