import numpy as np

Data = np.random.randint(100,size=(10,3))  # Matrix, size 10x3, numbers between 0-100
print(Data)
np.savetxt("Data.csv",Data,delimiter=",") #Create csv file
