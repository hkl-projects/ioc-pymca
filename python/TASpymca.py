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
        # ONLY PLOT WINDOW
        self.app = qt.QApplication([])
        #self.wind = pltwind(roi=True, fit=True)
        #self.wind.show()
        
        # FULL PyMca
        self.wind = PyMcaMain()
        self.wind.show()
        #self.set_datafile()
        #self.load_datafile()

        #self.x_data_name = '' # get from datafile header
        #self.y_data_name = '' # get from datafile header

        #self.set_window()

        self.app.exec()


    def load_datafile(self):

        self.wind.sourceWidget.sourceSelector.openSource(self.fname)
 
        #wind.sourceWidget.sourceSelector.update(f'{datafile_path}{datafile_name}')

        #wind.sourceWidget.sourceSelector.actions()
        #wind.sourceWidget.sourceSelector.event()


    def set_datafile(self):
        self.datafile_path = input("Enter datafile path, (ex// /home/l3b/Desktop/") 
        self.datafile_name = input("Enter datafile name (ex// scan001.dat")       
        self.fname = os.path.join(PyMcaDataDir.PYMCA_DATA_DIR, f'{self.datafile_path}{self.datafile_name}')

    def set_xy(self):
        # read in x and y from data header
        pass
        #pltwind.getCurve() # takes 2 args: self, legend #?

    def get_graphinfo(self):
        self.info = wind.scanWindow.scanWindowInfoWidget
        print(self.info.getInfo())

    def set_window(self):
        '''
        possibly helpful:

        DEBUG:PyMca5.PyMcaGui.pymca.QDispatcher:ddict = \
            {'event': 'NewSourceSelected', \
            'filter': 'Spec Files (*dat)', \
            'combokey': f'{datafile_name}', \
            'sourcelist': [f'{datafile_path}{datafile_name}']}
        
        wind.dispatcherAddSelectionSlot([...])

        wind.scanWindow._curveList
        wind.scanWindow.showCurves()
        wind.scanWindow.repaint()
        wind.scanWindow.setActiveCurve()

        app.processEvents()

        from PyMca5.PyMcaGui.pymca.ScanWindowInfoWidget import GraphInfoWidget
        info = GraphInfoWidget(wind)
        #info.fwhmAt...
        print(info.getInfo())

        
        from PyMca5.PyMcaGui.pymca import ScanWindowInfoWidget
        scan = ScanWindowInfoWidget.ScanWindowInfoWidget(wind)
        print(scan.getInfo())

        for child in wind.children():
            if isinstance(child, qt.QWidget) and child.metaObject().className() == 'ScanWindowInfoWidget':
                info_widget = child

        #info_widget. <tab>
        info_widget.children()

        labels = info_widget.findChildren(qt.QLabel)
        line_edits = info_widget.findChildren(qt.QLineEdit)

        for label in labels:
            print("QLabel:", label.text())

        for line_edit in line_edits:
            print("QLineEdit:", line_edit.text())

        '''       
        self.wind.dispatcherOtherSignalsSlot({
            'SourceName': [f'{self.fname}'],
            'SourceType': 'SpecFile',
            'event': 'SelectionTypeChanged',
            'SelectionType': 'Counters'
            })
            


