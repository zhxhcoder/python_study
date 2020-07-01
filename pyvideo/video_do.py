import datetime
import os
import re

import moviepy.editor as mp


def water_mark(src_dir):
    video = mp.VideoFileClip(src_dir)

    logo = (mp.ImageClip("watermark.png")
            .set_duration(video.duration)  # 时长
            .resize(height=100)  # 水印高度，等比缩放
            .margin(left=10, top=10, opacity=1)  # 水印边距和透明度
            .set_pos(("left", "top")))  # 水印位置

    result = mp.CompositeVideoClip([video, logo])

    print("开始写入水印。。。")
    # mp4文件默认用libx264编码， 比特率单位bps
    result.write_videofile(re.sub(r'\.mp4$', "_mark.mp4", src_dir), codec="libx264", bitrate="10000000")
    print("写入完成")


def traverse_file(src_dir):
    start = datetime.datetime.now()
    file_num = 0
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_num = file_num + 1
                src_file = os.path.join(root, file)
                if re.search(r'111\.mp4$', file) is not None:
                    water_mark(src_file)
                elif re.search(r'222\.mp4$', file) is not None:
                    water_mark(src_file)

    end = datetime.datetime.now()
    print('耗时: %s Seconds' % (end - start))


if __name__ == "__main__":
    srcDir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/video")
    traverse_file(srcDir)
