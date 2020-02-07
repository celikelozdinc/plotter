#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from entity.ExperimentCluster import ExperimentCluster

def main():
    df = pd.read_csv(u'../data/100Msg.csv')

    _4ReplicaSet_100Events_OurSoln = ExperimentCluster(replicas=4,events=100,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'our') ])
    _4ReplicaSet_100Events_BaseSoln = ExperimentCluster(replicas=4,events=100,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'base') ])

    green_bar = (_4ReplicaSet_100Events_BaseSoln._mean_restore_duration)
    blue_bar = (_4ReplicaSet_100Events_OurSoln._mean_restore_duration)

    green_std = (_4ReplicaSet_100Events_BaseSoln._std_restore_duration)
    blue_std = (_4ReplicaSet_100Events_OurSoln._std_restore_duration)

    # the x locations for the groups
    ind = np.arange(4)

    # the width of the bars
    width = 0.35

    plt.bar(ind, green_bar , width, label='Solution With Zookeeper',color='g',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.bar(ind + width, blue_bar, width, label='Solution Without Zookeeper',color='b',yerr=blue_std,align='center', ecolor='red', capsize=10)
    plt.ylabel('Restore Duration(sec)')
    plt.xlabel('Number of replicas')
    plt.title('Number of replicas vs Restore Duration')
    plt.xticks(ind + width / 2, ('#replicas=4', '#replicas=8', '#replicas=12', '#replicas=16'))
    plt.legend(loc='best')
    plt.show() 






main()

# %%
