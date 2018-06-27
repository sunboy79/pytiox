#!/home/steve/anaconda3/bin/python

import tio


tiofile = tio.TIO_File("test.h5")
tiofile.Add_State("state001")

tiofile.Print()
tiofile.states["state001"].Print()