import numpy as np

data = np.array([12, 15, 18, 21, 25, 30, 35, 40, 45, 50])

data_mean= np.mean(data)
data_min= np.min(data)
data_max= np.max(data)
print(data_mean, data_max, data_min)

data_part= data[data>25]
print(data_part)

data_normalize= (data-data_min)/(data_max-data_min)
print(data_normalize)

data=data.reshape(5,2)
print(data)