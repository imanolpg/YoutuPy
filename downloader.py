from pytube import YouTube
from pytube.helpers import safe_filename
import os

os.system("figlet YoutuPy")
videos = open("videos.txt").readlines()
os.system("rm -f *.mp3")
os.system("rm -f *.mp4")
for line in videos:
	video = line
	yt = YouTube(video)
	title = safe_filename(yt.title)
	print(title)
	a = yt.streams.filter(progressive = True, file_extension = "mp4").all()
	a[0].download()
	comando = "ffmpeg -i \'" + title  + ".mp4\' \'" + title + ".mp3\' >/dev/null 2>&1"
	os.system(comando)
os.system("mv -f *.mp3 canciones")
os.system("rm -f *.mp4")
print("------Terminado------")
