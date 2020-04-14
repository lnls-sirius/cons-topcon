#!/usr/bin/env python
from Common import FTVL

mod_mon = [
    {
        "params": {
            "pv": "$(D):Mod-Mon",
            "param": "getSysReadings",
            "scan": "",
            "nelm": "5",
            "type": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Mod-OutVolt-Mon", "desc": "Module out voltage", "egu": "V"},
            {"pv": "$(D):Mod-OutCurrent-Mon", "desc": "Module out current", "egu": "A"},
            {"pv": "$(D):Mod-OutPwr-Mon", "desc": "Module out power", "egu": "kW"},
            {
                "pv": "$(D):Mod-ResPreset-Mon",
                "desc": "Module resistence preset",
                "egu": "mOhm",
            },
            {
                "pv": "$(D):Mod-State-Mon",
                "desc": "Module state",
                "type": "mbbi",
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
        "pv": "$(D):Mod-ControlMode-Mon",
        "desc": "Module control mode",
        "param": "getModControlMode",
        "type": "mbbi",
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]
sys_get_set = []

sys_cmd = [
    {
        "pv": "$(D):Save-Cmd",
        "desc": "Save settings to non-volatile memory",
        "type": "bo_cmd",
        "param": "cmdStoreParam",
    },
    {
        "pv": "$(D):Clear-Cmd",
        "desc": "Clear Errors and/or warnings",
        "type": "bo_cmd",
        "param": "cmdClearErrors",
    },
]

sys_mon = [
    {
        "params": {
            "pv": "$(D):Sys-Mon",
            "param": "getSysReadings",
            "scan": "",
            "nelm": "5",
            "type": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Sys-OutVolt-Mon", "desc": "System out voltage", "egu": "V"},
            {"pv": "$(D):Sys-OutCurrent-Mon", "desc": "System out current", "egu": "A"},
            {"pv": "$(D):Sys-OutPwr-Mon", "desc": "System out power", "egu": "kW"},
            {
                "pv": "$(D):Sys-ResPreset-Mon",
                "desc": "System resistence preset",
                "egu": "mOhm",
            },
            {
                "pv": "$(D):Sys-State-Mon",
                "desc": "System state",
                "type": "mbbi",
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
        "pv": "$(D):Sys-ControlMode-Mon",
        "param": "getSysControlMode",
        "desc": "System control mode",
        "type": "mbbi",
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]


temp = {
    "params": {
        "pv": "$(D):T-Mon",
        "param": "getTemperatures",
        "scan": "",
        "nelm": "3",
        "type": FTVL.DOUBLE,
    },
    "items": [
        {"pv": "$(D):IGBTT-Mon", "desc": "IGBT temperature", "egu": "C"},
        {"pv": "$(D):RectifierT-Mon", "desc": "Rectifier temperature", "egu": "C"},
        {"pv": "$(D):PCBT-Mon", "desc": "PCB temperature", "egu": "C"},
    ],
}


generic_mon = [
    {
        "pv": "$(D):ActiveInterface-Mon",
        "desc": "Active interface",
        "type": "mbbi",
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
        "pv": "$(D):DSPVer-Mon",
        "desc": "DSP Firmware Version",
        "param": "getDSPVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):ModulatorVer-Mon",
        "desc": "Modulator Version",
        "param": "getModulatorVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):PheripherieVer-Mon",
        "desc": "Pheripherie Version",
        "param": "getPheripherieVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):BootloaderVer-Mon",
        "desc": "Bootloader Version",
        "param": "getBootloaderVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):DLLVer-Mon",
        "desc": "DLL Version",
        "param": "getDLLVersion",
        "scan": "10 second",
        "type": "stringin",
    },
]
