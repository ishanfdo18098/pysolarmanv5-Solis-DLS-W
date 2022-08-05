""" A basic client demonstrating how to use pysolarmanv5."""
from pysolarmanv5 import PySolarmanV5


def main():
    """Create new PySolarman instance, using IP address and S/N of data logger

    Only IP address and S/N of data logger are mandatory parameters. If port,
    mb_slave_id, and verbose are omitted, they will default to 8899, 1 and 0
    respectively.
    """
    modbus = PySolarmanV5(
        "DATALOGGER_IP", DATALOGGER_SERIAL_NUMBER, port=8899, mb_slave_id=1, verbose=False
    )

    print("Date/Time :", modbus.read_holding_registers(register_addr=2999, quantity=6))
    print("Failsafe :", modbus.read_holding_registers(register_addr=3152, quantity=2))

    DC1V = modbus.read_input_register_formatted(register_addr=3021, quantity=1, scale=0.1)
    DC1A = modbus.read_input_register_formatted(register_addr=3022, quantity=1, scale=0.1)
    DC2V = modbus.read_input_register_formatted(register_addr=3023, quantity=1, scale=0.1)
    DC2A = modbus.read_input_register_formatted(register_addr=3024, quantity=1, scale=0.1)
    DCPwr = modbus.read_input_register_formatted(register_addr=3006, quantity=2, scale=0.001)

    DC1Pwr = DC1V * DC1A / 1000
    DC2Pwr = DC2V * DC2A / 1000
    ACActPwr = modbus.read_input_register_formatted(register_addr=3004, quantity=2, scale=0.001)
    ACAppPwr = modbus.read_input_register_formatted(register_addr=3057, quantity=2, scale=0.001)

    print("\nAC Apparent Power: {:.2f}".format(ACAppPwr), "kW")
    print("AC Active Power: {:.2f}".format(ACActPwr), "kW")
    print("AC V: ", modbus.read_input_register_formatted(register_addr=3035, quantity=1, scale=0.1), "V")
    print("AC A: ", modbus.read_input_register_formatted(register_addr=3038, quantity=1, scale=0.1), "A")
    print("AC Freq: ", modbus.read_input_register_formatted(register_addr=3042, quantity=1, scale=0.01), "Hz")

    print("\nCalculated DC Power: {:.2f}".format(DC1Pwr + DC2Pwr), "kW")
    print("Current DC Power: {:.2f}".format(DCPwr), "kW")

    print("DC Power 1: {:.2f}".format(DC1Pwr), "kW")
    print("DC Power 2: {:.2f}".format(DC2Pwr), "kW")
    print("Efficiency: {:.1f}".format(ACActPwr / DCPwr * 100), "%")
    print("DC V 1: {:.1f}".format(DC1V), "V")
    print("DC A 1: ", DC1A, "A")
    print("DC V 2: {:.1f}".format(DC2V), "V")
    print("DC A 2: ", DC2A, "A")

    print("\nTemp: {:.1f}".format(modbus.read_input_register_formatted(register_addr=3041, quantity=1, scale=0.1)), "C")

    """ Note: Many of the yield figures are 32 bits but not sure which register, back one or forward one?? """
    print("\nPrev Month Yield: ", modbus.read_input_register_formatted(register_addr=3012, quantity=2), "kWh")
    print("This Month Yield: ", modbus.read_input_register_formatted(register_addr=3010, quantity=2), "kWh")
    print("Total Yield: ", modbus.read_input_register_formatted(register_addr=3008, quantity=2, scale=0.001), "MWh")
    print("Annual Yield: ", modbus.read_input_register_formatted(register_addr=3016, quantity=2, scale=0.001), "MWh")

    print("\nYear: ", modbus.read_input_register_formatted(register_addr=3072, quantity=1))
    print("Month: ", modbus.read_input_register_formatted(register_addr=3073, quantity=1))
    print("Day: ", modbus.read_input_register_formatted(register_addr=3074, quantity=1))
    print("Hour: ", modbus.read_input_register_formatted(register_addr=3075, quantity=1))
    print("Minute: ", modbus.read_input_register_formatted(register_addr=3076, quantity=1))
    print("Secs: ", modbus.read_input_register_formatted(register_addr=3077, quantity=1))


if __name__ == "__main__":
    main()
