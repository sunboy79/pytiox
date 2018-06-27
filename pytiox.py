#!/home/steve/anaconda3/bin/python

import h5py

class TIO_File:
    def __init__(self, filename):
        self.filename = filename
        self.Open()
    
    def Open(self):
        self.f = h5py.File(self.filename,'w')
    
    def Close(self):
        self.f.close()

    def Get_Info(self):
        pass


class TIO_State:

    def __init__(self): 
        pass
    
    def Open(self):
        pass

    def Close(self):
        pass

    def Get_Info(self):
        pass



tiofile = TIO_File("test.h5")
