#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ExperimentCluster import ExperimentCluster

def main():
    df = pd.read_csv(u'data/300Msg.csv')

    _4ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=4,events=300,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'our') ])
    _4ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=4,events=300,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'base') ])


    _8ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=8,events=300,dataframe=df[ (df[u'ReplicaSet'] == 8) & (df[u'Solution'] == u'our') ])
    _8ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=8,events=300,dataframe=df[ (df[u'ReplicaSet'] == 8) & (df[u'Solution'] == u'base') ])

    _12ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=12,events=300,dataframe=df[ (df[u'ReplicaSet'] == 12) & (df[u'Solution'] == u'our') ])
    _12ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=12,events=300,dataframe=df[ (df[u'ReplicaSet'] == 12) & (df[u'Solution'] == u'base') ])



    # the x locations for the groups
    ind = np.arange(3)

    # the width of the bars
    width = 0.35


    """
    base_memoryfootprint_1 = _4ReplicaSet_300Events_BaseSoln._all_memory_footprint.values
    our_memoryfootprint_1 = _4ReplicaSet_300Events_OurSoln._all_memory_footprint.values
    sub_1 = base_memoryfootprint_1 - our_memoryfootprint_1

    base_memoryfootprint_2 = _8ReplicaSet_300Events_BaseSoln._all_memory_footprint.values
    our_memoryfootprint_2 = _8ReplicaSet_300Events_OurSoln._all_memory_footprint.values
    sub_2 = base_memoryfootprint_2 - our_memoryfootprint_2


    base_memoryfootprint_3 = _12ReplicaSet_300Events_BaseSoln._all_memory_footprint.values
    our_memoryfootprint_3 = _12ReplicaSet_300Events_OurSoln._all_memory_footprint.values
    sub_3 = base_memoryfootprint_3 - our_memoryfootprint_3

    
    green_bar = (sub_1.mean(),sub_2.mean(),sub_3.mean())
    green_std = (sub_1.std(),sub_2.std(),sub_3.std())


    plt.bar(ind, green_bar , width, label='Memory Footprint Delta',color='g',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.ylabel('Memory Footprint Delta(KB)')
    plt.xlabel('Number of replicas')
    plt.title('Number of replicas vs Memory Footprint Delta')
    plt.xticks(ind + width / 2, ('#replicas=4', '#replicas=8', '#replicas=12', '#replicas=16'))
    plt.legend(loc='upper right')
    plt.show() 
    """
    
    
    
    green_bar = (_4ReplicaSet_300Events_BaseSoln._mean_restore_duration, _8ReplicaSet_300Events_BaseSoln._mean_restore_duration,_12ReplicaSet_300Events_BaseSoln._mean_restore_duration)
    blue_bar = (_4ReplicaSet_300Events_OurSoln._mean_restore_duration, _8ReplicaSet_300Events_OurSoln._mean_restore_duration,_12ReplicaSet_300Events_OurSoln._mean_restore_duration)

    green_std = (_4ReplicaSet_300Events_BaseSoln._std_restore_duration,_8ReplicaSet_300Events_BaseSoln._std_restore_duration,_12ReplicaSet_300Events_BaseSoln._std_restore_duration)
    blue_std = (_4ReplicaSet_300Events_OurSoln._std_restore_duration,_8ReplicaSet_300Events_OurSoln._std_restore_duration,_12ReplicaSet_300Events_OurSoln._std_restore_duration)

    plt.bar(ind, green_bar , width, label='Solution With Zookeeper',color='g',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.bar(ind + width, blue_bar, width, label='Solution Without Zookeeper',color='b',yerr=blue_std,align='center', ecolor='red', capsize=10)
    plt.ylabel('Restore Duration(sec)')
    plt.xlabel('Number of replicas')
    plt.title('Number of replicas vs Restore Duration')
    plt.xticks(ind + width / 2, ('#replicas=4', '#replicas=8', '#replicas=12', '#replicas=16'))
    plt.legend(loc='upper right')
    plt.show() 
    



main()

# %%
