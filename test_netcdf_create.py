#test_netcdf: create a netcdf file with data representing hypothetical temperature measurements
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
#basic numerical processing in python
import numpy
#open file for writing, use NETCDF3 for compatibility
file=netCDF4.Dataset('first_temperature_dataset.nc','w',format='NETCDF3_CLASSIC')
#create x and y dimensions
xdim = file.createDimension('x',3)
ydim = file.createDimension('y',4)
xval = file.createVariable('x','f4',('x'))
yval = file.createVariable('y','f4',('y'))
#follow c indexing conventions
temperature = file.createVariable('temperature','f4',('y','x'))
#some descriptive information is output.
print 'shape xval, yval, temperature',numpy.shape(xval),numpy.shape(yval),numpy.shape(temperature)
#fill in data values
#x position in mm
xval[:]=numpy.array([1.0,2.0,3.0])
#y position in mm
yval[:]=numpy.array([-2.0,0.0,2.0,4.0])
#temperature data in degrees C
temperature[:,:]=numpy.array([[20.0,19.5,18.0],[17.0,16.5,15.0],[14.0,13.0,12.5],[11.0,10.5,9.0]])
#closing the file writes it
file.close()
#shell commands to test the dataset
#ncdump first_temperature_dataset.nc | more
#print header and coordinate information
#ncdump -c first_temperature_dataset.nc | more
#print just header information
#ncdump -h first_temperature_dataset.nc | more
#ncks -d x,2.0 first_temperature_dataset.nc extract_x.nc
#ncdump  extract_x.nc
#ncks -d x,2.0,3.0 -d y,0.0,4.0 first_temperature_dataset.nc extract_xy.nc
#ncwa -a x extract_xy.nc x_mean-extract_xy.nc
#etc.
