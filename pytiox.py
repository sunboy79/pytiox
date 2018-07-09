#!/home/steve/anaconda3/bin/python

import tio


tiofile = tio.TIO_File("test.h5")
print(tiofile)
tiofile.Set_Info("thor","3.0.2","test calculation")
tiofile.Print()
tiofile.Open('w')
tiofile.Write()
tiofile.Close()
