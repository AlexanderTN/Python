#!/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg
# Usage:
#
# python youtube2mp3.py <URL>, ...
# 
# Example:
# 
# python youtube2mp3.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

import youtube_dl
import sys, os
from sys import argv
SAVE_PATH = os.getcwd() + '\Output_NhacCuaBa'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
}


if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        args = sys.argv[1:]
        with open("input.txt", 'r') as input_file:
            for line in input_file:
                print(line)
        temp = open("input.txt",'r').read().split('\n')
        download_list = []
        for item in temp:
            #if item.find("#") != -1: # Bad because we cannot use list remove() in a for loop => wrong
            if item.startswith("http") == True:
                download_list.append(item)
        
        print(download_list)
        with open("input.txt", 'r') as input_file:
            all_lines = input_file.readlines()
            print(type(all_lines))
        
        ydl.download(download_list)
