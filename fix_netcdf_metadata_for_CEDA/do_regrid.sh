#!/bin/bash
for RUN in {1..5}; do 
	echo ${RUN}
	for fullfile in *r${RUN}*.nc; do
		echo ${fullfile}
	    [ -e "$fullfile" ] || continue
	        # ... rest of the loop body
		filename=$(basename -- "$fullfile")
		extension="${filename##*.}"
		filename="${filename%.*}"
		echo ${filename}
		cdo remapbil,UKCA_griddes ${fullfile} ${filename}_regrid.nc
	done
done

