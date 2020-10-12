import numpy as np
import pylab as plt
import netCDF4 as nc

tropo_height_netCDF4 = nc.Dataset("xnktc_trohgt.nc", 'r')
O3_budget_netCDF4 = nc.Dataset("xnktc_pmi0_k9_ox_budget.nc", 'r')

tropo_height = tropo_height_netCDF4.variables['ht'][:]
z = O3_budget_netCDF4.variables['z'][:]
tropo_mask = np.empty([383,60,73,96])

for t in xrange(tropo_mask.shape[0]):
    for lat in xrange(tropo_mask.shape[2]):
        for lon in xrange(tropo_mask.shape[3]):
            for h in xrange(tropo_mask.shape[1]):
                if tropo_height[t, 0, lat, lon] >= z[h]:
                    tropo_mask[t, h, lat, lon] = 1
                else:
                    tropo_mask[t, h, lat, lon] = 0
                    
np.save("HIST_Trophgt.npy",tropo_mask)
