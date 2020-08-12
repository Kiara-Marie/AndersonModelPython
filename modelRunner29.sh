#!/bin/bash
#SBATCH --account=def-edgrant
#SBATCH --mem-per-cpu=500M
#SBATCH --time=2:00:00

module load python/3.6
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip

pip install --no-index -r requirements.txt
python createNumerovCache.py
