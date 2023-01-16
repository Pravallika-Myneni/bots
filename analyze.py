import numpy as np

with open('data/backLegValues.npy', 'rb') as f:
    backLegSensorValues = np.load(f)
    print(backLegSensorValues)