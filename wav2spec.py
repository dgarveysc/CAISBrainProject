import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

def spectro(wav_file):
	rate, data = wavfile.read(wav_file)
	fig, ax = plt.subplots(1)
	fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
	ax.axis('off')
	pxx, freqs, bins, im = ax.specgram(x=data[:,1], Fs=rate, noverlap=384, NFFT=512)
	ax.axis('off')
	save_file_l = wav_file.split(".")[0] + "l.png"
	save_file_r = wav_file.split(".")[0] + "r.png"
	fig.savefig(save_file_l, dpi=300, frameon='false')
	fig.savefig(save_file_r, dpi=300, frameon='false')



if __name__ == "__main__":
	with open("file_list.txt") as f:
		for line in f:
			line = line.replace("\n", "")
			spectro(line)