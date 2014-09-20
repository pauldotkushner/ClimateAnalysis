#test_netcdf: create a netcdf file with data representing hypothetical temperature measurements
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
#basic numerical processing in python
import numpy
#open file for writing, use NETCDF3 for compatibility
file=netCDF4.Dataset('temperature_time_record.nc','w',format='NETCDF3_CLASSIC')
xdim = file.createDimension('x',3)
ydim = file.createDimension('y',4)
tdim = file.createDimension('t', None)
xval = file.createVariable('x','f4',('x'))
yval = file.createVariable('y','f4',('y'))
#often, time is indicated as a double precision variable
tval = file.createVariable('t','f8',('t'))
temperature = file.createVariable('temperature','f8',('t','y','x'))
print 'shape xval, yval, temperature',numpy.shape(xval),numpy.shape(yval),numpy.shape(temperature)
xval[:]=[1,2,3]
yval[:]=[-2,0,2,4]
tval[:] = [0.1,0.2,0.3]
temperature[0,:,:]=[[20,19,18],[17,16,15],[14,13,12],[11,10,9]]
temperature[1,:,:]=temperature[0,:,:]*1.1
temperature[2,:,:]=temperature[1,:,:]*1.1
print 'shape xval, yval, temperature',numpy.shape(xval),numpy.shape(yval),numpy.shape(temperature)
file.close()
