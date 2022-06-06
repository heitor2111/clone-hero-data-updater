import os
import glob
from pytube import Search, YouTube
from pytube.cli import on_progress

def get_item_downloading(index, total):
    return '[' + str(index + 1) + '/' + str(total) + ']'

directories = [x[0] for x in os.walk('../songs')]

list = []

for directory in directories:
    is_music = glob.glob(directory + '\\song.ini')

    if is_music:
        song_data = {
            'name': directory.split('\\')[-1],
            'directory': directory,
            'length': 0
        }

        file = open(directory + '\\song.ini', errors='ignore')

        for line in file:
            if 'song_length' in line:
                length = line.split('=')[-1]
                song_data['length'] = int(length.strip())
        
        if song_data['length'] == 0:
            print(song_data['name'], 'not contain a song_length param and will be skiped.')

        file.close()

        haveVideo = glob.glob(directory + '\\video.*')

        if not haveVideo:
            list.append(song_data)
        else:
            print(song_data['name'], 'must have a video.')

for index, music in enumerate(list):
    search = Search(music['name'])
    downloaded = False

    for result in search.results:
        video = YouTube(result.watch_url, on_progress_callback=on_progress)

        min_length = music['length'] - 15000
        max_length = music['length'] + 5000

        if video.length * 1000 < max_length and video.length * 1000 > min_length:
            streams = video.streams.order_by('resolution').desc().filter(file_extension='mp4', progressive=False)

            for stream in streams:
                try:
                    if (int(stream.resolution[:-1]) <= 1080):
                        print(get_item_downloading(index, len(list)), 'Downloading:', music['name'])

                        stream.download(music['directory'], 'video.' + stream.subtype)
                
                except:
                    print('Error when downloading the video for', music['name'])
                
                else:
                    downloaded = True
                    break

                finally:
                    print('\n')

        if downloaded:
            break
    else:
        print('No video found for the song', music['name'] + '.')