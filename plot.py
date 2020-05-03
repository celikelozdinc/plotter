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

    df_6000 = pd.read_csv("data/6000Msg_with_12.csv")
    _4ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=4,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "distributed") ])
    _4ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=4,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "centralized") ])
    _4ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=4,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "conventional") ])

    _6ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=6,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "distributed") ])
    _6ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=6,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "centralized") ]) 
    _6ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=6,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "conventional") ]) 

    _8ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=8,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "distributed") ])
    _8ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=8,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "centralized") ])
    _8ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=8,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "conventional") ])

    _10ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=10,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "distributed") ])
    _10ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=10,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "centralized") ])
    _10ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=10,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "conventional") ])

    _12ReplicaSet_6000Events_DistributedSoln = ExperimentCluster(replicas=12,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 12) & (df_6000["Solution"] == "distributed") ])
    _12ReplicaSet_6000Events_CentralizedSoln = ExperimentCluster(replicas=12,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 12) & (df_6000["Solution"] == "centralized") ])
    _12ReplicaSet_6000Events_ConventionalSoln = ExperimentCluster(replicas=12,events=6000,dataframe=df_6000[ (df_6000["ReplicaSet"] == 12) & (df_6000["Solution"] == "conventional") ])


    # the width of the bars
    barWidth = 0.30

    """
    distributed_memoryfootprint_8 = _8ReplicaSet_6000Events_DistributedSoln._all_memory_footprint.values
    centralized_memoryfootprint_8 = _8ReplicaSet_6000Events_CentralizedSoln._all_memory_footprint.values
    conventional_memoryfootprint_8 = _8ReplicaSet_6000Events_ConventionalSoln._all_memory_footprint.values
    
    conventional_minus_centralized_8 =  conventional_memoryfootprint_8 - centralized_memoryfootprint_8
    conventional_minus_distributed_8 = conventional_memoryfootprint_8 - distributed_memoryfootprint_8
    distributed_minus_centralized_8 = distributed_memoryfootprint_8 - centralized_memoryfootprint_8
    """

    # heights of the bars    
    
    green_bar = (_6ReplicaSet_6000Events_DistributedSoln._mean_restore_duration,_8ReplicaSet_6000Events_DistributedSoln._mean_restore_duration,_10ReplicaSet_6000Events_DistributedSoln._mean_restore_duration,_12ReplicaSet_6000Events_DistributedSoln._mean_restore_duration)
    blue_bar = (_6ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration,_8ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration,_10ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration,_12ReplicaSet_6000Events_CentralizedSoln._mean_restore_duration)
    new_bar = (_6ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration,_8ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration, _10ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration, _12ReplicaSet_6000Events_ConventionalSoln._mean_restore_duration)
    all_bars = green_bar + blue_bar + new_bar
   


    #green_bar = (_6ReplicaSet_6000Events_DistributedSoln._mean_memory_footprint,_8ReplicaSet_6000Events_DistributedSoln._mean_memory_footprint,_10ReplicaSet_6000Events_DistributedSoln._mean_memory_footprint,_12ReplicaSet_6000Events_DistributedSoln._mean_memory_footprint)
    #blue_bar = (_6ReplicaSet_6000Events_CentralizedSoln._mean_memory_footprint,_8ReplicaSet_6000Events_CentralizedSoln._mean_memory_footprint,_10ReplicaSet_6000Events_CentralizedSoln._mean_memory_footprint,_12ReplicaSet_6000Events_CentralizedSoln._mean_memory_footprint)
    #new_bar = (_6ReplicaSet_6000Events_ConventionalSoln._mean_memory_footprint,_8ReplicaSet_6000Events_ConventionalSoln._mean_memory_footprint,_10ReplicaSet_6000Events_ConventionalSoln._mean_memory_footprint, _12ReplicaSet_6000Events_ConventionalSoln._mean_memory_footprint)
    #all_bars = green_bar + blue_bar + new_bar

    
    print("Distributed Checkpointing bar: {}".format(green_bar))
    print("Centralized Checkpointing bar: {}".format(blue_bar))
    print("Conventional Checkpointing bar: {}".format(new_bar))
    print("All bars: {}".format(all_bars))

    # std errors
    green_std = (_6ReplicaSet_6000Events_DistributedSoln._std_restore_duration,_8ReplicaSet_6000Events_DistributedSoln._std_restore_duration,_10ReplicaSet_6000Events_DistributedSoln._std_restore_duration, _12ReplicaSet_6000Events_DistributedSoln._std_restore_duration)
    blue_std = (_6ReplicaSet_6000Events_CentralizedSoln._std_restore_duration,_8ReplicaSet_6000Events_CentralizedSoln._std_restore_duration,_10ReplicaSet_6000Events_CentralizedSoln._std_restore_duration, _12ReplicaSet_6000Events_CentralizedSoln._std_restore_duration)
    new_std = (_6ReplicaSet_6000Events_ConventionalSoln._std_restore_duration,_8ReplicaSet_6000Events_ConventionalSoln._std_restore_duration,_10ReplicaSet_6000Events_ConventionalSoln._std_restore_duration, _12ReplicaSet_6000Events_ConventionalSoln._std_restore_duration)
    

    #green_std = (_6ReplicaSet_6000Events_DistributedSoln._std_memory_footprint,_8ReplicaSet_6000Events_DistributedSoln._std_memory_footprint,_10ReplicaSet_6000Events_DistributedSoln._std_memory_footprint, _12ReplicaSet_6000Events_DistributedSoln._std_memory_footprint)
    #blue_std = (_6ReplicaSet_6000Events_CentralizedSoln._std_memory_footprint,_8ReplicaSet_6000Events_CentralizedSoln._std_memory_footprint,_10ReplicaSet_6000Events_CentralizedSoln._std_memory_footprint,_12ReplicaSet_6000Events_CentralizedSoln._std_memory_footprint)
    #new_std = (_6ReplicaSet_6000Events_ConventionalSoln._std_memory_footprint,_8ReplicaSet_6000Events_ConventionalSoln._std_memory_footprint,_10ReplicaSet_6000Events_ConventionalSoln._std_memory_footprint, _12ReplicaSet_6000Events_ConventionalSoln._std_memory_footprint)
    
    
    print("STD of Distributed Checkpointing bar: {}".format(green_std))
    print("STD of Centralized Checkpointing bar: {}".format(blue_std))
    print("STD of Conventional Checkpointing bar: {}".format(new_std))


    # set positions of bars in x-axis
    r1 = np.arange(4)
    print("Position of bars - r1 : {}".format(r1))
    r2 = [x + barWidth for x in r1]
    print("Position of bars - r2 : {}".format(r2))
    r3 = [x + barWidth for x in r2]
    print("Position of bars - r3 : {}".format(r3))
    r4 = np.concatenate((r1,r2,r3))
    print("Position of bars - r4 : {}".format(r4))

    # Make the plot
    plt.bar(r1, green_bar, width=barWidth, label='Distributed Checkpointing',color='0.30',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.bar(r2, blue_bar, width=barWidth, label='Centralized Checkpointing',color='0.60',yerr=blue_std,align='center', ecolor='red', capsize=10)
    plt.bar(r3, new_bar, width=barWidth, label='Conventional Checkpointing', color ='0.90', yerr=new_std, align='center', ecolor='red',capsize=10)
    plt.ylabel('Restore Duration(sec)',fontsize=10,fontweight="bold")
    plt.xlabel('Number of replicas',fontsize=10,fontweight="bold")
    #plt.title('Number of replicas vs Restore Duration')
    plt.xticks([r + barWidth for r in range(4)], ('#replicas=6', '#replicas=8', '#replicas=10', '#replicas=12'),fontsize=10, rotation=45)
    for i in range(len(r4)):
        plt.text(x = r4[i]-0.1, y = all_bars[i]+0.2, s = all_bars[i], size = 6)
    plt.legend(loc='best',fontsize=10)
    plt.show()
    
    
    

    """
    plt.bar(r1, green_bar, width=barWidth, label='Distributed Checkpointing',color='0.30',yerr=green_std,align='center', ecolor='red', capsize=10)
    plt.bar(r2, blue_bar, width=barWidth, label='Centralized Checkpointing',color='0.60',yerr=blue_std,align='center', ecolor='red', capsize=10)
    plt.bar(r3, new_bar, width=barWidth, label='Conventional Checkpointing', color ='0.90', yerr=new_std, align='center', ecolor='red',capsize=10)
    plt.ylabel('Memory Footprint(kiB)',fontsize=10,fontweight="bold")
    plt.xlabel('Number of replicas',fontsize=10,fontweight="bold")
    #plt.title('Number of replicas vs Restore Duration')
    plt.xticks([r + barWidth for r in range(4)], ('#replicas=6','#replicas=8','#replicas=10','#replicas=12'),fontsize=10,rotation=45)
    for i in range(len(r4)):
        plt.text(x = r4[i]-0.1, y = all_bars[i]+0.2, s = all_bars[i], size = 6)
    plt.legend(loc='best',fontsize=10)
    plt.show()
    """
    
    
    



main()

# %%
