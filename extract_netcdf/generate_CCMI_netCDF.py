#!/usr/local/shared/ubuntu-12.04/x86_64/python2.7/bin/python
# Only use for files with more than one timestep as iris does not output that dimension if only one step in it. 
import iris
import STASH_definitions_73 as def_STASH
from ccmi_stash import lst
import os

jobid='xnktd'
#decades = [['i',range(0,10)], ['j',range(0,10)], ['k',range(0,10)], ['l',range(0,1)]]
#decades = [['i',range(0,10)]]#, ['j',range(0,10)], ['k',range(0,10)], ['l',range(0,1)]]
#decades = [['h',range(9,10)], ['i',range(0,10)], ['j',range(0,10)], ['k',range(0,10)], ['l',range(0,1)]]
#decades = [['i',range(0,10)], ['j',range(0,10)], ['k',range(0,5)], ['l',range(0,1)]]
#decades = [['j',range(0,6) ]]#, ['k',range(0,5)]]
decades = [['j',range(6,10)], ['k',range(0,5)]]
#decades = [['k',range(0,5)]]
inputdir='/work/n02/n02/jmk64/um/'+jobid+'/'
outputdir='/work/n02/n02/ptg21/'+jobid+'/netcdf_v2/'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

#################################################################### 
# Which STASH numbers to take for the netCDF file
#################################################################### 
name = []
stash_list = []
for i in lst:
    name.append(i[0])
    stash_list.append(i[1])
#################################################################### 
# loop over decades and years
#################################################################### 
for d in decades:
    for y in d[1]:
        print '\n'+jobid+'\npm'+d[0]+str(y)
        # prepare STASH codes
        path_to_files=inputdir+'*pm'+d[0]+str(y)+'*'
        for z in range(0,len(stash_list)):
            stash=[]
            field_constr=[]
            for i in stash_list[z]:
                def ret_stash_string(i):
                    isec=i/1000
                    sec="{:02d}".format(isec)
                    it="{:03d}".format(i-(1000*isec))
                    return 'm01s'+sec+'i'+it
                stash.append(ret_stash_string(i))
                field_constr.append(iris.AttributeConstraint(STASH=ret_stash_string(i)))
            print 'stash : '
            print stash
        # load pp files and output netCDF
            outfile=outputdir+jobid+'_pm'+d[0]+str(y)+name[z]+'.nc'
            field=iris.load(path_to_files,field_constr,callback=def_STASH.UKCA_callback)
            #print field
            iris.save(field, outfile, netcdf_format="NETCDF3_CLASSIC")

#################################################################### 
# Shell script to merge files
#################################################################### 
import subprocess

subprocess.call(["/bin/bash", "merge_netcdf.sh"] + [jobid] + [outputdir] + name)

