#!/bin/bash

FILENAME=""
AAC_EX=".aac"
AAC_FILE=""
WAV_EX=".wav"
WAV_FILE=""

> "file_list.txt"

for i in *.mp4; do
	FILENAME="${i%.*}"
	AAC_FILE="$FILENAME$AAC_EX"
	WAV_FILE="$FILENAME$WAV_EX"
	ffmpeg -i $i -vn -b:a 128k -c:a aac $AAC_FILE
	avconv -i $AAC_FILE $WAV_FILE
	rm $AAC_FILE
	echo $WAV_FILE >> "file_list.txt"
done

python3 wav2spec.py