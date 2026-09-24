import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("../jaredBot/initial/JaredBot v5.xml")
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        # data.ctrl[0] = 0.5
        mujoco.mj_step(model, data)
        viewer.sync()
