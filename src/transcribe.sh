#!/bin/bash
#SBATCH -A p31931
#SBATCH -p gengpu
#SBATCH --gres=gpu:a100:1
#SBATCH -t 2:00:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem=12G
#SBATCH --job-name=scribe
#SBATCH --mail-user=sayarenedennis@northwestern.edu
#SBATCH --mail-type=END,FAIL
#SBATCH --output=/projects/p30791/scribe/log/transcribe.out

module purge all 
module load python-miniconda3/4.12.0

source activate /projects/p30791/envs/scribe

cd /projects/p30791/scribe/

python src/transcribe.py /projects/p30791/scribe/mp3/test.mp3 /projects/p30791/scribe/mp3/test2.mp3

