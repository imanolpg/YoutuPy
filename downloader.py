from pytube import YouTube
import moviepy.editor as mp

video = raw_input("URL del video: ")
yt = YouTube(video)
title = yt.title
print(title)
print(yt.streams.filter(progressive = True, file_extension = "mp4").all())
a = yt.streams.filter(progressive = True, file_extension = "mp4").all()
a[0].download()
clip = mp.VideoFileClip(title + ".mp4")
clip.audio.write_audiofile(title + ".mp3")