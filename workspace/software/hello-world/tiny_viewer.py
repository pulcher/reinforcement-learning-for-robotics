import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("/opt/rl-env/lib/python3.12/site-packages/gymnasium/envs/mujoco/assets/ant.xml")
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        data.ctrl[0] = 0.5
        mujoco.mj_step(model, data)
        viewer.sync()
