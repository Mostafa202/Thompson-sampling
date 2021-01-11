import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

dataset=pd.read_csv('Ads_CTR_Optimisation.csv')

d=dataset.shape[1]

number_of_rewards_1=[0]*d
number_of_rewards_0=[0]*d
ads_selected=[]

total_rewards=0

for i in range(len(dataset)):
    ad=0
    max_random=0
    for j in range(d):
        random_beta=random.betavariate(number_of_rewards_1[j]+1,number_of_rewards_0[j]+1)
        if random_beta>max_random:
            max_random=random_beta
            ad=j
    ads_selected.append(ad)
    reward=dataset.iloc[i,ad]
    if reward:
        number_of_rewards_1[ad]+=1
    else:
        number_of_rewards_0[ad]+=1
    total_rewards+=reward

plt.hist(ads_selected)
plt.xlabel('ads')
plt.ylabel('the rate of ads')
plt.show()
    
        





