from TASpymca import TASpymca
import time

#if __name__ == "__main__":
    

print("running...")
pymcaApp = TASpymca()
pymcaApp.app.exec()
print("loading data")
pymcaApp.load_datafile()
