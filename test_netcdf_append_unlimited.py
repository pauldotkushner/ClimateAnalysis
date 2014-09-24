#test_netcdf: create a netcdf file with data representing hypothetical temperature measurements
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
#basic numerical processing in python
import numpy
#open file for appending, use NETCDF3 for compatibility
file=netCDF4.Dataset('temperature_time_record.nc','a',format='NETCDF3_CLASSIC')
tval = file.variables['t']
temperature = file.variables['temperature']
print 'shape tval, temperature',numpy.shape(tval),numpy.shape(temperature)
#Now add information about extra time steps
tval[3],tval[4],tval[5]=numpy.array([8.0,10.0,12.0])
temperature[3,:,:] = temperature[2,:,:]*1.1
temperature[4,:,:] = temperature[3,:,:]*1.2
temperature[5,:,:] = temperature[4,:,:]*0.9
print 'shape tval, temperature',numpy.shape(tval),numpy.shape(temperature)
file.close()
#ncdump temperature_time_record.nc
#ncview temperature_time_record.nc
#added comment
