#!/bin/bash

MIN_OFFSET=1
MAX_OFFSET=8192
MIN_INTERVAL=1
MAX_INTERVAL=128

if [ -z "$1" ] || [ -z "$2" ]; then
        echo "Usage $0 (bB) <wrapper_file>"
        exit
fi

if [ "$1" != "b" ] && [ "$1" != "B" ]; then
        echo "Usage $0 (bB) <wrapper_file>"
        exit
fi

if [ ! -f "$2" ]; then
        echo "$2 doesn't exist!"
        exit
fi

method=$1
wrapper="$2"

for (( offset=MIN_OFFSET; offset<=MAX_OFFSET; offset*=2 )); do
        ((offset*=10))
        for ((interval=MIN_INTERVAL; interval<=MAX_INTERVAL; interval*=2)); do
                python Steg.py -r -$method -o$offset -i$interval -w$wrapper > $method-$offset-$interval
                if [ ! -s "$method-$offset-$interval" ]; then
                        rm "$method-$offset-$interval"
                fi
        done
        ((offset/=10))
done
