import tables as tb

filename="data_speed_z5.hdf"
f=tb.openFile(filename,"a")
f.root
f.root.TimeStep
