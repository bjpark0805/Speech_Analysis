import io
import os
import sys
import numpy as np
import crepe
from scipy.io import wavfile
import wave
import resampy
import pandas as pd

file_path = "audio_wav/"     #Input audio file path in my case
output_filepath = "Timelines/" # Final transcript path
bucketname = "speechrecognitionkt" # Name of the bucket created in the step before

def beep_detection(filename):
    sr, audio = wavfile.read(file_path + filename) # ex) audio_wav/balhwa.wav
    audio_16000 = resampy.resample(audio, sr, 16000)
    time, frequency, confidence, activation = crepe.predict(audio_16000, 16000, step_size = 100)
    
    timeline = []
    beep_step = True
    beep_t = 0
    answer_t = 0
    
    for t, f in zip(time, frequency):
        if(f > 800 and f < 900 and t > beep_t + 1 and beep_step == True):
            beep_t = t
            beep_step = False
        elif(f > 800 and f < 900 and t > beep_t + 1 and beep_step == False):
            timeline.append((beep_t, -1, -1))
            beep_t = t
        elif(f > 0 and t > beep_t + 0.5 and beep_step == False):
            if(np.count_nonzero(frequency[(int)(10*t):(int)(10*t) + 4]) == 4 and np.mean(frequency[(int)(10*t):(int)(10*t) + 5]) < 620):
                answer_t = t
                timeline.append((beep_t, answer_t, round(answer_t - beep_t, 1)))
                beep_step = True
    
    return timeline

def save_csv(filename, timeline):
    # Convert to dataframe for saving the result as csv
    df = pd.DataFrame(timeline)
    df.columns = ['Beep Time', 'Response Time', 'Delay']
    
    df.to_csv(output_filepath + filename, mode = 'w')
    
if __name__ == "__main__":
    file_name = sys.argv[1]
    timeline = beep_detection(file_name)
    name = file_name.split(".")[0]
    save_csv(name + ".csv", timeline)
    print("Timeline Analyzed!!")