import mujoco
import numpy as np

# A tiny built-in MuJoCo model: a single joint and body
xml = """
<mujoco>
  <worldbody>
    <body name="box" pos="0 0 1">
      <joint name="hinge" type="hinge" axis="0 1 0"/>
      <geom type="box" size="0.1 0.1 0.1"/>
    </body>
  </worldbody>
</mujoco>
"""

# 1. Load model
model = mujoco.MjModel.from_xml_string(xml)

# 2. Allocate simulation data
data = mujoco.MjData(model)

# 3. Step simulation
for i in range(100):
    mujoco.mj_step(model, data)

# 4. Print something
print("Joint position qpos:", data.qpos)
print("Joint velocity qvel:", data.qvel)
