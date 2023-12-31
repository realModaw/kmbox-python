import serial #pip install pyserial
import serial.tools.list_ports
import time

##
## WORKING KMBOX support clone for python.
## FOR KMBOX B+ Pro

def find_port(target_description):
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if target_description in desc:
            return port  # 'port' is already a string
    return None


def open_port(port_name, baud_rate):
    try:
        ser = serial.Serial(port_name, baud_rate, timeout=1)
        return ser
    except serial.SerialException as e:
        print(f"Error opening port: {e}")
        return None

def send_command(ser, command):
    try:
        ser.write(command.encode())
    except serial.SerialException as e:
        print(f"Failed to write to serial port: {e}")

def km_move(ser, x, y):
    command = f"km.move({x},{y})\r\n"
    send_command(ser, command)

def km_click(ser):
    command_down = "km.left(1)\r\n"  # Left mouse button down
    command_up = "km.left(0)\r\n"    # Left mouse button up
    send_command(ser, command_down)
    time.sleep(0.01)  # 10ms delay
    send_command(ser, command_up)

# Example usage
target_description = "USB-SERIAL CH340"
port = find_port(target_description)
if not port:
    print("\n[!] no port found..")
else:
    ser = open_port(port, 115200)
    if ser:
        print(f"\n[+] connected to the kmbox with {port}")

        x = int(input("\n[+] to which x coordinate do you want to move?\n\n-> "))
        y = int(input("\n[+] to which y coordinate do you want to move?\n\n-> "))

        km_move(ser, x, y)
        print("\n[+] clicking left mouse button in 3 seconds")
        time.sleep(3)
        km_click(ser)
        print("\n[+] clicked your left mouse button!")

        ser.close()
