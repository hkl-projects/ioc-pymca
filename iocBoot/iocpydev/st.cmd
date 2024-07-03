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

pydev("import ab2")
pydev("pymca_window = ab2.TASpymca()")
pydev("pymca_window.load_datafile()")
