import numpy as np
import matplotlib.pyplot as plt

with open('data/backLegValues.npy', 'rb') as f:
    backLegSensorValues = np.load(f)
    #print(backLegSensorValues)

with open('data/frontLegValues.npy', 'rb') as f:
    frontLegSensorValues = np.load(f)
    #print(backLegSensorValues)

plt.plot(frontLegSensorValues, label = 'Front Leg', color = 'green', linestyle='dashed')
plt.plot(backLegSensorValues, label = 'Back Leg', color = 'blue', linestyle='dashed')
plt.legend()
plt.show()