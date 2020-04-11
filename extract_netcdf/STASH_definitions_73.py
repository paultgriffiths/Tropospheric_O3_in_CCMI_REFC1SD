''' Assign information to STASH numbers.
Such as variable names, units, conversion factors.
'''
#################################################################### 
# ASSIGN INFORMATION TO STASH NUMBERS

# Standard names than iris reads can be in file in "python:> help(iris.std_names)": /usr/local/shared/ubuntu-12.04/x86_64/python2.7-iris/1.6.1/local/lib/python2.7/site-packages/Iris-1.6.1-py2.7.egg/iris/std_names.py

#-------------------------------------------------------------------

# conversion factor= cspecies=M(var)/M(air)=M(var)/28.97g.mol-1
#################################################################### 

def UKCA_callback(cube, field, filename):
    if cube.attributes['STASH'] == 'm01s00i002':
        cube.rename(name='u')

    if cube.attributes['STASH'] == 'm01s00i012':
        cube.rename(name='qcf')

    if cube.attributes['STASH'] == 'm01s00i004':
        cube.rename(name='theta')

    if cube.attributes['STASH'] == 'm01s00i010':
        cube.rename(name='h2o')

    if cube.attributes['STASH'] == 'm01s00i025':
        cube.rename(name='bl_depth')

    if cube.attributes['STASH'] == 'm01s00i408':
        cube.rename(name='p')

    if cube.attributes['STASH'] == 'm01s16i004':
        cube.rename(name='temp')

    if cube.attributes['STASH'] == 'm01s34i150':
        cube.rename(name='aoa')

    if cube.attributes['STASH'] == 'm01s30i201':
        cube.rename(name='u-plevs')

    if cube.attributes['STASH'] == 'm01s30i202':
        cube.rename(name='v-plevs')

    if cube.attributes['STASH'] == 'm01s30i203':
        cube.rename(name='w-plevs')

    if cube.attributes['STASH'] == 'm01s30i451':
        cube.rename(name='trop_p')

    if cube.attributes['STASH'] == 'm01s30i452':
        cube.rename(name='trop_t')

    if cube.attributes['STASH'] == 'm01s30i453':
        cube.rename(name='trop_hgt')

    if cube.attributes['STASH'] == 'm01s34i361':
        cube.rename(name='airmass_trop')

    if cube.attributes['STASH'] == 'm01s34i363':
        cube.rename(name='airmass_atm')

    if cube.attributes['STASH'] == 'm01s34i362':
        cube.rename(name='tropospheric_mask')
#
#    if cube.attributes['STASH'] == 'm01s50i062':
#        cube.rename(name='tropospheric_mask')

#--------------------------------------------------------------
# Tracers UKCA
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i001':
        cube.rename(name='O3')

    if cube.attributes['STASH'] == 'm01s34i002':
        cube.rename(name='NO')

    if cube.attributes['STASH'] == 'm01s34i003':
        cube.rename(name='NO3')

    if cube.attributes['STASH'] == 'm01s34i006':
        cube.rename(name='HONO2')

    if cube.attributes['STASH'] == 'm01s34i008':
        cube.rename(name='H2O2')

    if cube.attributes['STASH'] == 'm01s34i009':
        cube.rename(name='CH4')

    if cube.attributes['STASH'] == 'm01s34i010':
        cube.rename(name='CO')

    if cube.attributes['STASH'] == 'm01s34i011':
        cube.rename(name='HCHO')

    if cube.attributes['STASH'] == 'm01s34i012':
        cube.rename(name='MeOOH')

    if cube.attributes['STASH'] == 'm01s34i014':
        cube.rename(name='C2H6')

    if cube.attributes['STASH'] == 'm01s34i015':
        cube.rename(name='EtOOH')

    if cube.attributes['STASH'] == 'm01s34i016':
        cube.rename(name='MeCHO')

    if cube.attributes['STASH'] == 'm01s34i017':
        cube.rename(name='PAN')

    if cube.attributes['STASH'] == 'm01s34i018':
        cube.rename(name='C3H8')

    if cube.attributes['STASH'] == 'm01s34i021':
        cube.rename(name='EtCOH')

    if cube.attributes['STASH'] == 'm01s34i022':
        cube.rename(name='Me2CO')

    if cube.attributes['STASH'] == 'm01s34i027':
        cube.rename(name='C5H8')

    if cube.attributes['STASH'] == 'm01s34i041':
        cube.rename(name='Cl')

    if cube.attributes['STASH'] == 'm01s34i042':
        cube.rename(name='ClO')

    if cube.attributes['STASH'] == 'm01s34i043':
        cube.rename(name='Cl2O2')

    if cube.attributes['STASH'] == 'm01s34i044':
        cube.rename(name='ClO2')

    if cube.attributes['STASH'] == 'm01s34i045':
        cube.rename(name='Br')

    if cube.attributes['STASH'] == 'm01s34i046':
        cube.rename(name='BrO')

    if cube.attributes['STASH'] == 'm01s34i049':
        cube.rename(name='N2O')

    if cube.attributes['STASH'] == 'm01s34i050':
        cube.rename(name='HCl')

    if cube.attributes['STASH'] == 'm01s34i054':
        cube.rename(name='ClONO2')

    if cube.attributes['STASH'] == 'm01s34i059':
        cube.rename(name='O3P')

    if cube.attributes['STASH'] == 'm01s34i081':
        cube.rename(name='OH')

    if cube.attributes['STASH'] == 'm01s34i082':
        cube.rename(name='HO2')

    if cube.attributes['STASH'] == 'm01s34i149':
        cube.rename(name='PassiveO3')

    if cube.attributes['STASH'] == 'm01s34i151':
        cube.rename(name='O1D')

    if cube.attributes['STASH'] == 'm01s34i152':
        cube.rename(name='NO2')

#--------------------------------------------------------------
#?# unit Dobson? conversion factor
    if cube.attributes['STASH'] == 'm01s34i172':
        cube.rename(name='Ozone_column')
#--------------------------------------------------------------
# Reaction fluxes
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i301':
        cube.rename(name='ox_prod_HO2_NO')

    if cube.attributes['STASH'] == 'm01s34i302':
        cube.rename(name='ox_prod_MeOO_NO')

    if cube.attributes['STASH'] == 'm01s34i303':
        cube.rename(name='ox_prod_NO_RO2')

    if cube.attributes['STASH'] == 'm01s34i304':
        cube.rename(name='ox_prod_OH_inorgAcid')

    if cube.attributes['STASH'] == 'm01s34i305':
        cube.rename(name='ox_prod_OH_orgNitrate')

    if cube.attributes['STASH'] == 'm01s34i306':
        cube.rename(name='ox_prod_orgNitrate_photol')

    if cube.attributes['STASH'] == 'm01s34i307':
        cube.rename(name='ox_prod_OH_PANrxns')

    if cube.attributes['STASH'] == 'm01s34i311':
        cube.rename(name='ox_loss_O1D_H2O')

    if cube.attributes['STASH'] == 'm01s34i312':
        cube.rename(name='ox_loss_minor_rxns')

    if cube.attributes['STASH'] == 'm01s34i313':
        cube.rename(name='ox_loss_HO2_O3')

    if cube.attributes['STASH'] == 'm01s34i314':
        cube.rename(name='ox_loss_OH_O3')

    if cube.attributes['STASH'] == 'm01s34i315':
        cube.rename(name='ox_loss_O3_alkene')

    if cube.attributes['STASH'] == 'm01s34i316':
        cube.rename(name='ox_loss_N2O5_H2O')

    if cube.attributes['STASH'] == 'm01s34i317':
        cube.rename(name='ox_loss_NO3_chemloss')

    if cube.attributes['STASH'] == 'm01s34i321':
        cube.rename(name='ozone_dry_dep_3D')

    if cube.attributes['STASH'] == 'm01s34i322':
        cube.rename(name='noy_dry_dep_3D')

    if cube.attributes['STASH'] == 'm01s34i331':
        cube.rename(name='noy_wet_dep_3D')

#    if cube.attributes['STASH'] == 'm01s50i022':
#        cube.var_name='noy_dry_dep_3D'
#
#    if cube.attributes['STASH'] == 'm01s50i023':
#        cube.var_name='noy_wet_dep_3D'

    if cube.attributes['STASH'] == 'm01s34i341':
        cube.rename(name='ch4+oh')

    if cube.attributes['STASH'] == 'm01s34i348':
        cube.rename(name='ch4+cl')

    if cube.attributes['STASH'] == 'm01s34i351':
        cube.rename(name='STE')

    if cube.attributes['STASH'] == 'm01s34i352':
        cube.rename(name='tendency_ozone_troposphere')

    if cube.attributes['STASH'] == 'm01s34i354':
        cube.rename(name='tendency_ozone_atm')
# ?unit
    if cube.attributes['STASH'] == 'm01s34i353':
        cube.rename(name='tropos_ozone')

    if cube.attributes['STASH'] == 'm01s34i381':
        cube.rename(name='lNOx_ems')

    if cube.attributes['STASH'] == 'm01s34i382':
        cube.rename(name='lNOx_flash')

#--------------------------------------------------------------
# Fixed Oxidants
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i023':
        cube.rename(name='CH4_1')
    if cube.attributes['STASH'] == 'm01s34i026':
        cube.rename(name='CH4_2')
    if cube.attributes['STASH'] == 'm01s34i037':
        cube.rename(name='CH4_3')
    if cube.attributes['STASH'] == 'm01s34i038':
        cube.rename(name='CH4_4')
    if cube.attributes['STASH'] == 'm01s34i039':
        cube.rename(name='CH4_5')
    if cube.attributes['STASH'] == 'm01s34i040':
        cube.rename(name='CH4_6')
    if cube.attributes['STASH'] == 'm01s34i060':
        cube.rename(name='CH4_7')
    if cube.attributes['STASH'] == 'm01s34i061':
        cube.rename(name='CH4_8')
    if cube.attributes['STASH'] == 'm01s34i062':
        cube.rename(name='CH4_9')
    if cube.attributes['STASH'] == 'm01s34i063':
        cube.rename(name='CH4_10')
    if cube.attributes['STASH'] == 'm01s34i064':
        cube.rename(name='CH4_11')
    if cube.attributes['STASH'] == 'm01s34i065':
        cube.rename(name='CH4_12')
    if cube.attributes['STASH'] == 'm01s34i066':
        cube.rename(name='CH4_13')
    if cube.attributes['STASH'] == 'm01s34i067':
        cube.rename(name='CH4_14')
    if cube.attributes['STASH'] == 'm01s34i068':
        cube.rename(name='CH4_15')
    if cube.attributes['STASH'] == 'm01s34i069':
        cube.rename(name='CH4_16')
    if cube.attributes['STASH'] == 'm01s34i071':
        cube.rename(name='CH4_17')
    if cube.attributes['STASH'] == 'm01s34i072':
        cube.rename(name='CH4_18')
    if cube.attributes['STASH'] == 'm01s34i073':
        cube.rename(name='CH4_19')
    if cube.attributes['STASH'] == 'm01s34i074':
        cube.rename(name='CH4_20')
    if cube.attributes['STASH'] == 'm01s34i075':
        cube.rename(name='CH4_21')
    if cube.attributes['STASH'] == 'm01s34i076':
        cube.rename(name='CH4_22')
    if cube.attributes['STASH'] == 'm01s34i077':
        cube.rename(name='CH4_23')
    if cube.attributes['STASH'] == 'm01s34i078':
        cube.rename(name='CH4_24')
    if cube.attributes['STASH'] == 'm01s34i079':
        cube.rename(name='CH4_25')
    if cube.attributes['STASH'] == 'm01s34i091':
        cube.rename(name='CH4_26')
    if cube.attributes['STASH'] == 'm01s34i092':
        cube.rename(name='CH4_27')
    if cube.attributes['STASH'] == 'm01s34i093':
        cube.rename(name='CH4_28')
    if cube.attributes['STASH'] == 'm01s34i096':
        cube.rename(name='CH4_29')
    if cube.attributes['STASH'] == 'm01s34i097':
        cube.rename(name='CH4_30')
    if cube.attributes['STASH'] == 'm01s34i098':
        cube.rename(name='CH4_31')
    if cube.attributes['STASH'] == 'm01s34i099':
        cube.rename(name='CH4_32')
    if cube.attributes['STASH'] == 'm01s34i100':
        cube.rename(name='CH4_33')

    if cube.attributes['STASH'] == 'm01s40i001':
        cube.rename(name='O1Dfix+CH4_1')
    if cube.attributes['STASH'] == 'm01s40i002':
        cube.rename(name='OHfix+CH4_1')
    if cube.attributes['STASH'] == 'm01s40i003':
        cube.rename(name='Clfix+CH4_1')
    if cube.attributes['STASH'] == 'm01s40i004':
        cube.rename(name='O1Dfix+CH4_2')
    if cube.attributes['STASH'] == 'm01s40i005':
        cube.rename(name='OHfix+CH4_2')
    if cube.attributes['STASH'] == 'm01s40i006':
        cube.rename(name='Clfix+CH4_2')
    if cube.attributes['STASH'] == 'm01s40i007':
        cube.rename(name='O1Dfix+CH4_3')
    if cube.attributes['STASH'] == 'm01s40i008':
        cube.rename(name='OHfix+CH4_3')
    if cube.attributes['STASH'] == 'm01s40i009':
        cube.rename(name='Clfix+CH4_3')
    if cube.attributes['STASH'] == 'm01s40i010':
        cube.rename(name='O1Dfix+CH4_4')
    if cube.attributes['STASH'] == 'm01s40i011':
        cube.rename(name='OHfix+CH4_4')
    if cube.attributes['STASH'] == 'm01s40i012':
        cube.rename(name='Clfix+CH4_4')
    if cube.attributes['STASH'] == 'm01s40i013':
        cube.rename(name='O1Dfix+CH4_5')
    if cube.attributes['STASH'] == 'm01s40i014':
        cube.rename(name='OHfix+CH4_5')
    if cube.attributes['STASH'] == 'm01s40i015':
        cube.rename(name='Clfix+CH4_5')
    if cube.attributes['STASH'] == 'm01s40i016':
        cube.rename(name='O1Dfix+CH4_6')
    if cube.attributes['STASH'] == 'm01s40i017':
        cube.rename(name='OHfix+CH4_6')
    if cube.attributes['STASH'] == 'm01s40i018':
        cube.rename(name='Clfix+CH4_6')
    if cube.attributes['STASH'] == 'm01s40i019':
        cube.rename(name='O1Dfix+CH4_7')
    if cube.attributes['STASH'] == 'm01s40i020':
        cube.rename(name='OHfix+CH4_7')
    if cube.attributes['STASH'] == 'm01s40i021':
        cube.rename(name='Clfix+CH4_7')
    if cube.attributes['STASH'] == 'm01s40i022':
        cube.rename(name='O1Dfix+CH4_8')
    if cube.attributes['STASH'] == 'm01s40i023':
        cube.rename(name='OHfix+CH4_8')
    if cube.attributes['STASH'] == 'm01s40i024':
        cube.rename(name='Clfix+CH4_8')
    if cube.attributes['STASH'] == 'm01s40i025':
        cube.rename(name='O1Dfix+CH4_9')
    if cube.attributes['STASH'] == 'm01s40i026':
        cube.rename(name='OHfix+CH4_9')
    if cube.attributes['STASH'] == 'm01s40i027':
        cube.rename(name='Clfix+CH4_9')
    if cube.attributes['STASH'] == 'm01s40i028':
        cube.rename(name='O1Dfix+CH4_10')
    if cube.attributes['STASH'] == 'm01s40i029':
        cube.rename(name='OHfix+CH4_10')
    if cube.attributes['STASH'] == 'm01s40i030':
        cube.rename(name='Clfix+CH4_10')
    if cube.attributes['STASH'] == 'm01s40i031':
        cube.rename(name='O1Dfix+CH4_11')
    if cube.attributes['STASH'] == 'm01s40i032':
        cube.rename(name='OHfix+CH4_11')
    if cube.attributes['STASH'] == 'm01s40i033':
        cube.rename(name='Clfix+CH4_11')
    if cube.attributes['STASH'] == 'm01s40i034':
        cube.rename(name='O1Dfix+CH4_12')
    if cube.attributes['STASH'] == 'm01s40i035':
        cube.rename(name='OHfix+CH4_12')
    if cube.attributes['STASH'] == 'm01s40i036':
        cube.rename(name='Clfix+CH4_12')
    if cube.attributes['STASH'] == 'm01s40i037':
        cube.rename(name='O1Dfix+CH4_13')
    if cube.attributes['STASH'] == 'm01s40i038':
        cube.rename(name='OHfix+CH4_13')
    if cube.attributes['STASH'] == 'm01s40i039':
        cube.rename(name='Clfix+CH4_13')
    if cube.attributes['STASH'] == 'm01s40i040':
        cube.rename(name='O1Dfix+CH4_14')
    if cube.attributes['STASH'] == 'm01s40i041':
        cube.rename(name='OHfix+CH4_14')
    if cube.attributes['STASH'] == 'm01s40i042':
        cube.rename(name='Clfix+CH4_14')
    if cube.attributes['STASH'] == 'm01s40i043':
        cube.rename(name='O1Dfix+CH4_15')
    if cube.attributes['STASH'] == 'm01s40i044':
        cube.rename(name='OHfix+CH4_15')
    if cube.attributes['STASH'] == 'm01s40i045':
        cube.rename(name='Clfix+CH4_15')
    if cube.attributes['STASH'] == 'm01s40i046':
        cube.rename(name='O1Dfix+CH4_16')
    if cube.attributes['STASH'] == 'm01s40i047':
        cube.rename(name='OHfix+CH4_16')
    if cube.attributes['STASH'] == 'm01s40i048':
        cube.rename(name='Clfix+CH4_16')
    if cube.attributes['STASH'] == 'm01s40i049':
        cube.rename(name='O1Dfix+CH4_17')
    if cube.attributes['STASH'] == 'm01s40i050':
        cube.rename(name='OHfix+CH4_17')
    if cube.attributes['STASH'] == 'm01s40i051':
        cube.rename(name='Clfix+CH4_17')
    if cube.attributes['STASH'] == 'm01s40i052':
        cube.rename(name='O1Dfix+CH4_18')
    if cube.attributes['STASH'] == 'm01s40i053':
        cube.rename(name='OHfix+CH4_18')
    if cube.attributes['STASH'] == 'm01s40i054':
        cube.rename(name='Clfix+CH4_18')
    if cube.attributes['STASH'] == 'm01s40i055':
        cube.rename(name='O1Dfix+CH4_19')
    if cube.attributes['STASH'] == 'm01s40i056':
        cube.rename(name='OHfix+CH4_19')
    if cube.attributes['STASH'] == 'm01s40i057':
        cube.rename(name='Clfix+CH4_19')
    if cube.attributes['STASH'] == 'm01s40i058':
        cube.rename(name='O1Dfix+CH4_20')
    if cube.attributes['STASH'] == 'm01s40i059':
        cube.rename(name='OHfix+CH4_20')
    if cube.attributes['STASH'] == 'm01s40i060':
        cube.rename(name='Clfix+CH4_20')
    if cube.attributes['STASH'] == 'm01s40i061':
        cube.rename(name='O1Dfix+CH4_21')
    if cube.attributes['STASH'] == 'm01s40i062':
        cube.rename(name='OHfix+CH4_21')
    if cube.attributes['STASH'] == 'm01s40i063':
        cube.rename(name='Clfix+CH4_21')
    if cube.attributes['STASH'] == 'm01s40i064':
        cube.rename(name='O1Dfix+CH4_22')
    if cube.attributes['STASH'] == 'm01s40i065':
        cube.rename(name='OHfix+CH4_22')
    if cube.attributes['STASH'] == 'm01s40i066':
        cube.rename(name='Clfix+CH4_22')
    if cube.attributes['STASH'] == 'm01s40i067':
        cube.rename(name='O1Dfix+CH4_23')
    if cube.attributes['STASH'] == 'm01s40i068':
        cube.rename(name='OHfix+CH4_23')
    if cube.attributes['STASH'] == 'm01s40i069':
        cube.rename(name='Clfix+CH4_23')
    if cube.attributes['STASH'] == 'm01s40i070':
        cube.rename(name='O1Dfix+CH4_24')
    if cube.attributes['STASH'] == 'm01s40i071':
        cube.rename(name='OHfix+CH4_24')
    if cube.attributes['STASH'] == 'm01s40i072':
        cube.rename(name='Clfix+CH4_24')
    if cube.attributes['STASH'] == 'm01s40i073':
        cube.rename(name='O1Dfix+CH4_25')
    if cube.attributes['STASH'] == 'm01s40i074':
        cube.rename(name='OHfix+CH4_25')
    if cube.attributes['STASH'] == 'm01s40i075':
        cube.rename(name='Clfix+CH4_25')
    if cube.attributes['STASH'] == 'm01s40i076':
        cube.rename(name='O1Dfix+CH4_26')
    if cube.attributes['STASH'] == 'm01s40i077':
        cube.rename(name='OHfix+CH4_26')
    if cube.attributes['STASH'] == 'm01s40i078':
        cube.rename(name='Clfix+CH4_26')
    if cube.attributes['STASH'] == 'm01s40i079':
        cube.rename(name='O1Dfix+CH4_27')
    if cube.attributes['STASH'] == 'm01s40i080':
        cube.rename(name='OHfix+CH4_27')
    if cube.attributes['STASH'] == 'm01s40i081':
        cube.rename(name='Clfix+CH4_27')
    if cube.attributes['STASH'] == 'm01s40i082':
        cube.rename(name='O1Dfix+CH4_28')
    if cube.attributes['STASH'] == 'm01s40i083':
        cube.rename(name='OHfix+CH4_28')
    if cube.attributes['STASH'] == 'm01s40i084':
        cube.rename(name='Clfix+CH4_28')
    if cube.attributes['STASH'] == 'm01s40i085':
        cube.rename(name='O1Dfix+CH4_29')
    if cube.attributes['STASH'] == 'm01s40i086':
        cube.rename(name='OHfix+CH4_29')
    if cube.attributes['STASH'] == 'm01s40i087':
        cube.rename(name='Clfix+CH4_29')
    if cube.attributes['STASH'] == 'm01s40i088':
        cube.rename(name='O1Dfix+CH4_30')
    if cube.attributes['STASH'] == 'm01s40i089':
        cube.rename(name='OHfix+CH4_30')
    if cube.attributes['STASH'] == 'm01s40i090':
        cube.rename(name='Clfix+CH4_30')
    if cube.attributes['STASH'] == 'm01s40i091':
        cube.rename(name='O1Dfix+CH4_31')
    if cube.attributes['STASH'] == 'm01s40i092':
        cube.rename(name='OHfix+CH4_31')
    if cube.attributes['STASH'] == 'm01s40i093':
        cube.rename(name='Clfix+CH4_31')
    if cube.attributes['STASH'] == 'm01s40i094':
        cube.rename(name='O1Dfix+CH4_32')
    if cube.attributes['STASH'] == 'm01s40i095':
        cube.rename(name='OHfix+CH4_32')
    if cube.attributes['STASH'] == 'm01s40i096':
        cube.rename(name='Clfix+CH4_32')
    if cube.attributes['STASH'] == 'm01s40i097':
        cube.rename(name='O1Dfix+CH4_33')
    if cube.attributes['STASH'] == 'm01s40i098':
        cube.rename(name='OHfix+CH4_33')
    if cube.attributes['STASH'] == 'm01s40i099':
        cube.rename(name='Clfix+CH4_33')

#--------------------------------------------------------------
# Emissions
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i451':
        cube.rename(name='ch4_apparent_ems')

    if cube.attributes['STASH'] == 'm01s00i302':
        cube.rename(name='ch4_ems')



