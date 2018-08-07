# Testing using PyCharm for Machine Learning course

# Data pre-processing model
# Import key libraries
# import numpy as np
# import matplatlib.pyplot as plt
import pandas as pd
import os

os.chdir("/Users/gaylonalfano/documents/Python/Machine Learning A-Z/Part 3 - Classification/Section 14 - Logistic Regression/")
print(os.getcwd())

# Import dataset
ds = pd.read_csv("Social_Network_Ads.csv")

print(ds.head())