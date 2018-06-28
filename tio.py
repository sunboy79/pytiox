'''@package tio
Module that encapsulates the TIO format with standard HDF plugin.

'''

import h5py

class TIO_File:
'''Class for describing a TIO file object'''
    def __init__(self, filename):
        '''Initialise the TIO_File object'''
        self.filename = filename
        self.states = {}
    
    def Open(self):
        '''Open the file associated with the TIO_File object'''
        self.f = h5py.File(self.filename,'w')
    
    def Close(self):
        '''Close the file associated with the TIO_File object'''
        self.f.close()

    def Get_Info(self):
        '''Return info about the TIO_File object'''
        pass
    
    def Print(self):
        '''Print info to screen about the TIO_File object'''
        print("File {0}".format(self.filename))

    def Create_State(self, statename):
        '''Create a TIO State in the TIO_File object'''
        self.states[statename] = TIO_State(statename)


class TIO_State:
    def __init__(self, name):
        '''Initialise the TIO_State object'''
        self.name = name
        self.meshes = {}
        pass
    
    def Open(self):
        '''Open the TIO_State object'''
        pass

    def Close(self):
        '''Close the TIO_State object'''
        pass

    def Get_Info(self):
        '''Return info about the TIO_State object'''
        pass
    
    def Print(self):
        '''Print info to screen about the TIO_State object'''
        print("State {0}".format(self.name))

    def Create_Mesh(self, meshname):
        '''Create a TIO Mesh to the TIO_State object'''
        self.meshes[meshname] = TIO_Mesh(meshname)

class TIO_Mesh:
    def __init__(self, name):
        '''Initialise the TIO_Mesh object'''
        self.name = name
        self.materials = {}
        self.quants = {}
    
    def Open(self):
        '''Open the TIO_Mesh object'''
        pass

    def Close(self):
        '''Close the TIO_Mesh object'''
        pass
    
    def Get_Info(self):
        '''Return info about the TIO_Mesh object'''
        pass
    
    def Print(self):
        '''Print info to screen about the TIO_Mesh object'''
        print("State {0}".format(self.name))


class TIO_Material:
    def __init__(self, name):
        '''Initialise the TIO_Material object'''
        self.name = name
        self.chunks = {}
    
    def Open(self):
        '''Open the TIO_Material object'''
        pass

    def Close(self):
        '''Close the TIO_Material object'''
        pass
    
    def Get_Info(self):
        '''Return info about the TIO_Material object'''
        pass
    
    def Print(self):
        '''Print info to screen about the TIO_Material object'''
        print("State {0}".format(self.name))


class TIO_Quant:
    def __init__(self, name):
        '''Initialise the TIO_Quant object'''
        self.name = name
        self.chunks = {}
    
    def Open(self):
        '''Open the TIO_Quant object'''
        pass

    def Close(self):
        '''Close the TIO_Quant object'''
        pass
    
    def Get_Info(self):
        '''Return info about the TIO_Quant object'''
        pass
    
    def Print(self):
        '''Print info to screen about the TIO_Quant object'''
        print("State {0}".format(self.name))