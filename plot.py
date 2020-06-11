#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ExperimentCluster import ExperimentCluster

def main():

    df_6000 = pd.read_csv("data/3600Messages.csv")

    _6_DistributedSoln = ExperimentCluster(replicas=6,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "distributed") ])
    _6_CentralizedSoln = ExperimentCluster(replicas=6,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "centralized") ]) 
    _6_ConventionalSoln = ExperimentCluster(replicas=6,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "conventional") ])
    _6_MirroredSoln = ExperimentCluster(replicas=6,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 6) & (df_6000["Solution"] == "mirrored") ]) 

    _8_DistributedSoln = ExperimentCluster(replicas=8,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "distributed") ])
    _8_CentralizedSoln = ExperimentCluster(replicas=8,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "centralized") ])
    _8_ConventionalSoln = ExperimentCluster(replicas=8,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "conventional") ])
    _8_MirroredSoln = ExperimentCluster(replicas=8,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 8) & (df_6000["Solution"] == "mirrored") ])

    _10_DistributedSoln = ExperimentCluster(replicas=10,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "distributed") ])
    _10_CentralizedSoln = ExperimentCluster(replicas=10,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "centralized") ])
    _10_ConventionalSoln = ExperimentCluster(replicas=10,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "conventional") ])
    _10_MirroredSoln = ExperimentCluster(replicas=10,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 10) & (df_6000["Solution"] == "mirrored") ])

    _4_DistributedSoln = ExperimentCluster(replicas=4,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "distributed") ])
    _4_CentralizedSoln = ExperimentCluster(replicas=4,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "centralized") ])
    _4_ConventionalSoln = ExperimentCluster(replicas=4,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "conventional") ])
    _4_MirroredSoln = ExperimentCluster(replicas=4,events=3600,dataframe=df_6000[ (df_6000["ReplicaSet"] == 4) & (df_6000["Solution"] == "mirrored") ])


    # the width of the bars
    barWidth = 0.20

    #heights of the bars    
    # distributed_bar = (_4_DistributedSoln._mean_restore_duration,_6_DistributedSoln._mean_restore_duration,_8_DistributedSoln._mean_restore_duration,_10_DistributedSoln._mean_restore_duration)
    # centralized_bar = (_4_CentralizedSoln._mean_restore_duration,_6_CentralizedSoln._mean_restore_duration,_8_CentralizedSoln._mean_restore_duration,_10_CentralizedSoln._mean_restore_duration)
    # conventional_bar = (_4_ConventionalSoln._mean_restore_duration,_6_ConventionalSoln._mean_restore_duration,_8_ConventionalSoln._mean_restore_duration, _10_ConventionalSoln._mean_restore_duration)
    # mirrored_bar = (_4_MirroredSoln._mean_restore_duration,_6_MirroredSoln._mean_restore_duration,_8_MirroredSoln._mean_restore_duration, _10_MirroredSoln._mean_restore_duration)
    # all_bars = distributed_bar + centralized_bar + conventional_bar + mirrored_bar
   

    distributed_bar = (_4_DistributedSoln._mean_memory_footprint,_6_DistributedSoln._mean_memory_footprint,_8_DistributedSoln._mean_memory_footprint,_10_DistributedSoln._mean_memory_footprint)
    centralized_bar = (_4_CentralizedSoln._mean_memory_footprint,_6_CentralizedSoln._mean_memory_footprint,_8_CentralizedSoln._mean_memory_footprint,_10_CentralizedSoln._mean_memory_footprint)
    conventional_bar = (_4_ConventionalSoln._mean_memory_footprint,_6_ConventionalSoln._mean_memory_footprint,_8_ConventionalSoln._mean_memory_footprint,_10_ConventionalSoln._mean_memory_footprint)
    mirrored_bar = (_4_MirroredSoln._mean_memory_footprint,_6_MirroredSoln._mean_memory_footprint,_8_MirroredSoln._mean_memory_footprint,_10_MirroredSoln._mean_memory_footprint)
    all_bars = distributed_bar + centralized_bar + conventional_bar + mirrored_bar

    
    print("Distributed Checkpointing - values : {}".format(distributed_bar))
    print("Centralized Checkpointing - values : {}".format(centralized_bar))
    print("Conventional Checkpointing - values : {}".format(conventional_bar))
    print("Mirrored Checkpointing - values : {}".format(mirrored_bar))
    print("All bars: {}".format(all_bars))

    # std errors
    # distributed_std = (_4_DistributedSoln._std_restore_duration,_6_DistributedSoln._std_restore_duration,_8_DistributedSoln._std_restore_duration,_10_DistributedSoln._std_restore_duration)
    # centralized_std = ( _4_CentralizedSoln._std_restore_duration,_6_CentralizedSoln._std_restore_duration,_8_CentralizedSoln._std_restore_duration,_10_CentralizedSoln._std_restore_duration)
    # conventional_std = ( _4_ConventionalSoln._std_restore_duration,_6_ConventionalSoln._std_restore_duration,_8_ConventionalSoln._std_restore_duration,_10_ConventionalSoln._std_restore_duration)
    # mirrored_std = (_4_MirroredSoln._std_restore_duration,_6_MirroredSoln._std_restore_duration,_8_MirroredSoln._std_restore_duration,_10_MirroredSoln._std_restore_duration)
    

    distributed_std = (_4_DistributedSoln._std_memory_footprint,_6_DistributedSoln._std_memory_footprint,_8_DistributedSoln._std_memory_footprint,_10_DistributedSoln._std_memory_footprint)
    centralized_std = (_4_CentralizedSoln._std_memory_footprint,_6_CentralizedSoln._std_memory_footprint,_8_CentralizedSoln._std_memory_footprint,_10_CentralizedSoln._std_memory_footprint)
    conventional_std = ( _4_ConventionalSoln._std_memory_footprint,_6_ConventionalSoln._std_memory_footprint,_8_ConventionalSoln._std_memory_footprint,_10_ConventionalSoln._std_memory_footprint)
    mirrored_std = (_4_MirroredSoln._std_memory_footprint,_6_MirroredSoln._std_memory_footprint,_8_MirroredSoln._std_memory_footprint,_10_MirroredSoln._std_memory_footprint)

    
    print("Distributed Checkpointing - standard deviations : {}".format(distributed_std))
    print("Centralized Checkpointing - standard deviations : {}".format(centralized_std))
    print("Conventional Checkpointing - standard deviations : {}".format(conventional_std))
    print("Mirrored Checkpointing - standard deviations : {}".format(mirrored_std))


    # set positions of bars in x-axis
    r1 = np.arange(4)
    print("Position of bars - r1 : {}".format(r1))
    r2 = [x + barWidth for x in r1]
    print("Position of bars - r2 : {}".format(r2))
    r3 = [x + barWidth for x in r2]
    print("Position of bars - r3 : {}".format(r3))
    r4 = [x + barWidth for x in r3]
    print("Position of bars - r4 : {}".format(r4))
    r5 = np.concatenate((r1,r2,r3,r4))
    print("Position of bars - r5 : {}".format(r5))

    # Make the plot
    """
    plt.bar(r1, distributed_bar, width=barWidth, label='Distributed Checkpointing',color='0.20',yerr=distributed_std,align='center', ecolor='red', capsize=10)
    plt.bar(r2, centralized_bar, width=barWidth, label='Centralized Checkpointing',color='0.40',yerr=centralized_std,align='center', ecolor='red', capsize=10)
    plt.bar(r3, conventional_bar, width=barWidth, label='Conventional Checkpointing', color ='0.60', yerr=conventional_std, align='center', ecolor='red',capsize=10)
    plt.bar(r4, mirrored_bar, width=barWidth, label='Mirrored Checkpointing', color ='0.80', yerr=mirrored_std, align='center', ecolor='red',capsize=10)
    plt.ylabel('Restore Duration(sec)',fontsize=10,fontweight="bold")
    plt.xlabel('Number of replicas',fontsize=10,fontweight="bold")
    #plt.title('Number of replicas vs Restore Duration')
    plt.xticks([r + barWidth for r in range(4)], ('#replicas=4','#replicas=6', '#replicas=8', '#replicas=10'),fontsize=10, rotation=45)
    for i in range(len(r5)):
        plt.text(x = r5[i]-0.1, y = all_bars[i]+0.2, s = all_bars[i], size = 6)
    plt.legend(loc='best',fontsize=10)
    plt.show()
    """
    
    
    
    plt.bar(r1, distributed_bar, width=barWidth, label='Distributed Checkpointing',color='0.20',yerr=distributed_std,align='center', ecolor='red', capsize=10)
    plt.bar(r2, centralized_bar, width=barWidth, label='Centralized Checkpointing',color='0.40',yerr=centralized_std,align='center', ecolor='red', capsize=10)
    plt.bar(r3, conventional_bar, width=barWidth, label='Conventional Checkpointing', color ='0.60', yerr=conventional_std, align='center', ecolor='red',capsize=10)
    plt.bar(r4, mirrored_bar, width=barWidth, label='Mirrored Checkpointing', color ='0.80', yerr=mirrored_std, align='center', ecolor='red',capsize=10)
    plt.ylabel('Memory Footprint(B)',fontsize=10,fontweight="bold")
    plt.xlabel('Number of replicas',fontsize=10,fontweight="bold")
    #plt.title('Number of replicas vs Restore Duration')
    plt.xticks([r + barWidth for r in range(4)], ('#replicas=4','#replicas=6','#replicas=8','#replicas=10'),fontsize=10,rotation=45)
    for i in range(len(r5)):
        plt.text(x = r5[i]-0.1, y = all_bars[i]+0.2, s = all_bars[i], size = 6)
    plt.legend(loc='best',fontsize=10)
    plt.show()

    
    
    



main()

# %%
