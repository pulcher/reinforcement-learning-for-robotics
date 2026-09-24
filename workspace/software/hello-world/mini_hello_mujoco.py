import mujoco

model = mujoco.MjModel.from_xml_path("/opt/rl-env/lib/python3.12/site-packages/gymnasium/envs/mujoco/assets/humanoid.xml")
data = mujoco.MjData(model)

for _ in range(10):
    mujoco.mj_step(model, data)

print("COM position:", data.subtree_com[model.body_root])
