#!/bin/bash 

#SBATCH -n 12  #Number of cores
#SBATCH -N 1   #node number

#SBATCH -t 3000  #Runtime in minutes 

#SBATCH -p general  #Partition to submit to 

#SBATCH --mem=10600  #Memory per node in MB (see also --mem-per-cpu)

#SBATCH -o S1-%A_%a.out
#SBATCH -J S1-%A_%a.err

source ../chilin_env/bin/activate
chilin simple -u qinq -s mm10 --threads 8 -i H3K27me3_S1 -o S1 -t /mnt/Storage/home/qinq/01_Projects/Programming/chilin/demo/GSM392049/SRR038978.fastq,/mnt/Storage/home/qinq/01_Projects/Programming/chilin/demo/GSM392050/SRR038979.fastq -p broad -r histone --dont_remove
