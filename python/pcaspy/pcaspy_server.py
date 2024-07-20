import os
import threading

import random

from pcaspy import Driver, SimpleServer, Severity

prefix = 'HB3:'
pvdb = {
    # Test PV
    'RAND' : {'prec' : 3, 'scan' : 1},

    # acquisition control and status
    'Acquire': {
        'type': 'enum',
        'enums': ['Stop', 'Start'],
        'asyn': True
    },

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
    'FileTemplate':       {'type': 'str', 'type': 'str', 'value': '%s%04d%s'},
    'AutoIncrement':      {'type': 'enum', 'enums': ['No', 'Yes'], 'value': 1},
    'AutoSave':           {'type': 'enum', 'enums': ['No', 'Yes'], 'value': 1},
    'FullFileName_RBV':   {'type': 'char', 'count': 256},
    'FilePathExists_RBV': {'type': 'enum', 'enums': ['No', 'Yes'],
        'states': [Severity.MAJOR_ALARM, Severity.NO_ALARM]},
    'FileExists_RBV': {'type': 'enum', 'enums': ['No', 'Yes'],
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
    
    def write(self, reason, value):
        status = True
        # take proper actions
        if reason == 'Acquire':
            self.setParam(reason, value)
            print("Start PyMca, read spectrum file")

            # Read Spec file
            fileExists = self.getParam('FileExists_RBV')
            fileName = self.getParam('FullFileName_RBV')
            if fileExists:
                str = open(fileName, 'r').read()
                self.setParam('SpecFile', str)

#            self.setParam('Acquire', 0)
##           self.callbackPV('Acquire')

        if reason == 'FilePath':
            self.setParam(reason, value)
            self.setParam('FilePathExists_RBV',
                    os.path.exists(value) and os.access(value, os.R_OK))
        if reason == 'FileName':
            self.setParam(reason,value)
        if reason == 'FileNumber':
            self.setParam(reason, value)
        if reason == 'FileTemplate':
            self.setParam(reason, value)
        if reason == 'FileExtension':
            self.setParam(reason, value)

        path = self.getParam('FilePath')
        name = self.getParam('FileName')
        number = self.getParam('FileNumber')
        template = self.getParam('FileTemplate')
        extension = self.getParam('FileExtension')
        increment = self.getParam('AutoIncrement')
        autoSave = self.getParam('AutoSave')

        fullFileName = os.path.join(path, template % (name, number, extension))
        self.setParam('FullFileName_RBV', fullFileName)
        self.setParam('FileExists_RBV',
                      os.path.exists(fullFileName) and os.access(fullFileName, os.R_OK))

        self.updatePVs()

        #status = False
        return status

if __name__ == '__main__':
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = PyMcaDriver()
    while True:
        server.process(0.1)

    
