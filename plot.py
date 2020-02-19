#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ExperimentCluster import ExperimentCluster

def main():
    df = pd.read_csv(u'../data/300Msg.csv')

    _4ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=4,events=300,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'our') ])
    _4ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=4,events=300,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'base') ])

    base_memoryfootprint = _4ReplicaSet_300Events_BaseSoln._all_memory_footprint.values
    our_memoryfootprint = _4ReplicaSet_300Events_OurSoln._all_memory_footprint.values
    sub = base_memoryfootprint - our_memoryfootprint
    """
    print("-----")
    print(sub.mean())
    print(sub.std())
    print("-----")
    """


    """
    print("... STATISCTICS for DURATION ... ")
    print("Mean of our soln-> {}".format(_4ReplicaSet_300Events_OurSoln._mean_restore_duration))
    print("Std of our soln -> {}".format(_4ReplicaSet_300Events_OurSoln._std_restore_duration))

    print("Mean of base soln-> {}".format(_4ReplicaSet_300Events_BaseSoln._mean_restore_duration))
    print("Std of base soln -> {}".format(_4ReplicaSet_300Events_BaseSoln._std_restore_duration))
    """


    """
    green_bar = (_4ReplicaSet_300Events_BaseSoln._mean_restore_duration)
    blue_bar = (_4ReplicaSet_300Events_OurSoln._mean_restore_duration)

    green_std = (_4ReplicaSet_300Events_BaseSoln._std_restore_duration)
    blue_std = (_4ReplicaSet_300Events_OurSoln._std_restore_duration)
    """

    green_bar = (sub.mean())

    green_std = (sub.std())


    # the x locations for the groups
    ind = np.arange(1)

    # the width of the bars
    width = 0.35

    #plt.bar(ind, green_bar , width, label='Solution With Zookeeper',color='g',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.bar(ind, green_bar , width, label='Memory Footprint Delta',color='g',yerr=green_std,align='center', ecolor='red', capsize=10)
    #plt.bar(ind + width, blue_bar, width, label='Solution Without Zookeeper',color='b',yerr=blue_std,align='center', ecolor='red', capsize=10)
    #plt.ylabel('Restore Duration(sec)')
    plt.ylabel('Memory Footprint Delta(KB)')
    plt.xlabel('Number of replicas')
    #plt.title('Number of replicas vs Restore Duration')
    plt.title('Number of replicas vs Memory Footprint Delta')
    plt.xticks(ind + width / 2, ('#replicas=4', '#replicas=8', '#replicas=12', '#replicas=16'))
    plt.legend(loc='upper left')
    plt.show() 






main()

# %%
