import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
data = boston.data
target = boston.target

model = LinearRegression()
model.fit(data, target)
