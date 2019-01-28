import os

try:
    from mutagen.easyid3 import EasyID3
    import mutagen
except ModuleNotFoundError:
    print("Installing mutagen...")
    os.system("python3 -m pip install mutagen")

if input("Manage songs metadata?: ") == "y":
    files = os.listdir("./canciones")
    counter = 1
    for file in files:
        if file[0] == ".":
            pass
        else:
            try:
                song = EasyID3("./canciones/" + file)
                file_split = file.split(".")
                file = ""
                for part in file_split[0: len(file_split) - 1]:
                    file = file + part
                try:
                    song['title'] = file.split("-")[1].strip()
                    song['artist'] = file.split("-")[0].strip()
                except:
                    song['title'] = file
                    song['artist'] = ""
                song['album'] = ""
                song['composer'] = ""
                song.save()
            except mutagen.id3._util.ID3NoHeaderError:
                song = mutagen.File("./songs/" + file, easy=True)
                song.add_tags()
                file_split = file.split(".")
                file = ""
                for part in file_split[0: len(file_split) - 1]:
                    file = file + part
                try:
                    song['title'] = file.split("-")[1].strip
                    song['artist'] = file.split("-")[0].strip()
                except:
                    song['title'] = file
                    song['artist'] = ""
                song['album'] = ""
                song['composer'] = ""
                song.save()
        print("Done: {0:>4}/{1:<4}: {2:<60}" .format(str(counter), str(len(files)), file))
        counter = counter + 1
print("------Finished------")
