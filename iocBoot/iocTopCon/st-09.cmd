#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD09
drvAsynIPPortConfigure("P9","unix:///var/tmp/REG09")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
