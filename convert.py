import os

path = os.getcwd()
path = path + "/audio_raw"

for filename in os.listdir(path):
    if (filename.endswith(".3gp")): #or .avi, .mpeg, whatever.
        print(filename)
        filename = filename.split('.')[0]
        print("ffmpeg -i audio_raw/{}.3gp audio_wav/{}.wav".format(filename, filename))
        os.system("ffmpeg -i audio_raw/{}.3gp audio_wav/{}.wav".format(filename, filename))
    elif (filename.endswith(".mp4")):
        print(filename)
        filename = filename.split('.')[0]
        print("ffmpeg -i audio_raw/{}.mp4 -ac 2 -f wav audio_wav/{}.wav".format(filename, filename))
        os.system("ffmpeg -i audio_raw/{}.mp4 -ac 2 -f wav audio_wav/{}.wav".format(filename, filename))
    else:
        continue
        