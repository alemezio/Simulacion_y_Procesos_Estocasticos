#  Ejemplo del libro de Ciaburro: https://github.com/PacktPublishing/Hands-On-Simulation-Modeling-with-Python-Second-Edition
import numpy as np
from sklearn.model_selection import KFold

StartedData=np.arange(10,110,10)
print(StartedData)


kfold = KFold(5, shuffle=True, random_state=1)

for TrainData, TestData in kfold.split(StartedData):
	# print(TrainData, TestData)
	print("Train Data :", StartedData[TrainData],"Test Data :", StartedData[TestData])
    
