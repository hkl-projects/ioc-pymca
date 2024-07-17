from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
from PyMca5.PyMcaGui.pymca.ScanWindowInfoWidget import GraphInfoWidget
from PyMca5 import PyMcaDataDir
#from PyMca5.PyMcaGui.pymca import QDispatcher
#from PyMca5.PyMcaGui.plotting.PlotWindow import PlotWindow as pltwind 
import epics
import os
 
class TASpymca():
    def __init__(self):
        self.datafile_path = '/epics/support/pymca/data/exp798/Datafiles/'
        self.datafile_name = 'HB3_exp0798_scan0090.dat'
        self.fname = os.path.join(PyMcaDataDir.PYMCA_DATA_DIR, f'{self.datafile_path}{self.datafile_name}')
        self.app = qt.QApplication([])
        self.wind = PyMcaMain()
        self.wind.show()
 
 
    def load_datafile(self):
        self.wind.sourceWidget.sourceSelector.openSource(self.fname)
 
    def set_datafile(self):
        self.datafile_path = input("Enter datafile path, (ex// /home/l3b/Desktop/")
        self.datafile_name = input("Enter datafile name (ex// scan001.dat")
        self.fname = os.path.join(PyMcaDataDir.PYMCA_DATA_DIR, f'{self.datafile_path}{self.datafile_name}')
 
    def set_xy(self):
        pass
 
    def get_graphinfo(self):
        self.info = wind.scanWindow.scanWindowInfoWidget
        print(self.info.getInfo())
 
    def set_window(self):
        self.wind.dispatcherOtherSignalsSlot({
            'SourceName': [f'{self.fname}'],
            'SourceType': 'SpecFile',
            'event': 'SelectionTypeChanged',
            'SelectionType': 'Counters'
            })