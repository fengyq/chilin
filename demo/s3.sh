#!/bin/bash 

#SBATCH -n 12  #Number of cores
#SBATCH -N 1   #node number

#SBATCH -t 3000  #Runtime in minutes 

#SBATCH -p general  #Partition to submit to 

#SBATCH --mem=10600  #Memory per node in MB (see also --mem-per-cpu)

#SBATCH -o S3-%A_%a.out
#SBATCH -J S3-%A_%a.err

source ../chilin_env/bin/activate
chilin simple -u qinq -s mm10 --threads 8 -i H3K4me3_S3 -o S3 -t wgEncodeLicrHistoneBmarrowH3k4me3MAdult8wksC57bl6StdRawDataRep1.fastq.gz,wgEncodeLicrHistoneBmarrowH3k4me3MAdult8wksC57bl6StdRawDataRep2.fastq.gz -p narrow -r histone --dont_remove
