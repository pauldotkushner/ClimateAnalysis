#april_zonal_mean.py: do some temperature analysis and save to a netcdf file.
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
import numpy
fname = "air.mon.mean.nc"
f_in=netCDF4.Dataset(fname,'r')
f_out = netCDF4.Dataset('from_python.zm.tm.april.'+fname,'w',format='NETCDF3_CLASSIC')
f_out.createDimension('level',len(f_in.variables['level']))
f_out.createDimension('lat',len(f_in.variables['lat']))
f_out.createVariable('level','f4',('level'))
f_out.createVariable('lat','f4',('lat'))
f_out.createVariable('air','f4',('level','lat'))
for var in ['lat','level','air']:
    f_out.variables[var].units = f_in.variables[var].units

april_temp = f_in.variables['air'][3::12,:,:,:]
zm_april_temp = numpy.mean(april_temp,3)
tm_zm_april_temp = numpy.mean(zm_april_temp,0)

f_out.variables['level'][:] = f_in.variables['level'][:]
f_out.variables['lat'][:] = f_in.variables['lat'][:]
f_out.variables['air'][:] = tm_zm_april_temp
f_out.close()
