import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

import os
import shutil
import wave

def spectro(wav_file, action):
    rate, data = wavfile.read("/hdd/datasets/Moments_in_Time_Mini/training-sound/" + action + "/" + wav_file)
    print(wav_file)
    print(action)
    fig, ax = plt.subplots(1)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.axis('off')
    
    #check if one channel of audio
    if wave.open("/hdd/datasets/Moments_in_Time_Mini/training-sound/" + action + "/" + wav_file, 'rb').getnchannels() == 2:
        '''
        print(data[0])
        pxx, freqs, bins, im = ax.specgram(x=data[:,0], Fs=rate, noverlap=384, NFFT=512)
        ax.axis('off')
        save_file = wav_file.split(".")[0] + ".png"
        fig.savefig(save_file, dpi=300, frameon='false')
        #save file in the right directory in the training-spec folder
        shutil.move(save_file, "/hdd/datasets/Moments_in_Time_Mini/training-spec/" + action + "/" + save_file)     
    else:
        '''
        #check if two channels of audio 
        pxx, freqs, bins, im = ax.specgram(x=data[:,1], Fs=rate, noverlap=384, NFFT=512)
        ax.axis('off')
        save_file_l = wav_file.split(".")[0] + "-l.png"
        save_file_r = wav_file.split(".")[0] + "-r.png"
        fig.savefig(save_file_l, dpi=300, frameon='false')
        fig.savefig(save_file_r, dpi=300, frameon='false')
        #save file in the right directory in the training-spec folder
        shutil.move(save_file_l, "/hdd/datasets/Moments_in_Time_Mini/training-spec/" + action + "/" + save_file_l)
        shutil.move(save_file_r, "/hdd/datasets/Moments_in_Time_Mini/training-spec/" + action + "/" + save_file_r)
        
        plt.close('all')
    
    plt.close('all')


if __name__ == "__main__":
    #retrieve file_list.txt from training-sound
    with open("/hdd/datasets/Moments_in_Time_Mini/training-sound/file_list.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            
            if line[0] == 'a' or line[0] == 'b':
                print("Skipped")
                continue
            
            #split line by '/' to get the action and the file name
            split_by_action = line.split("/")
            #delimit directory name from string
            action = split_by_action[0]
            
            filename = split_by_action[1]
            
            if os.path.isfile("/hdd/datasets/Moments_in_Time_Mini/training-sound/" + action + "/" + filename):
                try:
                    spectro(filename, action)
                except Exception:
                    continue