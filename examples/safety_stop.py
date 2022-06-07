"""
Basic Move Program using the RTDEControlInterface 

Uses ur_rtde library 

"""

import rtde_control
import rtde_receive
import time

# Initialize the control interface 
rtde_control = rtde_control.RTDEControlInterface("127.0.0.1")
rtde_receive = rtde_receive.RTDEReceiveInterface("127.0.0.1")

while True:
    print(rtde_receive.getActualQ())
    time.sleep(1.5)