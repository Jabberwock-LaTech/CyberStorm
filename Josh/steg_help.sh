#!/bin/bash

# add the correct file name in the same directory
filename="Text.txt"
bit_or_byte="B"

plus_one=false

image=false

# A shell script to run the Steg program with a large number of offsets and intervals.
for (( j = 1; j <= 13; j++ ))      ### Offset loop ###
do
    offset=$((2**$j))                   #   offset will increase by the powwer of 2's
    if [ "$plus_one" = true ] ;
    then
        offset=$(($offset+1))
    fi
    for (( k = 0 ; k <= 6; k++ )) ### Interval loop ###
    do
        interval=$((2**$k))
        if [ "$image" = true ] ;
        then
            python steg.py "-r" "-$bit_or_byte" "-o$offset" "-i$interval" "-w$filename" > "tmp _o$offset _i$interval.bmp"
        else
            python steg.py "-r" "-$bit_or_byte" "-o$offset" "-i$interval" "-w$filename" > "tmp _o$offset _i$interval.txt"
        fi
    done

done
echo "Done" #### print the new line ###