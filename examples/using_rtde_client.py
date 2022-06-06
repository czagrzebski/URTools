import rtde.rtde as rtde
import rtde.rtde_config as rtde_config
import time

conf = rtde_config.ConfigFile("./examples/rtde_conf.xml")

output_names, output_types = conf.get_recipe("out")

# initialize RTDE socket
con = rtde.RTDE("127.0.0.1", 30004)

# connect and negotiate controller version
con.connect()

# get the current controller version
con.get_controller_version()

# define output variables
con.send_output_setup(output_names, output_types)

# start controller synchronization @ 125hz
con.send_start()

while con.is_connected():
    print(con.receive().__dict__['timestamp'])
    time.sleep(1)
