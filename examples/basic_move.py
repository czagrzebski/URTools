"""
Basic Move Program using the RTDEControlInterface
"""

import rtde_control
import dashboard_client
import time

# Initialize the control interface 
rtde_control = rtde_control.RTDEControlInterface("127.0.0.1")

# Initialize the dashboard client
polyscope = dashboard_client.DashboardClient("127.0.0.1")

# Connect to the polyscope interface w/ 2000ms time out
polyscope.connect(2000)

# Prompt Operator of Remove Override
polyscope.popup("Remote Override Initiated")

time.sleep(4)

# Define the joint positions (rad)
joint_q = [-1.54, -1.83, -2.28, -0.59, 1.60, 0.023]

# Move synchronously 
rtde_control.moveJ(joint_q)

# Terminate the script
rtde_control.stopScript()