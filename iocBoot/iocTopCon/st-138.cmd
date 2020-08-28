#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/db/Security.as")

drvAsynIPPortConfigure("P138","$(REGATRON_INTERFACE_MS_HOST):20138")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P138")

cd "${TOP}/iocBoot/${IOC}"
iocInit
iocLogInit

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
