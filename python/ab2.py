from PyMca5.PyMcaGui.pymca.PyMcaMain import PyMcaMain
from PyMca5.PyMcaGui import PyMcaQt as qt
#from PyMca5.PyMcaGui.pymca import QDispatcher
#from PyMca5.PyMcaGui.plotting.PlotWindow import PlotWindow as pltwind 

class TASpymca():
    def __init__(self):
        self.datafile_path = '/epics/support/pymca/data/exp798/Datafiles/'
        self.datafile_name = 'HB3_exp0798_scan0090.dat'

        # ONLY PLOT WINDOW
        self.app = qt.QApplication([])
        #self.wind = pltwind(roi=True, fit=True)
        #self.wind.show()
        #app.exec() ?
        
        # FULL PyMca
        self.wind = PyMcaMain()
        self.wind.show()

        self.x_data_name = '' # get from datafile header
        self.y_data_name = '' # get from datafile header

        self.app.exec()

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
