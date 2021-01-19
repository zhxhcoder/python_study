# -*- coding: utf-8 -*-
# 解决应用加固导致 Walle 渠道信息失效的自动化脚本工具

import getopt
import os
import shutil
import sys

zipalign = "/Users/xhzh/Library/Android/sdk/build-tools/28.0.3/zipalign"
apksigner = "/Users/xhzh/Library/Android/sdk/build-tools/28.0.3/apksigner"
keystore = "release.keystore"
key_alias = ""
keystore_password = ""
key_password = ""


walle_cli = "walle-cli-all.jar"
channel_conf = "channel"

CMD_ZIP_ALIGN = zipalign + " -v 4 %s %s"
CMD_APK_SIGNER = apksigner + " sign --ks " + keystore + " --ks-key-alias " + key_alias + " --ks-pass pass:" \
                 + keystore_password + " --key-pass pass:" + key_password + " --out %s %s"
CMD_WALLE = "java -jar %s  batch -f " + channel_conf + " %s %s"

flavor = None


def parse_options(argv):
    print(argv)
    opts, args = getopt.getopt(argv, "f:", ["flavor="])
    if len(opts) == 0:
        print("请输入参数，例如 --flavor=release")
        raise AttributeError()

    for k, v in opts:
        if k == "--flavor":
            return v
    print(options.__str__())
    return None


# 获取 output/apk 的子目录
def get_apk_dirs(dir_path):
    apk_dirs = []
    for f in os.listdir(dir_path):
        if f == "debug":
            continue
        child_path = os.path.join(dir_path, f)
        if os.path.isdir(child_path):
            # 指定了 flavor 就忽略其它
            if flavor is not None and f != flavor:
                continue
            apk_dirs.append(child_path)
            print("发现一个 apk 目录：%s" % child_path)
    return apk_dirs


# 获取 apk 文件
def get_apk_files(dir_path):
    apk_files = []
    for f in os.listdir(dir_path):
        if f == "channels" or f == "debug":
            continue
        file = os.path.join(dir_path, f)
        if os.path.isfile(file) and file.endswith(".apk"):
            apk_files.append(file)
            print("发现一个 apk：%s" % file)
        elif os.path.isdir(file):
            apk_files.extend(get_apk_files(file))
            print("发现一个 apk 目录：%s" % file)
    return apk_files


if __name__ == '__main__':
    try:
        print("action")
        # 当前工作目录，请把此 py 文件放至 app 项目的根目录下
        project_path = os.getcwd()
        # 默认生成的 apk 目录
        apk_path = project_path + os.sep + "archives" + os.sep + "release"
        print("check %s exist" % apk_path)
        if not os.path.exists(apk_path):
            print("未检测到 %s 下有 apk" % apk_path)
            raise RuntimeError

        if len(sys.argv[1:]) != 0:
            # 如果指定了 flavor ，则只对该 flavor 下的目录打包
            flavor = parse_options(sys.argv[1:])

        apk_files = []
        for d in get_apk_dirs(apk_path):
            apk_files.extend(get_apk_files(d))

        for apk in apk_files:
            # 在当前目录生成对齐的文件
            apk_name = os.path.basename(apk).split(".")[0]
            dir_path = os.path.dirname(apk)

            aligned_apk = os.path.join(dir_path, "%s_aligned.apk" % apk_name)
            if os.path.exists(aligned_apk):
                os.remove(aligned_apk)
            print("对齐：%s" % aligned_apk)
            os.system(CMD_ZIP_ALIGN % (apk, aligned_apk))

            signed_apk = os.path.join(dir_path, "%s_signed.apk" % apk_name)
            if os.path.exists(signed_apk):
                os.remove(signed_apk)
            print("签名：%s" % signed_apk)
            os.system(CMD_APK_SIGNER % (signed_apk, aligned_apk))

            channel_dir = os.path.join(dir_path, "channels")
            if os.path.exists(channel_dir):
                # 强制删除
                shutil.rmtree(channel_dir)
            os.mkdir(channel_dir)
            print("创建渠道文件夹：%s" % channel_dir)

            # 进行写入渠道号
            os.system(CMD_WALLE % (walle_cli, signed_apk, channel_dir))

            # clean
            os.remove(aligned_apk)
            os.remove(signed_apk)

    except Exception as e:
        print(e)
        input("Please Enter To Finish...")
