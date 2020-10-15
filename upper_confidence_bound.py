# Upper Confidence Bound Algorithm tutorial from Machine Learning A-Z - SuperDataScience -> Input by Ryan L Buchanan 15OCT20

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implement the Upper Confidence Bound algorithm
# Number of users
N = 10000
# Number of adds
d = 10 
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0


# Visualize the results