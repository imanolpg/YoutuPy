from pytube import YouTube


video = raw_input("URL del video: ")
yt = YouTube(video)
title = yt.title
print(title)
try:
	print(yt.streams.filter(progressive = True, file_extension = "mp4").all())
	a = yt.streams.filter(progressive = True, file_extension = "mp4").all()
	a[0].download()
except:
	exit()