#test_netcdf: create a netcdf file with bogus data
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
#basic numerical processing in python
import numpy
#open file for writing, use NETCDF3 for compatibility
file=netCDF4.Dataset('test_dataset.nc','w',format='NETCDF3_CLASSIC')
#create x and y dimensions
xdim = file.createDimension('x',3)
ydim = file.createDimension('y',4)
xval = file.createVariable('x','f8',('x'))
yval = file.createVariable('y','f8',('y'))
#follow c indexing conventions
data = file.createVariable('data','f8',('y','x'))
#some descriptive information is output.
print 'shape xval, yval, data',numpy.shape(xval),numpy.shape(yval),numpy.shape(data)
#fill in data values
xval[:]=[1,2,3]
yval[:]=[-2,0,2,4]
data[:,:]=[[20,19,18],[17,16,15],[14,13,12],[11,10,9]]
#closing the file writes it
file.close()
#shell commands to test the dataset
#ncdump test_dataset.nc
#ncdump -c test_dataset.nc
#ncdump -h test_dataset.nc
#ncwa -a x test_dataset.nc xave.nc
#ncdump xave.nc
#ncview test_dataset.nc
