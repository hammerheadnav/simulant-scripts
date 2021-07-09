# This software is subject to the license described in the
# LICENSE_A+SS.txt file included with this software distribution.
# You may not use this file except in compliance with this license.
#
# Copyright (c) Garmin Canada Inc. 2018
# All rights reserved.

# This scripts sets up a bike power sensor to sweep through torque values. The script will choose whether to sweep wheel torque or pedal torque
# based on which is available. This effectively will sweep power as well.

from sensorSimulation import sweeper
from System.Timers import Timer
import System


eventTimer = Timer(1000) # convert time to milliseconds
sweepTorque = sweeper()

# SWEEP CONFIGURATION - Modify the values in the following four lines to change the sweep characteristics
# Make sure that all of these are doubles (use a decimal point!) so that calculations are accurate
sweepTorque.minValue = 0.0 # Minimum value in sweeping range, in Nm
sweepTorque.maxValue = 32.0 # Maximum value in sweeping range in Nm
sweepTorque.sweepTime = 10 # Time to sweep between the minimum and maximum values, in seconds
sweepTorque.constantTime = 1.0 # Time to spend at a constant torque in the minimum and maximum values, in seconds

# Check if the device has a Crank Torque which may be swept
# This applies to Bike Power Sensor (Crank Torque) and Bike Power Sensor (CTF)
if hasattr(simulator,"CrankTorque"):
   logScriptEvent("Sweeping Crank Torque...")
   simulator.CrankTorque = sweepTorque.minValue
   def update(sender, args):
      simulator.CrankTorque = sweepTorque.getNextValue()
      simulator.Offset = 850 if simulator.CrankTorque == 0 else 512

   def stopScript():
      sweepTorque.stop()
      eventTimer.Stop()
      simulator.TurnOff()

   eventTimer.Elapsed += update
   simulator.TurnOn()
   eventTimer.Start()
   sweepTorque.start()

# Check if the device has a Wheel Torque which may be swept
# This applies to Bike Power Sensor (Wheel Torque)
elif hasattr(simulator,"WheelTorque"):
   logScriptEvent("Sweeping Wheel Torque...")
   simulator.WheelTorque = sweepTorque.minValue
   def update(sender, args):
      simulator.WheelTorque = sweepTorque.getNextValue()

   def stopScript():
      sweepTorque.stop()
      eventTimer.Stop()
      simulator.TurnOff()

   eventTimer.Elapsed += update
   simulator.TurnOn()
   eventTimer.Start()
   sweepTorque.start()

#Device does not have a Torque value that can be swept (i.e. if the sensor being simulated is Bike Power Sensor (Power-Only) )
else:
   logScriptEvent("Cannot sweep wheel or pedal torque.")
   endScript() #Noting to do...exit.
