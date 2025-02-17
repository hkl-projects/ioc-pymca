import os
import threading

import random

from pcaspy import Driver, SimpleServer, Severity

DETECTOR_ID = 0

prefix = 'HB3:'
# prefix = 'MTEST:'
pvdb = {
    # Test PV
    'RAND' : {'prec' : 3,'scan' : 1},

    # Spectra data descriptors
    'NColumns_RBV':  {'type': 'int'},
    'NRows_RBV':     {'type': 'int'},

    'DetX_RBV':     {'type': 'char', 'count': 32},
    'DetY_RBV':     {'type': 'char', 'count': 32},
    'NdetX':        {'type': 'int'},
    'NdetY':        {'type': 'int'},

    'ColHeaders_RBV':   {'type': 'char', 'count': 256},
    'SpecFile':         {'type': 'char', 'count': 6553600},

    # File I/O control
    'FilePath':           {'type': 'char', 'count': 128},
    'FileName':           {'type': 'char', 'count': 128, 'value': 'test'},
    'FileNumber':         {'type': 'int'},
    'FileExtension':      {'type': 'char', 'count': 24, 'value': '.dat'},
    #'FileTemplate':       {'type': 'str', 'value': '%s_%04d.dat'},
    'FileTemplate':       {'type': 'str', 'type': 'str', 'value': '%s%d%s'},
    'AutoIncrement':      {'type': 'enum', 'enums': ['No', 'Yes'], 'value': 1},
    'AutoSave':           {'type': 'enum', 'enums': ['No', 'Yes'], 'value': 1},
    'FullFileName_RBV':   {'type': 'char', 'count': 256},
    'FilePathExists_RBV': {'type': 'enum', 'enums': ['No', 'Yes'],
        'states': [Severity.MAJOR_ALARM, Severity.NO_ALARM]},

    # Scan windows Info
    'Peak_RBV':     {'type': 'int'},
    'PeakAt_RBV':   {'type': 'int'},
    'FWHM_RBV':     {'type': 'int'},
    'FWHMat_RBV':   {'type': 'int'},    
    'Com_RBV':      {'type': 'int'},
    'Mean_RBV':     {'type': 'int'},
    'Std_RBV':      {'type': 'int'},
    'Min_RBV':      {'type': 'int'},
    'Max_RBV':      {'type': 'int'},
    'Delta_RBV':    {'type': 'int'},    
}

class PyMcaDriver(Driver):
    def __init__(self):
    #    super(PyMcaDriver, self).__init__()
        Driver.__init__(self)
    
    def read(self, reason):
        if reason == 'RAND':
            value = random.random()
        else:
            value = self.getParam(reason)
        return value
    
#    def readFile(self, reason, value):
    def readFile(self):        
        path = self.getParam('FilePath')
        name = self.getParam('FileName')
        number = self.getParam('FileNumber')
        template = self.getParam('FileTemplate')
        extension = self.getParam('FileExtension')
        increment = self.getParam('AutoIncrement')
        auto_save = self.getParam('AutoSave')

        fullFileName = os.path.join(path, template % (name, number, extension))
        self.setParam('FullFileName_RBV', fullFileName)
        self.updatePVs()
        print("read file")

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = PyMcaDriver()
    while True:
        server.process(0.1)
        driver.readFile()
    
