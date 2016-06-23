#!/bin/bash 

#SBATCH -n 12  #Number of cores
#SBATCH -N 1   #node number

#SBATCH -t 3000  #Runtime in minutes 

#SBATCH -p general  #Partition to submit to 

#SBATCH --mem=10600  #Memory per node in MB (see also --mem-per-cpu)

#SBATCH -o S8-%A_%a.out
#SBATCH -J S8-%A_%a.err

source ../chilin_env/bin/activate
chilin simple -u qinq -s hg38 --threads 8 -i STAT6_S8 -o S8 -t GSM445803/SRR039652.fastq -p narrow -r tf --dont_remove
