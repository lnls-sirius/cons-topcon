#!../../bin/linux-x86_64/TopCon

## You may have to change TopCon to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure("P01", "/dev/tty0100")
asynSetOption("P01", 0, "baud", "38400")
asynSetOption("P01", 0, "bits", "8")
asynSetOption("P01", 0, "parity", "none")
asynSetOption("P01", 0, "stop", "1")

drvAsynSerialPortConfigure("P02", "/dev/tty0200")
asynSetOption("P02", 0, "baud", "38400")
asynSetOption("P02", 0, "bits", "8")
asynSetOption("P02", 0, "parity", "none")
asynSetOption("P02", 0, "stop", "1")

#dbLoadRecords("db/TopCon.db", "DEVICE=PA-RaPS03:PS-Reg-SI01-M, PORT=P01, MASTER=1")

dbLoadRecords("db/TopCon.db",       "DEVICE=Tc, PORT=P01")
dbLoadRecords("db/TopConMaster.db", "DEVICE=Tc, PORT=P01")
dbLoadRecords("db/asynRecord.db",   "P=Tc,R=,PORT=P01,ADDR=,IMAX=,OMAX=")
 
dbLoadRecords("db/TopCon.db",       "DEVICE=Tc2, PORT=P02")
dbLoadRecords("db/asynRecord.db",   "P=Tc2,R=,PORT=P02,ADDR=,IMAX=,OMAX=")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1