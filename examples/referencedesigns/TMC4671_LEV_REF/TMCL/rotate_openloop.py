"""
Turn a motor without feedback in open loop mode
"""

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.referencedesigns import TMC4671_LEV_REF
import time

PyTrinamic.show_info()

# please select your CAN adapter
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

with myInterface:
    module = TMC4671_LEV_REF(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMC4671-LEV-REF.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_OPENLOOP
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.open_loop_current = 1000
    print(motor.drive_settings)

    # motion settings
    motor.linear_ramp.max_velocity = 2000
    motor.linear_ramp.max_acceleration = 1000
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    print("Starting motor...")
    motor.rotate(1000)
    time.sleep(3)

    print("Changing motor direction...")
    motor.rotate(-1000)
    time.sleep(6)

    print("Stopping motor...")
    motor.rotate(0)
    time.sleep(3)

    # power of
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DISABLED

print("\nReady.")
