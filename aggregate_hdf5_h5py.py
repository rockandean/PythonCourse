#!/usr/bin/python2.7
# aggregate Bx from data_speed_z4 and data_speed_z5
import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt

Files=sys.argv[1:] # get file name from screen
# select one file, create a map, datatypes using VisitAllObjects
#Files[0]='data_speed_z5.hdf'

FirstFid=h5py.File(Files[0],'r')



# process failed: mocing into plotting toghether
