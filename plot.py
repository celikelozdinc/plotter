#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ExperimentCluster import ExperimentCluster

def main():

    """
    df = pd.read_csv(u'data/300Msg.csv')

    _4ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=4,events=300,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'our') ])
    _4ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=4,events=300,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'base') ])


    _8ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=8,events=300,dataframe=df[ (df[u'ReplicaSet'] == 8) & (df[u'Solution'] == u'our') ])
    _8ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=8,events=300,dataframe=df[ (df[u'ReplicaSet'] == 8) & (df[u'Solution'] == u'base') ])

    _12ReplicaSet_300Events_OurSoln = ExperimentCluster(replicas=12,events=300,dataframe=df[ (df[u'ReplicaSet'] == 12) & (df[u'Solution'] == u'our') ])
    _12ReplicaSet_300Events_BaseSoln = ExperimentCluster(replicas=12,events=300,dataframe=df[ (df[u'ReplicaSet'] == 12) & (df[u'Solution'] == u'base') ])
    """

    df_6000 = pd.read_csv("data/6000Msg.csv")
    _4ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=4,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "distributed") ])
    _4ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=4,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "centralized") ])
    _4ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=4,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "conventional") ])

    _6ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=6,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "distributed") ])
    _6ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=6,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "centralized") ]) 
    _6ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=6,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "conventional") ]) 

    _8ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=8,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "distributed") ])
    _8ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=8,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "centralized") ])
    _8ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=8,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "conventional") ])



    # the width of the bars
    barWidth = 0.30

    distributed_memoryfootprint_8 = _8ReplicaSet_6000Events_DistributedSoln._all_memory_footprint.values
    centralized_memoryfootprint_8 = _8ReplicaSet_6000Events_CentralizedSoln._all_memory_footprint.values
    conventional_memoryfootprint_8 = _8ReplicaSet_6000Events_ConventionalSoln._all_memory_footprint.values
    
    conventional_minus_centralized_8 =  conventional_memoryfootprint_8 - centralized_memoryfootprint_8
    conventional_minus_distributed_8 = conventional_memoryfootprint_8 - distributed_memoryfootprint_8
    distributed_minus_centralized_8 = distributed_memoryfootprint_8 - centralized_memoryfootprint_8
    
    

    """

    base_memoryfootprint_1 = _4ReplicaSet_3000Events_DistributedSoln._all_memory_footprint.values
    our_memoryfootprint_1 = _4ReplicaSet_3000Events_CentralizedSoln._all_memory_footprint.values
    #sub_1 = base_memoryfootprint_1 - our_memoryfootprint_1
    sub_1 = np.absolute(base_memoryfootprint_1 - our_memoryfootprint_1)

    base_memoryfootprint_2 = _8ReplicaSet_3000Events_DistributedSoln._all_memory_footprint.values
    our_memoryfootprint_2 = _8ReplicaSet_3000Events_CentralizedSoln._all_memory_footprint.values
    #sub_2 = base_memoryfootprint_2 - our_memoryfootprint_2
    sub_2 = np.absolute(base_memoryfootprint_2 - our_memoryfootprint_2)


    base_memoryfootprint_3 = _12ReplicaSet_3000Events_DistributedSoln._all_memory_footprint.values
    our_memoryfootprint_3 = _12ReplicaSet_3000Events_CentralizedSoln._all_memory_footprint.values
    #sub_3 = base_memoryfootprint_3 - our_memoryfootprint_3
    sub_3 = np.absolute(base_memoryfootprint_3 - our_memoryfootprint_3)



    green_bar = (sub_1.mean(),sub_2.mean(),sub_3.mean())
    green_std = (sub_1.std(),sub_2.std(),sub_2.std())


    plt.bar(ind, green_bar , width, label='Memory Consumption Difference',color='0.80',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.ylabel('Memory Footprint Delta(KB)', fontsize=20)
    plt.xlabel('Number of replicas', fontsize=20)
    #plt.title('Number of replicas vs Memory Footprint Delta',fontsize=20)
    plt.xticks(ind + width / 10, ('#replicas=4', '#replicas=8', '#replicas=12'),fontsize=20)
    plt.legend(loc='best',fontsize=20)
    plt.show()
    """
    
    
    # heights pf the bars
    green_bar = (_4ReplicaSet_6000Events_DistributedSoln._mean_restore_duration,_6ReplicaSet_6000Events_DistributedSoln._mean_restore_duration,_8ReplicaSet_6000Events_DistributedSoln._mean_restore_duration)
    blue_bar = (_4ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration, _6ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration, _8ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration)
    new_bar = (_4ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration, _6ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration, _8ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration)

    # std errors
    green_std = (_4ReplicaSet_6000Events_DistributedSoln._std_restore_duration,_6ReplicaSet_6000Events_DistributedSoln._std_restore_duration,_8ReplicaSet_6000Events_DistributedSoln._std_restore_duration)
    blue_std = (_4ReplicaSet_6000Events_CentralizedSoln._std_restore_duration,_6ReplicaSet_6000Events_CentralizedSoln._std_restore_duration,_8ReplicaSet_6000Events_CentralizedSoln._std_restore_duration)
    new_std = (_4ReplicaSet_6000Events_ConventionalSoln._std_restore_duration, _6ReplicaSet_6000Events_ConventionalSoln._std_restore_duration, _8ReplicaSet_6000Events_ConventionalSoln._std_restore_duration)

    # set positions of bars in x-axis
    r1 = np.arange(3)
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    #print("{}, {}, {}".format(r1,r2,r3))
    

    # Make the plot
    plt.bar(r1, green_bar, width=barWidth, label='Distributed Checkpointing',color='0.30',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.bar(r2, blue_bar, width=barWidth, label='Centralized Checkpointing',color='0.60',yerr=blue_std,align='center', ecolor='red', capsize=10)
    plt.bar(r3, new_bar, width=barWidth, label='Conventional Checkpointing', color ='0.90', yerr=new_std, align='center', ecolor='red',capsize=10)
    plt.ylabel('Restore Duration(sec)',fontsize=10,fontweight="bold")
    plt.xlabel('Number of replicas',fontsize=10,fontweight="bold")
    #plt.title('Number of replicas vs Restore Duration')
    plt.xticks([r + barWidth for r in range(3)], ('#replicas=4', '#replicas=6', '#replicas=8', '#replicas=16'),fontsize=20)
    plt.legend(loc='best',fontsize=10)
    plt.show()

    
    
    



main()

# %%
