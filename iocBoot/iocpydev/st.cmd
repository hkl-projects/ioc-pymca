#!../../bin/linux-x86_64/pydevioc

< envPaths

# PYTHONPATH points to folders where Python modules are.
epicsEnvSet("PYTHONPATH","$(TOP)/python")

cd ${TOP}

## Register all support components
dbLoadDatabase "${TOP}/dbd/pydevioc.dbd"
pydevioc_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("${TOP}/db/pymca.db")

cd ${TOP}/iocBoot/${IOC}

# temporary, will replace with a PV that launches pymca
pydev("import TASpymca")
pydev("pymca_window = TASpymca.TASpymca()")
pydev("pymca_window.load_datafile()")
