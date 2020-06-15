#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD07
drvAsynIPPortConfigure("P7","unix:///var/tmp/REG07")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
