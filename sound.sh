#!/bin/bash

FILENAME=""
AAC_EX=".aac"
AAC_FILE=""
WAV_EX=".wav"
WAV_FILE=""

> "file_list.txt"

BASE_DIR="/hdd/datasets/Moments_in_Time_Mini/validation"
DIR=""
ACTION=""

for filename in $BASE_DIR/*; do

    DIR=$filename
    #echo $DIR
    #echo $BASE_DIR

    #split directory name to get the action
    IFS='/'
    read -ra ADDR <<< "$DIR"
    ACTION="${ADDR[5]}"
    #echo $ACTION
    
    IFS=' '

    #make a directory in /hdd/datasets/Moments_in_Time_Mini/training-sound for each action
    mkdir -p /hdd/datasets/Moments_in_Time_Mini/validation-spec/$ACTION;

    : '
    for file in $filename/*; do
        #echo $file
        if [[ $file == *.mp4 ]]; then
            echo $file
            #split file name to get the name of the video
            IFS='/'
            read -ra ADDR <<< "$file"
            NAME="${ADDR[6]}"
            echo $NAME
            IFS='.'
            read -ra ADDR <<< "$NAME"
            MOD_NAME="${ADDR[0]}"
            echo $MOD_NAME
            FILENAME="$MOD_NAME"
            echo "FILENAME: $FILENAME"
            IFS=' '
            
            AAC_FILE="$FILENAME$AAC_EX"
            WAV_FILE="$FILENAME$WAV_EX" #each WAV file will have a name <mp4 name>.wav
            ffmpeg -i $file -vn -b:a 128k -c:a aac $AAC_FILE
            ffmpeg -i $AAC_FILE $WAV_FILE
            rm $AAC_FILE
            echo $ACTION/$WAV_FILE >> "file_list.txt"

            #add WAV file to the directory of that action
            mv $WAV_FILE /hdd/datasets/Moments_in_Time_Mini/validation-sound/$ACTION
            
        fi
    done
    '

done

#mv file_list.txt /hdd/datasets/Moments_in_Time_Mini/validation-sound/
#python3 wav2spec.py
