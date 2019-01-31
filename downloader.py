import os
import ssl

if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

try:
    from pytube import YouTube
    from pytube.helpers import safe_filename
except ModuleNotFoundError:
    os.system("python3 -m pip install pytube")
    os.system("python3 -m pip install pyfiglet")
    from pytube import YouTube
    from pytube.helpers import safe_filename

os.system("figlet YoutuPy")
videos = open("videos.txt").readlines()
os.system("rm -f *.mp3")
os.system("rm -f *.mp4")
counter = 0
for line in videos:
    counter = counter + 1
    try:
        video = line
        yt = YouTube(video)
        title = safe_filename(yt.title)
        print(title)
        a = yt.streams.filter(progressive=True, file_extension="mp4").all()
        a[0].download()
        command = "ffmpeg -i \'" + title + ".mp4\' \'" + title + ".mp3\' >/dev/null 2>&1"
        os.system(command)
    except:
        failed_videos = open("failed_videos.txt", "a")
        failed_videos.write(video)
        failed_videos.close()
        print("Error in video: " + str(counter) + " | Link --> failed_videos.txt")
os.system("mv -f *.mp3 songs >/dev/null 2>&1")
print("Songs moved to \"songs\" folder")
if input("Do you want to keep all videos?: ") in ["Y", "y", "yes", "YES", "Yes"]:
    os.system("mv -f *.mp4 videos >/dev/null 2>&1")
    print("Videos moved to \"videos\" folder")
else:
    os.system("rm -f *.mp4 >/dev/null 2>&1")
    print("All videos deleted")
print("------Finished------")
print("Change songs property with modifier.py\n")
