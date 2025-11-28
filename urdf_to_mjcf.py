import mujoco

model = mujoco.MjModel.from_xml_path("z1.urdf")
mujoco.mj_saveLastXML("z1.xml", model)
print("Conversion complete: z1.xml created.")