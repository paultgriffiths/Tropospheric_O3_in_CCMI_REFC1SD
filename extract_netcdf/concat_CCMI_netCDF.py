#!/usr/local/shared/ubuntu-12.04/x86_64/python2.7/bin/python
# Only use for files with more than one timestep as iris does not output that dimension if only one step in it. 
import os
from ccmi_stash import lst
import subprocess

jobid='xnktd'
outputdir='/work/n02/n02/ptg21/'+jobid+'/netcdf_v2/'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

name = []
stash_list = []
for i in lst:
    name.append(i[0])

subprocess.call(["/bin/bash", "/home/n02/n02/ptg21/data_analysis/create_netcdf/merge_netcdf.sh"] + [jobid] + [outputdir] + name)

