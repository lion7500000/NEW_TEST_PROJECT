# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess
from sys import stdout
from datetime import timedelta

video_extensions = ['mp4', 'avi']

def get_videos():
    videos = []
    for root, subfolders, files in os.walk(os.getcwd()):
        for file in files:
            if file.split('.')[-1] in video_extensions:
                videos.append (os.path.join(root, file))
    return videos

def get_ffprobe_output (file_name):
    file_name = file_name.replace (' ', '\ ')
    cmd = 'ffprobe -i {} -show_entries format=duration -v quite -of csv="p=0"'.format(file_name)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    #output = p.stdout.read().decode().split()
    return int(float(stdout))

def seconds_to_str (s):
    return (timedelta(seconds=s))

def main ():
    videos= get_videos()
    total_duration = 0
    for video in videos:
        duration = get_ffprobe_output(video)

        print(video.split('/')[-1], 'Duration:', duration)
        total_duration += duration

    print()
    print('Total duration', seconds_to_str(total_duration))
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
