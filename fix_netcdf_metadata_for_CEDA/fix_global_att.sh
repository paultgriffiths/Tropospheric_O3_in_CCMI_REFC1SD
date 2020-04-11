#!/bin/bash
for filename in fODS*.nc; do
  echo ${filename}
        ncatted -h -a contact,global,o,c,"Paul Griffiths paul.griffiths@ncas.ac.uk" ${filename}
        ncatted -h -a institution,global,o,c,"National Centre for Atmospheric Science" ${filename}
        ncatted -h -a project,global,o,c,"ACCI" ${filename}
        ncatted -h -a model,global,o,c,"Data were generated using the Met Office Unified Model (UM) at N48 horizontal resolution over global domain." ${filename}
        ncatted -h -a model_description,global,o,c,"Griffiths et al. (2019) On the changing role of the stratosphere on the tropospheric ozone budget: 1979-2010" ${filename}
        ncatted -h -a run,global,o,c,"Historical integration with constant ODS at 1979 values, other emissions and forcings as per Eyring et al 2013" ${filename}
        ncatted -h -a run_experiment,global,o,c,"Original UM job was XNKTD" ${filename}
done
