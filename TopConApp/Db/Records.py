#!/usr/bin/env python
from Common import FTVL, TemplateType

mod_mon = [
    {
        "params": {
            "pv": "$(D):ModMinMaxNom-Mon",
            "param": "getModMinMaxNom",
            "scan": "30 second",
            "nelm": "12",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):ModMinVolt-Mon", "desc": "Voltage Min", "egu": "V"},
            {"pv": "$(D):ModMinCurrent-Mon", "desc": "Current Min", "egu": "A"},
            {"pv": "$(D):ModMinPwr-Mon", "desc": "Power Min", "egu": "kW"},
            {"pv": "$(D):ModMinRes-Mon", "desc": "Resistance Min", "egu": "mOhm"},
            {"pv": "$(D):ModMaxVolt-Mon", "desc": "Voltage Max", "egu": "V"},
            {"pv": "$(D):ModMaxCurrent-Mon", "desc": "Current Max", "egu": "A"},
            {"pv": "$(D):ModMaxPwr-Mon", "desc": "Power Max", "egu": "kW"},
            {"pv": "$(D):ModMaxRes-Mon", "desc": "Resistance Max", "egu": "mOhm"},
            {"pv": "$(D):ModNomVolt-Mon", "desc": "Voltage Nominal", "egu": "V"},
            {"pv": "$(D):ModNomCurrent-Mon", "desc": "Current Nominal", "egu": "A"},
            {"pv": "$(D):ModNomPwr-Mon", "desc": "Power Nominal", "egu": "kW"},
            {"pv": "$(D):ModNomRes-Mon", "desc": "Resistance Nominal", "egu": "mOhm"},
        ],
    },
    {
        "params": {
            "pv": "$(D):Mod-Mon",
            "param": "getModReadings",
            "scan": "5 second",
            "nelm": "5",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):ModOutVolt-Mon", "desc": "Module out voltage", "egu": "V"},
            {"pv": "$(D):ModOutCurrent-Mon", "desc": "Module out current", "egu": "A"},
            {"pv": "$(D):ModOutPwr-Mon", "desc": "Module out power", "egu": "kW"},
            {
                "pv": "$(D):ModResPreset-Mon",
                "desc": "Module resistence preset",
                "egu": "mOhm",
            },
            {
                "pv": "$(D):ModState-Mon",
                "desc": "Module state",
                "type": TemplateType.MBBI_ITEM,
                "onst": "",
                "twst": "POWERUP",
                "frst": "READY",
                "eist": "RUN",
                "nist": "",
                "test": "WARN",
                "tvst": "ERROR",
                "ftst": "STOP",
            },
        ],
    },
    {
        "pv": "$(D):ModControlMode-Mon",
        "desc": "Module control mode",
        "param": "getModControlMode",
        "type": TemplateType.MBBI,
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
    {
        "pv": "$(D):ModVoltageRef-Mon",
        "desc": "Reference val. for voltage",
        "type": TemplateType.ANALOG_GET,
        "param": "getModVoltageRef",
        "egu": "V",
        "prio": "HIGH",
        "scan": "60 second",
    },
    {
        "pv": "$(D):ModCurrentRef-Mon",
        "desc": "Reference val. for current",
        "type": TemplateType.ANALOG_GET,
        "param": "getModCurrentRef",
        "egu": "A",
        "prio": "HIGH",
        "scan": "60 second",
    },
    {
        "pv": "$(D):ModResistanceRef-Mon",
        "desc": "Reference val. for resistance",
        "type": TemplateType.ANALOG_GET,
        "param": "getModResistanceRef",
        "egu": "mOhm",
        "prio": "HIGH",
        "scan": "60 second",
    },
    {
        "pv": "$(D):ModPwrRef-Mon",
        "desc": "Reference val. for power",
        "type": TemplateType.ANALOG_GET,
        "param": "getModPowerRef",
        "egu": "kW",
        "prio": "HIGH",
        "scan": "60 second",
    },
]
mod_get_set = []
sys_get_set = [
    {
        "pv": "$(D):PwrState",
        "desc": "Enable/Disable output voltage",
        "type": TemplateType.BINARY_STS_SEL,
        "znam": "Off",
        "onam": "On",
        "param": "SysOutVoltEnable",
        "prio": "HIGH",
        "scan": "60 second",
    },
    #   {
    #       "pv": "$(D):SysVoltageRef",
    #       "desc": "Reference val. for voltage",
    #       "type": TemplateType.ANALOG_GET_SET,
    #       "param": "SysVoltageRef",
    #       "egu": "V",
    #       "prio": "HIGH",
    #       "scan": "60 second",
    #   },
    {
        "pv": "$(D):SysCurrentRef",
        "desc": "Reference val. for current",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysCurrentRef",
        "egu": "A",
        "prio": "HIGH",
        "scan": "60 second",
    },
    {
        "pv": "$(D):SysResistanceRef",
        "desc": "Reference val. for resistance",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysResistanceRef",
        "egu": "mOhm",
        "prio": "HIGH",
        "scan": "60 second",
    },
    {
        "pv": "$(D):SysPwrRef",
        "desc": "Reference val. for power",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysPowerRef",
        "egu": "kW",
        "prio": "HIGH",
        "scan": "60 second",
    },
    {
        "pv": "$(D):SysVoltSlopeWf-Mon_proc",
        "type": TemplateType.BINARY_FLNK,
        "prio": "LOW",
        "flnk": "$(D):SysVoltSlopeWf-Mon",
        "scan": "60 second",
    },
    {
        "params": {
            "pv": "$(D):SysVoltSlopeWf-Mon",
            "param": "getSlopeVolt",
            "scan": "Passive",
            "nelm": "4",
            "ftvl": FTVL.DOUBLE,
            "prio": "HIGH",
        },
        "items": [
            {
                "pv": "$(D):SysStartupVoltSlopeRaw-RB",
                "desc": "Set values when enabling output volt",
                "egu": "units",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):SysVoltSlopeRaw-RB",
                "desc": "Set values when they are changed",
                "egu": "units",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):SysStartupVoltSlope-RB",
                "desc": "Set values when enabling output volt",
                "egu": "V/ms",
                "prec": "2",
            },
            {
                "pv": "$(D):SysVoltSlope-RB",
                "desc": "Set values when they are changed",
                "egu": "V/ms",
                "prec": "2",
            },
        ],
    },
    {
        "pv": "$(D):SysSlopeVoltMax-Mon",
        "desc": "Voltage slope max",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeVoltMax",
        "egu": "V/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": "30 second",
    },
    {
        "pv": "$(D):SysSlopeVoltMin-Mon",
        "desc": "Voltage slope min",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeVoltMin",
        "egu": "V/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": "30 second",
    },
    {
        "pv": "$(D):SysStartupVoltSlope-SP",
        "desc": "Set values when enabling output volt",
        "type": TemplateType.ANALOG_SET,
        "param": "setSlopeStartupVoltMs",
        "egu": "V/ms",
        "prio": "HIGH",
        "prec": "2",
        "flnk": "$(D):SysStartupVoltSlope-SP_",
    },
    {
        "pv": "$(D):SysStartupVoltSlope-SP_",
        "desc": "Actual setpoint to be sent",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeStartupVoltSp",
        "egu": "V/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": ".5 second",
    },
    {
        "pv": "$(D):SysVoltSlope-SP",
        "desc": "Set values when they are changed",
        "type": TemplateType.ANALOG_SET,
        "param": "setSlopeVoltMs",
        "egu": "V/ms",
        "prio": "HIGH",
        "prec": "2",
    },
    {
        "pv": "$(D):SysVoltSlope-SP_",
        "desc": "Actual setpoint to be sent",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeVoltSp",
        "egu": "V/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": ".5 second",
    },
    {
        "pv": "$(D):SysStartupVoltSlopeRaw-SP",
        "desc": "Set values when enabling output volt",
        "type": TemplateType.LONG_SET,
        "param": "setSlopeStartupVoltRaw",
        "egu": "units",
        "prio": "HIGH",
        "drvh": "32000",
        "drvl": "1",
    },
    {
        "pv": "$(D):SysVoltSlopeRaw-SP",
        "desc": "Set values when they are changed",
        "type": TemplateType.LONG_SET,
        "param": "setSlopeVoltRaw",
        "egu": "units",
        "prio": "HIGH",
        "drvh": "32000",
        "drvl": "1",
    },
    {
        "pv": "$(D):SysWriteVoltSlope-Cmd",
        "desc": "Apply voltage slope settings",
        "type": TemplateType.BO_CMD,
        "param": "cmdSlopeVoltWrite",
        "prio": "HIGH",
        "flnk": "$(D):SysVoltSlopeWf-Mon",
        "diss": "NO_ALARM",
        "disv": "0",
        "high": "0.1",
        "sdis": "$(D):SysWriteVoltSlope-Cmd",
    },
    {
        "pv": "$(D):SysCurrSlopeWf-Mon_proc",
        "type": TemplateType.BINARY_FLNK,
        "prio": "LOW",
        "flnk": "$(D):SysCurrSlopeWf-Mon",
        "scan": "60 second",
    },
    {
        "params": {
            "pv": "$(D):SysCurrSlopeWf-Mon",
            "param": "getSlopeCurrent",
            "scan": "Passive",
            "nelm": "4",
            "ftvl": FTVL.DOUBLE,
            "prio": "HIGH",
        },
        "items": [
            {
                "pv": "$(D):SysStartupCurrSlopeRaw-RB",
                "desc": "Set values when enabling output volt",
                "egu": "units",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):SysCurrSlopeRaw-RB",
                "desc": "Set values when they are changed",
                "egu": "units",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):SysStartupCurrSlope-RB",
                "desc": "Set values when enabling output volt",
                "egu": "A/ms",
                "prec": "2",
            },
            {
                "pv": "$(D):SysCurrSlope-RB",
                "desc": "Set values when they are changed",
                "egu": "A/ms",
                "prec": "2",
            },
        ],
    },
    {
        "pv": "$(D):SysSlopeCurrMax-Mon",
        "desc": "Current slope max",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeCurrentMax",
        "egu": "A/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": "30 second",
    },
    {
        "pv": "$(D):SysSlopeCurrMin-Mon",
        "desc": "Current slope min",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeCurrentMin",
        "egu": "A/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": "30 second",
    },
    {
        "pv": "$(D):SysStartupCurrSlope-SP",
        "desc": "Set values when enabling output current",
        "type": TemplateType.ANALOG_SET,
        "param": "setSlopeStartupCurrentMs",
        "egu": "A/ms",
        "prio": "HIGH",
        "prec": "2",
        "flnk": "$(D):SysStartupCurrSlope-SP_",
    },
    {
        "pv": "$(D):SysStartupCurrSlope-SP_",
        "desc": "Actual setpoint to be sent",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeStartupCurrentSp",
        "egu": "A/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": ".5 second",
    },
    {
        "pv": "$(D):SysCurrSlope-SP",
        "desc": "Set values when they are changed",
        "type": TemplateType.ANALOG_SET,
        "param": "setSlopeCurrentMs",
        "egu": "A/ms",
        "prio": "HIGH",
        "prec": "2",
        "flnk": "$(D):SysCurrSlope-SP_",
    },
    {
        "pv": "$(D):SysCurrSlope-SP_",
        "desc": "Actual setpoint to be sent",
        "type": TemplateType.ANALOG_GET,
        "param": "getSlopeCurrentSp",
        "egu": "A/ms",
        "prio": "HIGH",
        "prec": "2",
        "scan": ".5 second",
    },
    {
        "pv": "$(D):SysStartupCurrSlopeRaw-SP",
        "desc": "Set values when enabling output current",
        "type": TemplateType.LONG_SET,
        "param": "setSlopeStartupCurrentRaw",
        "egu": "units",
        "prio": "HIGH",
        "drvh": "32000",
        "drvl": "1",
    },
    {
        "pv": "$(D):SysCurrSlopeRaw-SP",
        "desc": "Set values when they are changed",
        "type": TemplateType.LONG_SET,
        "param": "setSlopeCurrentRaw",
        "egu": "units",
        "prio": "HIGH",
        "drvh": "32000",
        "drvl": "1",
    },
    {
        "pv": "$(D):SysWriteCurrSlope-Cmd",
        "desc": "Apply current slope settings",
        "type": TemplateType.BO_CMD,
        "param": "cmdSlopeCurrentWrite",
        "prio": "HIGH",
        "flnk": "$(D):SysCurrSlopeWf-Mon",
        "diss": "NO_ALARM",
        "disv": "0",
        "high": "0.1",
        "sdis": "$(D):SysWriteCurrSlope-Cmd",
    },
]

sys_cmd = [
    {
        "pv": "$(D):Save-Cmd",
        "desc": "Save settings to non-volatile memory",
        "type": TemplateType.BO_CMD,
        "param": "cmdStoreParam",
        "prio": "HIGH",
        "diss": "NO_ALARM",
        "high": "0.1",
        "disv": "0",
        "sdis": "$(D):Save-Cmd",
    },
    {
        "pv": "$(D):Reset-Cmd",
        "desc": "Clear Errors and/or warnings",
        "type": TemplateType.BO_CMD,
        "param": "cmdClearErrors",
        "prio": "HIGH",
        "diss": "NO_ALARM",
        "high": "0.1",
        "disv": "0",
        "sdis": "$(D):Reset-Cmd",
    },
]

sys_mon = [
    {
        "params": {
            "pv": "$(D):SysMinMaxNom-Mon",
            "param": "getSysMinMaxNom",
            "scan": "30 second",
            "nelm": "12",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):SysMinVolt-Mon", "desc": "Voltage Min", "egu": "V"},
            {"pv": "$(D):SysMinCurrent-Mon", "desc": "Current Min", "egu": "A"},
            {"pv": "$(D):SysMinPwr-Mon", "desc": "Power Min", "egu": "kW"},
            {"pv": "$(D):SysMinRes-Mon", "desc": "Resistance Min", "egu": "mOhm"},
            {"pv": "$(D):SysMaxVolt-Mon", "desc": "Voltage Max", "egu": "V"},
            {"pv": "$(D):SysMaxCurrent-Mon", "desc": "Current Max", "egu": "A"},
            {"pv": "$(D):SysMaxPwr-Mon", "desc": "Power Max", "egu": "kW"},
            {"pv": "$(D):SysMaxRes-Mon", "desc": "Resistance Max", "egu": "mOhm"},
            {"pv": "$(D):SysNomVolt-Mon", "desc": "Voltage Nominal", "egu": "V"},
            {"pv": "$(D):SysNomCurrent-Mon", "desc": "Current Nominal", "egu": "A"},
            {"pv": "$(D):SysNomPwr-Mon", "desc": "Power Nominal", "egu": "kW"},
            {"pv": "$(D):SysNomRes-Mon", "desc": "Resistance Nominal", "egu": "mOhm"},
        ],
    },
    {
        "params": {
            "pv": "$(D):Sys-Mon",
            "param": "getSysReadings",
            "scan": "5 second",
            "nelm": "5",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Voltage-Mon", "desc": "System out voltage", "egu": "V"},
            {"pv": "$(D):SysOutCurrent-Mon", "desc": "System out current", "egu": "A"},
            {"pv": "$(D):SysOutPwr-Mon", "desc": "System out power", "egu": "kW"},
            {
                "pv": "$(D):SysResPreset-Mon",
                "desc": "System resistence preset",
                "egu": "mOhm",
            },
            {
                "pv": "$(D):OpMode-Sts",
                "desc": "System state",
                "type": TemplateType.MBBI_ITEM,
                "onst": "",
                "twst": "POWERUP",
                "frst": "READY",
                "eist": "RUN",
                "nist": "",
                "test": "WARN",
                "tvst": "ERROR",
                "ftst": "STOP",
            },
        ],
    },
    {
        "pv": "$(D):SysControlMode-Mon",
        "param": "getSysControlMode",
        "desc": "System control mode",
        "type": TemplateType.MBBI,
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]


temperature = {
    "params": {
        "pv": "$(D):T-Mon",
        "param": "getTemperatures",
        "scan": "5 second",
        "nelm": "3",
        "ftvl": FTVL.DOUBLE,
    },
    "items": [
        {"pv": "$(D):IGBTT-Mon", "desc": "IGBT temperature", "egu": "C"},
        {"pv": "$(D):RectifierT-Mon", "desc": "Rectifier temperature", "egu": "C"},
        {"pv": "$(D):PCBT-Mon", "desc": "PCB temperature", "egu": "C"},
    ],
}


generic_mon = [
    {
        "pv": "$(D):Properties-Cte",
        "type": TemplateType.WF_STRING_STATIC,
        "nelm": "6000",
    },
    {
        "pv": "$(D):ActiveInterface-Mon",
        "desc": "Active interface",
        "scan": "60 second",
        "type": TemplateType.MBBI,
        "param": "getControlInput",
        "zrst": "Analog/Digital Inputs",
        "onst": "HMI/HME",
        "twst": "RS232",
        "thst": "",
        "frst": "",
        "frvl": "",
    },
    {
        "pv": "$(D):DCLinkVolt-Mon",
        "desc": "DC link voltage measure",
        "param": "getDCLinkVoltage",
        "egu": "V",
        "scan": "5 second",
    },
    {
        "pv": "$(D):PrimaryCurr-Mon",
        "desc": "Transformer primary current",
        "param": "getPrimaryCurrent",
        "egu": "A",
        "scan": "5 second",
    },
    {
        "pv": "$(D):ModuleID-Mon",
        "desc": "Module ID - switch",
        "param": "getModuleID",
        "scan": "60 second",
        "type": TemplateType.LONG_IN,
    },
    {
        "pv": "$(D):DSPVer-Mon",
        "desc": "DSP Firmware Version",
        "param": "getDSPVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):PLDVer-Mon",
        "desc": "PLD Firmware Version",
        "param": "getPLDVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):IBCVer-Mon",
        "desc": "IBC Firmware Version",
        "param": "getIBCVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):BootloaderVer-Mon",
        "desc": "Bootloader Version",
        "param": "getBootloaderVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):DLLVer-Mon",
        "desc": "DLL Version",
        "param": "getDLLVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):OperatingTime-Mon",
        "desc": "Actual operating hour counter",
        "param": "getOperatingSeconds",
        "scan": "60 second",
        "type": TemplateType.LONG_IN,
        "egu": "s",
    },
    {
        "pv": "$(D):PowerUpTime-Mon",
        "desc": "Operating hour counter at powerup",
        "param": "getPowerupTimeSeconds",
        "scan": "60 second",
        "type": TemplateType.LONG_IN,
        "egu": "s",
    },
]

generic_cmd = [
    {
        "pv": "$(D):Connect-Cmd",
        "desc": "Attempt to connect to the device",
        "type": TemplateType.BO_CMD,
        "param": "cmdConnect",
        "prio": "HIGH",
        "diss": "NO_ALARM",
        "high": "0.1",
        "disv": "0",
        "sdis": "$(D):Connect-Cmd",
    },
    {
        "pv": "$(D):Disconnect-Cmd",
        "desc": "Disconnect from device",
        "type": TemplateType.BO_CMD,
        "param": "cmdDisconnect",
        "prio": "HIGH",
        "diss": "NO_ALARM",
        "high": "0.1",
        "disv": "0",
        "sdis": "$(D):Disconnect-Cmd",
    },
    {
        "pv": "$(D):ReadErrors-Cmd",
        "desc": "Read Errors from TC",
        "type": TemplateType.BO_CMD,
        "param": "cmdReadErrors",
        "prio": "HIGH",
        "diss": "NO_ALARM",
        "high": "0.1",
        "disv": "0",
        "sdis": "$(D):ReadErrors-Cmd",
    },
]

generic_get_set = [
    {
        "pv": "$(D):ErrorHistory-Mon",
        "param": "getFlashErrorHistory",
        "scan": "Passive",
        "nelm": "300",
        "ftvl": FTVL.STRING,
        "prio": "HIGH",
        "type": TemplateType.WF_STRING_DB,
    },
    # {
    #     "pv": "$(D):ErrorHistory-Mon_pact",
    #     "type": TemplateType.IS_ACTIVE,
    #     "inpa": "$(D):ErrorHistory-Mon.PACT",
    #     "inpb": "$(D):ErrorHistory-Mon",
    #     "desc": "Is reading?",
    #     "scan": "1 second",
    # },
    {
        "pv": "$(D):ErrorHistoryMax",
        "desc": "Maximum entries from error history",
        "type": TemplateType.LONG_GET_SET,
        "param": "FlashErrorHistoryMax",
        "prio": "HIGH",
        "scan": "1 second",
    },
    {
        "pv": "$(D):AutoReconnect",
        "desc": "Enable/Disable auto reconnect to device",
        "type": TemplateType.BINARY_GET_SET,
        "param": "AutoReconnect",
        "onam": "Enable",
        "znam": "Disable",
        "prio": "HIGH",
        "scan": "60 second",
    },
]
