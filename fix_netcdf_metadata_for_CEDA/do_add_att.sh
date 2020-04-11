#!/bin/bash
for filename in xmveg*.nc; do
	ncatted -h -a contact,global,o,c,"Paul Griffiths paul.griffiths@ncas.ac.uk" ${filename}
	ncatted -h -a institution,global,o,c,"National Centre for Atmospheric Science" ${filename}
	ncatted -h -a project,global,o,c,"ACCI" ${filename}
	ncatted -h -a model,global,o,c,"Data were generated using the Met Office Unified Model (UM) at N48 horizontal resolution over global domain." ${filename}
	ncatted -h -a model_description,global,o,c,"Griffiths et al. (2019) Methane Emissions in a Chemistry-Climate Model: feedbacks and climate response" ${filename}
	ncatted -h -a run,global,o,c,"xmveg with climate forcings (but not CH4 or O3PRE) RCP 85 emissions as per Lamarque et al 2013" ${filename}
	ncatted -h -a run_experiment,global,o,c,"Delta(CC) - future RCP8.5 with climate forcings only" ${filename}
done
