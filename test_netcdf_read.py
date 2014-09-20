#test_netcdf: create a netcdf file with bogus data
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
import numpy
import pylab
file=netCDF4.Dataset('test_dataset_unlimited.nc')
xval = file.variables['x'][:]
yval = file.variables['y'][:]
tval = file.variables['t'][:]
data = file.variables['data'][:]
print 'shape xval, yval, data',numpy.shape(xval),numpy.shape(yval),numpy.shape(data)
pylab.figure(1)
pylab.subplot(2,1,1)
pylab.plot(xval,data[2,:],'r')
pylab.plot(xval,data[0,:],'b')
pylab.subplot(2,1,2)
pylab.contourf(xval,yval,pylab.squeeze(data[2,:,:]))
pylab.colorbar()
show()
