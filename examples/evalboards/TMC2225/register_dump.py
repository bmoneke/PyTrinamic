"""
Dump all register values of the TMC2225 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2225_eval

pytrinamic.show_info()

myInterface = ConnectionManager().connect()
print(myInterface)
eval_board = TMC2225_eval(myInterface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF:       0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))
print("GSTAT:       0x{0:08X}".format(eval_board.read_register(drv.REG.GSTAT)))
print("IFCNT:       0x{0:08X}".format(eval_board.read_register(drv.REG.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(eval_board.read_register(drv.REG.SLAVECONF)))
print("IHOLD_IRUN:  0x{0:08X}".format(eval_board.read_register(drv.REG.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(eval_board.read_register(drv.REG.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(eval_board.read_register(drv.REG.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(eval_board.read_register(drv.REG.TPWMTHRS)))
print("MSCNT:       0x{0:08X}".format(eval_board.read_register(drv.REG.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(eval_board.read_register(drv.REG.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("DRV_STATUS:  0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_STATUS)))
print("PWMCONF:     0x{0:08X}".format(eval_board.read_register(drv.REG.PWMCONF)))

myInterface.close()

print("\nReady.")
