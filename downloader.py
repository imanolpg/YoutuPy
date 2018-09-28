from pytube import YouTube
import os

videos = open("videos.txt").readlines()
for line in videos:
	video = line
	yt = YouTube(video)
	title = yt.title
	print(title)
	a = yt.streams.filter(progressive = True, file_extension = "mp4").all()
	a[0].download()
	title = title.replace(",", "")
	comando = "ffmpeg -i \'" + title  + ".mp4\' -vn -ab 192k -acodec libmp3lame -ac 2 \'" + title + ".mp3\'"
	os.system(comando)