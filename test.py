#!/usr/bin/python2.7
import numpy as np
import matplotlib.pyplot as plt
import h5py

# read HDF files
fid1=h5py.File('data_speed_z4.hdf','r')
fid2=h5py.File('data_speed_z6.hdf','r')

a=fid1['/TimeStep/10/ZoneFields/Bx']
b=fid2['/TimeStep/10/ZoneFields/Bx']


