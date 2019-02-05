## Summary

The goal of this repo is to make using the lab instruments easier.
There are three types of instruments: oscilloscopes, power supplies, parameter analizers
There are many brands: Agilent, Keithley, Keysight, Caen, Tektronicks

Currently I see some files named Agilent, Lecroy, and others named PowerSupply, etc.

To make this libray support legacy code, by manipulating the file `__init__.py` we will support either `from contraption import PowerSupply.Keithley2657a`, `from contraption import Keithley.Keithley2657a`, `from contraption import Keithley2657a`.
