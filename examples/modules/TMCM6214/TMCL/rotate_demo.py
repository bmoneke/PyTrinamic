import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM6214
import time

pytrinamic.show_info()
connectionManager = ConnectionManager()

with connectionManager.connect() as myInterface:
    module = TMCM6214(myInterface)
    motor_0 = module.motors[0]

    print("Preparing parameters")
    motor_0.max_acceleration = 20000

    print("Rotating")
    motor_0.rotate(50000)

    time.sleep(5)

    print("Stopping")
    motor_0.stop()

    print("ActualPostion = {}".format(motor_0.actual_position))

    time.sleep(5)

    print("Doubling moved distance")
    motor_0.move_by(motor_0.actual_position, 50000)
    while not(motor_0.get_position_reached()):
        pass

    print("Furthest point reached")
    print("ActualPostion = {}".format(motor_0.actual_position))

    time.sleep(5)

    print("Moving back to 0")
    motor_0.move_to(0, 100000)

    # Wait until position 0 is reached
    while not(motor_0.get_position_reached()):
        pass

    print("Reached Position 0")


