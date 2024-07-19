#!/bin/bash
source ~/anaconda3/bin/activate 
conda activate pymca
python -i /epics/iocs/ioc-pymca/python/pcaspy/pcaspy_server.py
