import mujoco
import mujoco.viewer
import os

# Path to any Gymnasium MuJoCo model
MODEL_PATH = "humanoid.xml"

model = mujoco.MjModel.from_xml_path(MODEL_PATH)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:

    while viewer.is_running():
        print("Number of actuators:", model.nu)
        for i in range(model.nu):
            print(i, model.actuator_name2id.keys())

        # Apply a tiny torque to the first actuator (if present)
        if model.nu > 0:
            data.ctrl[0] = 0.2

        mujoco.mj_step(model, data)
        viewer.sync()
