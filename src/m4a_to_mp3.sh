#!/bin/bash

module purge all
module load python-miniconda3/4.12.0

source activate /projects/p30791/envs/scribe  # contains ffmpeg

fin="/projects/p30791/scribe/m4a/test2.m4a"
fout="/projects/p30791/scribe/mp3/test2.mp3"

ffmpeg -i $fin -codec:a libmp3lame -qscale:a 2 $fout

# code taken from https://askubuntu.com/questions/65331/how-to-convert-a-m4a-sound-file-to-mp3
