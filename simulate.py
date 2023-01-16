import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np



physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)


for loop in range(100):
    p.stepSimulation()
    frontLegSensorValues[loop] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegSensorValues[loop] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

    time.sleep(1/60)
    #print(loop)

print(frontLegSensorValues)
print(backLegSensorValues)

np.save('data/frontLegValues.npy',frontLegSensorValues)
np.save('data/backLegValues.npy',backLegSensorValues)

p.disconnect()