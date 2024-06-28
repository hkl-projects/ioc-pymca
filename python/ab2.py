from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
from PyMca5.PyMcaGui.pymca import QDispatcher
from PyMca5.PyMcaGui.plotting.PlotWindow import PlotWindow as pltwind 

class TASpymca():
    def __init__(self):
        self.datafile_path = '/epics/support/pymca/data/exp798/Datafiles/'
        self.datafile_name = 'HB3_exp0798_scan0090.dat'
        self.app = qt.QApplication([])
        self.wind = PyMcaMain()
        self.x_data_name = '' # get from datafile header
        self.y_data_name = '' # get from datafile header

    def load_datafile(self):
        '''
        DEBUG:PyMca5.PyMcaGui.pymca.QDispatcher:ddict = \
            {'event': 'NewSourceSelected', \
            'filter': 'Spec Files (*dat)', \
            'combokey': f'{datafile_name}', \
            'sourcelist': [f'{datafile_path}{datafile_name}']}
        '''
        self.wind.sourceWidget.sourceSelector.openSource(f'{self.datafile_path}{self.datafile_name}')

        #wind.sourceWidget.sourceSelector.update(f'{datafile_path}{datafile_name}')

        #wind.sourceWidget.sourceSelector.actions()
        #wind.sourceWidget.sourceSelector.event()

    def set_xy(self):
        # read in x and y from data header
        pass
        #pltwind.getCurve() # takes 2 args: self, legend #?





# TESTING
'''
from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
from PyMca5.PyMcaCore import Plugin1DBase
app = qt.QApplication([])
wind = PyMcaMain()
wind.sourceWidget.sourceSelector.openSource('/epics/support/pymca/data/exp798/Datafiles/HB3_exp0798_scan0090.dat')
'''



'''
DEBUG:PyMca5.PyMcaGui.io.QSourceSelector:openfile
...
DEBUG:PyMca5.PyMcaCore.PyMcaDirs:got outputDir /home/l3b
DEBUG:PyMca5.PyMcaCore.PyMcaDirs:setting openFilter Spec Files (*dat)
DEBUG:PyMca5.PyMcaCore.PyMcaDirs:getting saveFilter
DEBUG:PyMca5.PyMcaCore.PyMcaDirs:got saveFilter None
DEBUG:PyMca5.PyMcaCore.PyMcaDirs:setting saveFilter Spec Files (*dat)
DEBUG:PyMca5.PyMcaCore.PyMcaDirs:setting inputDir /epics/support/pymca/data/exp799/Datafiles
DEBUG:PyMca5.PyMcaGui.pymca.QDispatcher:_sourceSelectorSlot(self, ddict)
DEBUG:PyMca5.PyMcaGui.pymca.QDispatcher:ddict = {'event': 'NewSourceSelected', 'filter': 'Spec Files (*dat)', 'combokey': 'HB3_exp0799_scan0072.dat', 'sourcelist': ['/epics/support/pymca/data/exp799/Datafiles/HB3_exp0799_scan0072.dat']}
DEBUG:PyMca5.PyMcaIO.specfilewrapper:this does not look as a specfile
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:Checking if the file is TAS Spec
DEBUG:PyMca5.PyMcaIO.specfilewrapper:Recognized as a TAS spec file
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:Starting TAS Spec file parsing
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:READ IN LINE/KEY/VALUE: # scan = 72 # scan 72
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:READ IN LINE/KEY/VALUE: # date = 4/19/2024 # date 4/19/2024
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:READ IN DATE:  ['#D 4/19/2024'] 4/19/2024
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:READ IN LINE/KEY/VALUE: # time = 5:42:48 PM # time 5:42:48 PM
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:READ IN Time:  ['#D 4/19/2024', '#T 5:42:48 PM'] 5:42:48 PM
DEBUG:PyMca5.PyMcaIO.TASSpecFileParser:READ IN LINE/KEY/VALUE: # proposal = 32303 # proposal 32303
...
'''
