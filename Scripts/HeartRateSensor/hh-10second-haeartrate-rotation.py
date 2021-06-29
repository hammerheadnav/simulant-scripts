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

eventTimer = Timer(10000)  # convert time to milliseconds

# SWEEP CONFIGURATION - Modify the values in the following four lines to change the sweep characteristics
# Make sure that all of these are doubles (use a decimal point!) so that calculations are accurate
# sweepPower.minValue = 10.0 # Minimum value in sweeping range, in Watts
# sweepPower.maxValue = 795.0 # Maximum value in sweeping range in Watts
# # sweepPower.sweepTime = 60.0 # Time to sweep between the minimum and maximum values, in seconds
# # sweepPower.constantTime = 5.0 # Time to spend at a constant speed in the minimum and maximum values, in seconds
#
increment = 0
baseHeartRate = 50

simulator.HeartRate = baseHeartRate  # sweepPower.minValue


def update(sender, args):
    global increment
    global baseHeartRate

    increment = (increment + 20) % 190
    simulator.HeartRate = baseHeartRate + increment


def stopScript():
    eventTimer.Stop()
    simulator.TurnOff()

eventTimer.Elapsed += update
simulator.TurnOn()
eventTimer.Start()
