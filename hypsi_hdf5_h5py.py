#!/usr/bin/python2.7
# print the names of Groups and datatypes
import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt
# HDF Hierarchy
def VisitAllObjects(Group,Path):
    for i in Group.items():
        if isinstance(i[1],h5py.Group):
            VisitAllObjects(i[1],Path+'/'+i[0])
        else:
            DatasetName=Path+'/'+i[0]
            FileInfo[DatasetName]=(Group[DatasetName].shape,
                                   Group[DatasetName].dtype
                                  #, Group[DatasetName].attrs.listitmes()
                                   )
# any HDF file: File, Group, and Dataset

Files=sys.argv[1:] # get file name from screen
# select one file, create a map, datatypes using VisitAllObjects
#Files[0]='data_speed_z5.hdf'

FirstFid=h5py.File(Files[0],'r')

# start dictionary
FileInfo={}



VisitAllObjects(FirstFid,'')
FirstFid.close()

# print dataset paths and info to screen
for (k,v) in FileInfo.items():
    print k,v

# aggregate data

OutputFileId=h5py.File('AggregationData.h5','w')
NumberOfFiles= len(Files)

# here is the meat of the code
# hte outer loop is over datasets, the inner is over all files.

for Dataset in FileInfo.keys():
    AggregationData=np.ndarray(FileInfo[Dataset][0]+(NumberOfFiles,),dtype=FileInfo[Dataset][1])
    for FileNumber in range(NumberOfFiles):
# open file, read data into array and close
        fid= h5py.File(Files[FileNumber],'r')
        AggregationData[...,FileNumber]=fid[Dataset].value
        fid.close()
    Path=Dataset.split('/')
    map((lambda(x): OutputFileId.require_group(x)), Path[i:-1])

#DS=
OutputFileId.create_dataset(Dataset,data=AggregationData, compression=5, chunks=FileInfo[Dataset][0]+(1,))
#[DS.attrs.__setitem__(Attribute[0],Attribute[1]) for Attribute in FileInfo[Dataset][2]]

OutputFileId.close()








