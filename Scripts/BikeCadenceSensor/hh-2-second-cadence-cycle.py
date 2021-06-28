# This software is subject to the license described in the
# LICENSE_A+SS.txt file included with this software distribution.
# You may not use this file except in compliance with this license.
#
# Copyright (c) Garmin Canada Inc. 2018
# All rights reserved.

# This scripts sets up a bike cadence sensor to transmit the specified
# range of sweeping values. Refer to the sesnsorSimulation module for additional
# details on the sweeping mechanism
from System.Timers import Timer

eventTimer = Timer(1000) # convert time to milliseconds

# SWEEP CONFIGURATION - Modify the values in the following four lines to change the sweep characteristics
# Make sure that all of these are doubles (use a decimal point!) so that calculations are accurate

simulator.Cadence = 60

def update(sender, args):
   simulator.Cadence = 110 if simulator.Cadence == 60 else 60

def stopScript():
   eventTimer.Stop()
   simulator.TurnOff()

eventTimer.Elapsed += update
simulator.TurnOn()
eventTimer.Start()
