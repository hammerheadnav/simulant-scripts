# This software is subject to the license described in the
# LICENSE_A+SS.txt file included with this software distribution.
# You may not use this file except in compliance with this license.
#
# Copyright (c) Garmin Canada Inc. 2018
# All rights reserved.

# This scripts sets up a bike power sensor to transmit the specified
# range of sweeping values. Refer to the sesnsorSimulation module for additional
# details on the sweeping mechanism

# from sensorSimulation import sweeper
from System.Timers import Timer
import System

eventTimer = Timer(10000) # convert time to milliseconds

simulator.CrankTorque = 16 #

def update(sender, args):
    simulator.CrankTorque = (simulator.CrankTorque + 16) % 96

def stopScript():
   eventTimer.Stop()
   simulator.TurnOff()

eventTimer.Elapsed += update
simulator.TurnOn()
eventTimer.Start()
