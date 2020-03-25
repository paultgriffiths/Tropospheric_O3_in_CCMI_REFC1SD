import netCDF4 as nc
import numpy as np
from tropo_mask import tropo_mask_calc

tropo_mask = tropo_mask_calc('HIST_Trophgt.nc')
nyrs=2010-1979

ncfile = nc.Dataset('HIST_ox_prod.nc')
alecfac = 3.0## NOTE Errorin STASH output so have had to multiply fluxes (here) by three!!

## Ox PRODUCTION
p1 = np.array(ncfile.variables['ox_prod_ho2_no'][-12*nyrs:], dtype=np.float64)
p1 = p1 * alecfac* tropo_mask
ho2no_tot   = np.sum(p1*48.*3600.*24.*30.,axis=(1,2,3))

p2 = np.array(ncfile.variables['ox_prod_meoo_no'][-12*nyrs:], dtype=np.float64)
p2 = p2 * alecfac* tropo_mask
meo2no_tot  = np.sum(p2*48.*3600.*24.*30.,axis=(1,2,3))

p3 = np.array(ncfile.variables['ox_prod_no_ro2'][-12*nyrs:], dtype=np.float64)
p3 = p3 * alecfac* tropo_mask
ro2no_tot   = np.sum(p3*48.*3600.*24.*30.,axis=(1,2,3))

p4 = np.array(ncfile.variables['ox_prod_oh_inorgacid'][-12*nyrs:], dtype=np.float64)
p4 = p4 * alecfac* tropo_mask
ohrcooh_tot = np.sum(p4*48.*3600.*24.*30.,axis=(1,2,3))

p5 = np.array(ncfile.variables['ox_prod_oh_orgnitrate'][-12*nyrs:], dtype=np.float64)
p5 = p5 * alecfac* tropo_mask
ohrono2_tot = np.sum(p5*48.*3600.*24.*30.,axis=(1,2,3))

p6 = np.array(ncfile.variables['ox_prod_orgnitrate_photol'][-12*nyrs:], dtype=np.float64)
p6 = p6 * alecfac* tropo_mask
hvrono2_tot = np.sum(p6*48.*3600.*24.*30.,axis=(1,2,3))

p7 = np.array(ncfile.variables['ox_prod_oh_panrxns'][-12*nyrs:], dtype=np.float64)
p7 = p7 * alecfac* tropo_mask
ohpan_tot   = np.sum(p7*48.*3600.*24.*30.,axis=(1,2,3))

prod = p1 + p2 + p3 + p4 + p5 + p6 + p7
o3prod_tot  = np.sum(prod*48.*3600.*24.*30.,axis=(1,2,3))

## Ox LOSS
ncfile = nc.Dataset('HIST_ox_loss.nc')
l1 = np.array(ncfile.variables['ox_loss_o1d_h2o'][-12*nyrs:], dtype=np.float64)
l1 = l1*alecfac*tropo_mask
o1d_tot     = np.sum(l1*48.*3600.*24.*30.,axis=(1,2,3))

l2 = np.array(ncfile.variables['ox_loss_minor_rxns'][-12*nyrs:], dtype=np.float64)
l2 = l1*alecfac*tropo_mask
mlr_tot     = np.sum(l2*48.*3600.*24.*30.,axis=(1,2,3))

l3 = np.array(ncfile.variables['ox_loss_ho2_o3'][-12*nyrs:], dtype=np.float64)
l3 = l3*alecfac*tropo_mask
ho2o3_tot   = np.sum(l3*48.*3600.*24.*30.,axis=(1,2,3))

l4 = np.array(ncfile.variables['ox_loss_oh_o3'][-12*nyrs:], dtype=np.float64)
l4 = l4*alecfac*tropo_mask
oho3_tot    = np.sum(l4*48.*3600.*24.*30.,axis=(1,2,3))

l5 = np.array(ncfile.variables['ox_loss_o3_alkene'][-12*nyrs:], dtype=np.float64)
l5 = l5*alecfac*tropo_mask
o3alk_tot   = np.sum(l5*48.*3600.*24.*30.,axis=(1,2,3))

l6 = np.array(ncfile.variables['ox_loss_n2o5_h2o'][-12*nyrs:], dtype=np.float64)
l6 = l6*alecfac*tropo_mask
n2o5h2o_tot = 3.*np.sum(l6*48.*3600.*24.*30.,axis=(1,2,3))

l7 = np.array(ncfile.variables['ox_loss_no3_chemloss'][-12*nyrs:], dtype=np.float64)
l7 = l7*alecfac*tropo_mask
no3loss_tot = np.sum(l7*48.*3600.*24.*30.,axis=(1,2,3))

loss = l1 + l2 + l3 + l4 + l5 + l6 + l7
o3loss_tot  = np.sum(loss*48.*3600.*24.*30.,axis=(1,2,3))

ncfile = nc.Dataset('HIST_ox_dep.nc')
# DRY DEP OF OX as O3 and NOy (HONO2 counts as one Ox)
d_1 = np.array(ncfile.variables['ozone_dry_dep_3d'][-12*nyrs:], dtype=np.float64)
d_2 = np.array(ncfile.variables['noy_dry_dep_3d'][-12*nyrs:], dtype=np.float64)
d_3 = np.array(ncfile.variables['noy_wet_dep_3d'][-12*nyrs:], dtype=np.float64)
dtot = (d_1 + d_2 + d_3)
dep_tot = ste_tot = np.sum(dtot*48.*3600.*24.*30.,axis=(1,2,3))

# STRAT - TROP EXCHANGE, apply TROPMASK
ncfile = nc.Dataset('HIST_ox_STE.nc')
ste = np.array(ncfile.variables['ste'][-12*nyrs:], dtype=np.float64)
ste_tot = np.sum(ste*48.*3600.*24.*30.,axis=(1,2,3))
#net = o3prod_tot - o3loss_tot - dep_tot + ste_tot

o3_mass_prod = np.zeros(nyrs)
o3_mass_loss = np.zeros(nyrs)

# WRITE OUT INTERMEDIATE RESULTS
for iyear in range(0, nyrs):
    o3_mass_prod[iyear] = np.sum(prod[iyear*12:(iyear+1)*12,:,:,:])*48.*3600.*24.*30.# total prod
    o3_mass_loss[iyear] = np.sum(loss[iyear*12:(iyear+1)*12,:,:,:])*48.*3600.*24.*30. # total loss