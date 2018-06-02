import numpy as np
from sklearn.linear_model import LinearRegression
import sys
from src.readFile import readFile
from src.convertData import convertData
from src.errorExit import *
from src.calcEstimatedPrice import *
from src.writeFile import *

data = convertData(readFile(sys.argv[1]))
X = np.array([_[0] for _ in data]).reshape(-1, 1)
y = [_[1] for _ in data]
lm = LinearRegression()
lm.fit(X, y)
print(lm.coef_, lm.intercept_)
print(lm.predict(240000))