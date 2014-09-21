#test_netcdf: create a netcdf file with bogus data
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
import numpy
import pylab
pylab.ion() 
file=netCDF4.Dataset('temperature_time_record.nc')
xval = file.variables['x']
yval = file.variables['y']
tval = file.variables['t']
data = file.variables['temperature']
print 'shape xval, yval, data',numpy.shape(xval),numpy.shape(yval),numpy.shape(data)
pylab.figure(1)
pylab.subplot(2,1,1)
pylab.plot(xval,data[0,2,:],'r')
pylab.plot(xval,data[1,2,:],'b')
pylab.legend(('time %3.1f s'%tval[0],'time %3.1f'%tval[1]))
pylab.title('temperature for y=%3.1f %s'%(yval[2],yval.units))
pylab.xlabel('x(%s)'%xval.units)
pylab.ylabel('t(%s)'%tval.units)
pylab.subplot(2,1,2)
pylab.contourf(xval,yval,data[2,:,:])
pylab.title('Temperature(%s) at time %3.1f %s'%(data.units,tval[2],tval.units))
pylab.xlabel('x(%s)'%xval.units)
pylab.ylabel('y(%s)'%yval.units)
pylab.colorbar()
pylab.show()
