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
# N_i(n)
numbers_of_selections = [0] * d
# R_i(n)
sums_of_rewards = [0] * d
total_reward = 0

# Step 2: 
#       -> Compute the average reward of ad i up to round n
#       -> Compute the confidence interval
# Import math library for square root function
import math
  
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            # r_bar(n)
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections)
            upper_bound = average_reward + delta_i
        else:

# Visualize the results