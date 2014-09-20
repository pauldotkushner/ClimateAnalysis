#test_netcdf: create a netcdf file with bogus data
#Paul Kushner
#See netCDF4 documentation at http://unidata.github.io/netcdf4-python/
import netCDF4
import numpy
file=netCDF4.Dataset('test_dataset_unlimited.nc','w',format='NETCDF3_CLASSIC')
xdim = file.createDimension('x',3)
ydim = file.createDimension('y',4)
tdim = file.createDimension('t', None)
xval = file.createVariable('x','f8',('x'))
yval = file.createVariable('y','f8',('y'))
tval = file.createVariable('t','f8',('t'))
data = file.createVariable('data','f8',('t','y','x'))
print 'shape xval, yval, data',numpy.shape(xval),numpy.shape(yval),numpy.shape(data)
xval[:]=[1,2,3]
yval[:]=[-2,0,2,4]
tval[:] = [0.1,0.2,0.3]
data[0,:,:]=[[20,19,18],[17,16,15],[14,13,12],[11,10,9]]
data[1,:,:]=data[0,:,:]*1.1
data[2,:,:]=data[1,:,:]*1.1
print 'shape xval, yval, data',numpy.shape(xval),numpy.shape(yval),numpy.shape(data)
file.close()
#shell commands to test the dataset
#python test_netcdf_create_unlimited.py
#ncdump test_dataset.nc
#ncdump -c test_dataset.nc
#ncdump -h test_dataset.nc
#ncwa -a x test_dataset.nc xave.nc
#ncdump xave.nc
#ncview test_dataset.nc
