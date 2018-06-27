#!/home/steve/anaconda3/bin/python

import h5py

class TIO_File:
    def __init__(self, filename):
        self.filename = filename
        self.states = {}
    
    def Open(self):
        self.f = h5py.File(self.filename,'w')
    
    def Close(self):
        self.f.close()

    def Get_Info(self):
        pass
    
    def Print(self):
        print("File {0}".format(self.filename))

    def Add_State(self, statename):
        self.states[statename] = TIO_State(statename)


class TIO_State:
    def __init__(self, name):
        self.name = name 
        pass
    
    def Open(self):
        pass

    def Close(self):
        pass

    def Get_Info(self):
        pass
    
    def Print(self):
        print("State {0}".format(self.name))

class TIO_Mesh:
    def __init__(self, name):
        pass

tiofile = TIO_File("test.h5")
tiofile.Add_State("state001")

tiofile.Print()
tiofile.states["state001"].Print()