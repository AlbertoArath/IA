import mujoco
import mujoco.viewer
import os
import numpy as np
import time
# Load the MuJoCo model from the XML file
model = mujoco.MjModel.from_xml_path("drone.xml")
data = mujoco.MjData(model)

# Simulation parameters
duration = 10  # seconds
timestep = model.opt.timestep
steps = int(duration / timestep)

# Control parameters
amplitude = 0.5
frequency = 1  # Hz

# Create a MuJoCo viewer with a refresh rate of 30 Hz
with mujoco.viewer.launch_passive(model, data) as viewer:
    # Simulate for a certain number of steps
    for i in range(steps):
        # Calculate sinusoidal control input for vertical motion
        phase = 2 * np.pi * frequency * i * timestep
        control = amplitude * np.sin(phase)

        # Set the same control input for all motors
        data.ctrl[:] = control  # Set all motor controls to the same value

        # Step the simulation
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(0.05)
    # The simulation finished.
    print('Simulation finished')
    input("Press Enter to close the viewer...")

# Close the viewer, if the with statement did not already.
viewer.close()
# Close the viewer, if the with statement did not already.
viewer.close()