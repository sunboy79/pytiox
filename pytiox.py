#!/home/steve/anaconda3/bin/python

import h5py

class TIO_File:
    def __init__(self, filename):
        self.filename = filename
        self.Open()
    
    def Open(self): pass
        self.f = h5py.File(self.filename,'w')
    
    def Close(self): pass
        self.f.close()

tiofile = TIO_File("test.h5")
