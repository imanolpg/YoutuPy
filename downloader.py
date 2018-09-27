from pytube import YouTube
import os

#video = input("URL del video: ")
yt = YouTube('https://www.youtube.com/watch?v=va-uhVt93hA')
title = yt.title
print(title)
print(yt.streams.filter(progressive = True, file_extension = "mp4").all())
yt.streams.filter(progressive = True, file_extension = "mp4").all().download()