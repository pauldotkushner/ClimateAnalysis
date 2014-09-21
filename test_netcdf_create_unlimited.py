#test_netcdf: create a netcdf file with data representing hypothetical temperature measurements
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
#time module for time stamps
import time
#basic numerical processing in python
import numpy
#open file for writing, use NETCDF3 for compatibility
file=netCDF4.Dataset('temperature_time_record.nc','w',format='NETCDF3_CLASSIC')
#create x,y,t dimensions and make the time dimension unlimited
xdim = file.createDimension('x',3)
ydim = file.createDimension('y',4)
tdim = file.createDimension('t', None)

xval = file.createVariable('x','f4',('x'))
yval = file.createVariable('y','f4',('y'))
#often, time is indicated as a double precision variable
tval = file.createVariable('t','f8',('t'))
temperature = file.createVariable('temperature','f4',('t','y','x'))

#Now add some attributes to the data
file.description = 'Temperature time series from lab sensor, created ', time.ctime(time.time())
xval.units = 'mm'
yval.units = 'mm'
tval.units = 's'
temperature.units = 'degC'

#Now populate the data array
print 'shape xval, yval, temperature',numpy.shape(xval),numpy.shape(yval),numpy.shape(temperature)
#x position in mm
xval[:]=numpy.array([1.0,2.0,3.0])
#y position in mm
yval[:]=numpy.array([-2.0,0.0,2.0,4.0])
#time in s
tval[:] = numpy.array([2.0,4.0,6.0])
#simulated experiment where data is getting warmer
#first time step
temperature[0,:,:]=numpy.array([[20.0,19.5,18.0],[17.0,16.5,15.0],[14.0,13.0,12.5],[11.0,10.5,9.0]])
#second time step
temperature[1,:,:]=temperature[0,:,:]*1.1
#third time step
temperature[2,:,:]=temperature[1,:,:]*1.2
print 'shape xval, yval, temperature',numpy.shape(xval),numpy.shape(yval),numpy.shape(temperature)
file.close()
