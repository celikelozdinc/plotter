#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt


class Storage:

    def __init__(self):
        # Members related to DURATION #
        self._duration_calculations_without_ZK = []
        self._duration_mean_without_ZK = 0
        self._duration_std_without_ZK = 0
        self._duration_calculations_with_ZK = []
        self._duration_mean_with_ZK = 0
        self._duration_std_with_ZK = 0
        # Members related to MEMORY FOOTPRINT #
        self._memoryFootprint_calculations_without_ZK = []
        self._memoryFootprint_calculations_with_ZK = []
        self._memoryFootprint_delta = []
        self._memoryFootprint_delta_mean = 0
        self._memoryFootprint_delta_std = 0
        
        
    def _populate_data(self,file_without_ZK,file_with_ZK):
        self._duration_calculations_without_ZK = genfromtxt(file_without_ZK, dtype=float, delimiter=",", names=True)['Restore_Duration_in_sec']
        self._duration_calculations_with_ZK =  genfromtxt(file_with_ZK, dtype=float, delimiter=",", names=True)['Restore_Duration_in_sec']

        self._memoryFootprint_calculations_without_ZK = genfromtxt(file_without_ZK, dtype=int, delimiter=",", names=True)['Delta_Memory_Usage_in_KB_from_top']
        self._memoryFootprint_calculations_with_ZK = genfromtxt(file_with_ZK, dtype=int, delimiter=",", names=True)['Delta_Memory_Usage_in_KB_from_top']
        self._memoryFootprint_delta = [x - y for x, y in zip(self._memoryFootprint_calculations_with_ZK, self._memoryFootprint_calculations_without_ZK)] 
    

    def _calculate_statistics(self):
        self._duration_mean_without_ZK = np.mean(self._duration_calculations_without_ZK)
        self._duration_std_without_ZK = np.std(self._duration_calculations_without_ZK)

        self._duration_mean_with_ZK = np.mean(self._duration_calculations_with_ZK)
        self._duration_std_with_ZK = np.std(self._duration_calculations_with_ZK)
        
        self._memoryFootprint_delta_mean = np.mean(self._memoryFootprint_delta) 
        self._memoryFootprint_delta_std = np.std(self._memoryFootprint_delta)
        

def generate_plot_for_memory_footprint(_4ReplicaSet, _8ReplicaSet, _12ReplicaSet, _16ReplicaSet):
    print(u'Plot for memory footprint')

    """
    green_bar = (_4ReplicaSet._memoryFootprint_delta_mean, _8ReplicaSet._memoryFootprint_delta_mean, _12ReplicaSet._memoryFootprint_delta_mean, _16ReplicaSet._memoryFootprint_delta_mean)
    default_std = (_4ReplicaSet._memoryFootprint_delta_std, _8ReplicaSet._memoryFootprint_delta_std, _12ReplicaSet._memoryFootprint_delta_std, _16ReplicaSet._memoryFootprint_delta_std)
    """

    green_bar = (_4ReplicaSet._memoryFootprint_delta_mean, _8ReplicaSet._memoryFootprint_delta_mean, _12ReplicaSet._memoryFootprint_delta_mean,_16ReplicaSet._memoryFootprint_delta_mean)
    default_std = (_4ReplicaSet._memoryFootprint_delta_std, _8ReplicaSet._memoryFootprint_delta_std, _12ReplicaSet._memoryFootprint_delta_std, _16ReplicaSet._memoryFootprint_delta_std)

    # the x locations for the groups
    ind = np.arange(4)

    # Figure size
    #plt.figure(figsize=(10,5))

    # the width of the bars
    width = 0.35       

    # Plotting
    plt.bar(ind, green_bar , width, label='Memory consumption difference',color='0.15',yerr=default_std,align='center', ecolor='red', capsize=10)
    #plt.bar(ind + width, blue_bar, width, label='Solution Without Zookeeper',color='b',yerr=our_std,align='center', ecolor='red', capsize=10)
    plt.ylabel('Memory Footprint Delta (KB)',fontsize=20)
    plt.xlabel('Number of replicas',fontsize=20)
    #plt.title('Number of replicas vs Memory Footprint Delta')
    plt.xticks(ind + width / 10, ('#replicas=4', '#replicas=8', '#replicas=12' , '#replicas=16'),fontsize=20)
    plt.legend(loc='best',fontsize=20)
    plt.show()    

def generate_plot_for_duration(_4ReplicaSet, _8ReplicaSet, _12ReplicaSet, _16ReplicaSet):
    print(u'Plot for duration')

    
    green_bar = (_4ReplicaSet._duration_mean_with_ZK, _8ReplicaSet._duration_mean_with_ZK, _12ReplicaSet._duration_mean_with_ZK, _16ReplicaSet._duration_mean_with_ZK)
    blue_bar = (_4ReplicaSet._duration_mean_without_ZK, _8ReplicaSet._duration_mean_without_ZK, _12ReplicaSet._duration_mean_without_ZK,_16ReplicaSet._duration_mean_without_ZK)
    default_std = (_4ReplicaSet._duration_std_with_ZK, _8ReplicaSet._duration_std_with_ZK, _12ReplicaSet._duration_std_with_ZK,_16ReplicaSet._duration_std_with_ZK)
    our_std = (_4ReplicaSet._duration_std_without_ZK, _8ReplicaSet._duration_std_without_ZK, _12ReplicaSet._duration_std_without_ZK, _16ReplicaSet._duration_std_without_ZK)
    

    """
    green_bar = (_4ReplicaSet._duration_mean_with_ZK, _8ReplicaSet._duration_mean_with_ZK, _16ReplicaSet._duration_mean_with_ZK)
    blue_bar = (_4ReplicaSet._duration_mean_without_ZK, _8ReplicaSet._duration_mean_without_ZK,_16ReplicaSet._duration_mean_without_ZK)
    default_std = (_4ReplicaSet._duration_std_with_ZK, _8ReplicaSet._duration_std_with_ZK, _16ReplicaSet._duration_std_with_ZK)
    our_std = (_4ReplicaSet._duration_std_without_ZK, _8ReplicaSet._duration_std_without_ZK, _16ReplicaSet._duration_std_without_ZK)
    """


    """
    green_bar = (_4ReplicaSet._duration_mean_with_ZK, _8ReplicaSet._duration_mean_with_ZK, _12ReplicaSet._duration_mean_with_ZK)
    blue_bar = (_4ReplicaSet._duration_mean_without_ZK, _8ReplicaSet._duration_mean_without_ZK, _12ReplicaSet._duration_mean_without_ZK)
    default_std = (_4ReplicaSet._duration_std_with_ZK, _8ReplicaSet._duration_std_with_ZK, _12ReplicaSet._duration_std_with_ZK)
    our_std = (_4ReplicaSet._duration_std_without_ZK, _8ReplicaSet._duration_std_without_ZK, _12ReplicaSet._duration_std_without_ZK)
    """

    # the x locations for the groups
    ind = np.arange(4)

    # Figure size
    #plt.figure(figsize=(10,5))

    # the width of the bars
    width = 0.35       

    # Plotting
    plt.bar(ind, green_bar , width, label='Solution With Zookeeper',color='0.15',yerr=default_std,align='center', ecolor='red', capsize=10)
    plt.bar(ind + width, blue_bar, width, label='Solution Without Zookeeper',color='0.90',yerr=our_std,align='center', ecolor='red', capsize=10)
    plt.ylabel('Restore Duration(sec)',fontsize=20)
    plt.xlabel('Number of replicas',fontsize=20)
    #plt.title('Number of replicas vs Restore Duration')
    plt.xticks(ind + width / 2, ('#replicas=4', '#replicas=8', '#replicas=12','#replicas=16'),fontsize=20)
    plt.legend(loc='best',fontsize=20)
    plt.show()    

def main(): 
    
    """
    _96Event_4Replicas = Storage(); _96Event_4Replicas._populate_data('our_solution/96_4.csv','base_solution/96_4.csv'); _96Event_4Replicas._calculate_statistics()
    _96Event_8Replicas = Storage(); _96Event_8Replicas._populate_data('our_solution/96_8.csv','base_solution/96_8.csv'); _96Event_8Replicas._calculate_statistics()
    _96Event_12Replicas = Storage(); _96Event_12Replicas._populate_data('our_solution/96_12.csv','base_solution/96_12.csv'); _96Event_12Replicas._calculate_statistics()
    _96Event_16Replicas = Storage(); _96Event_16Replicas._populate_data('our_solution/96_16.csv','base_solution/96_16.csv'); _96Event_16Replicas._calculate_statistics()
    generate_plot_for_duration(_96Event_4Replicas, _96Event_8Replicas, _96Event_12Replicas, _96Event_16Replicas)
    """

    """
    _9600Event_4Replicas = Storage(); _9600Event_4Replicas._populate_data('9600_4_Without_ZK.csv',u'9600_4_With_ZK.csv'); _9600Event_4Replicas._calculate_statistics()
    _9600Event_8Replicas = Storage(); _9600Event_8Replicas._populate_data('9600_8_Without_ZK.csv',u'9600_8_With_ZK.csv'); _9600Event_8Replicas._calculate_statistics()
    _9600Event_12Replicas = Storage(); _9600Event_12Replicas._populate_data('9600_12_Without_ZK.csv',u'9600_12_With_ZK.csv'); _9600Event_12Replicas._calculate_statistics()
    #_9600Event_16Replicas = Storage(); _9600Event_16Replicas._populate_data('9600_16_Without_ZK.csv',u'9600_16_With_ZK.csv'); _9600Event_16Replicas._calculate_statistics()
    #generate_plot_for_duration(_9600Event_4Replicas, _9600Event_8Replicas, _9600Event_12Replicas,"")
    #generate_plot_for_memory_footprint(_9600Event_4Replicas, _9600Event_8Replicas, _9600Event_12Replicas,"")
    """

    
    _960Event_4Replicas = Storage(); _960Event_4Replicas._populate_data('our_solution/960_4.csv','base_solution/960_4.csv'); _960Event_4Replicas._calculate_statistics()
    _960Event_8Replicas = Storage(); _960Event_8Replicas._populate_data('our_solution/960_8.csv','base_solution/960_8.csv'); _960Event_8Replicas._calculate_statistics()
    _960Event_12Replicas = Storage(); _960Event_12Replicas._populate_data('our_solution/960_12.csv','base_solution/960_12.csv'); _960Event_12Replicas._calculate_statistics()
    _960Event_16Replicas = Storage(); _960Event_16Replicas._populate_data('our_solution/960_16.csv','base_solution/960_16.csv'); _960Event_16Replicas._calculate_statistics()
    #generate_plot_for_duration(_960Event_4Replicas, _960Event_8Replicas, _960Event_12Replicas, _960Event_16Replicas)
    generate_plot_for_memory_footprint(_960Event_4Replicas, _960Event_8Replicas, _960Event_12Replicas, _960Event_16Replicas)
    

"""
    # %%
    _4800Event_4Replicas = Storage(); _4800Event_4Replicas._populate_data(u'our_solution/4800_4.csv',u'base_solution/4800_4.csv'); _4800Event_4Replicas._calculate_statistics()
    _4800Event_8Replicas = Storage(); _4800Event_8Replicas._populate_data(u'our_solution/4800_8.csv',u'base_solution/4800_8.csv'); _4800Event_8Replicas._calculate_statistics()
    _4800Event_12Replicas = Storage(); _4800Event_12Replicas._populate_data(u'our_solution/4800_12.csv',u'base_solution/4800_12.csv'); _4800Event_12Replicas._calculate_statistics()
    _4800Event_16Replicas = Storage(); _4800Event_16Replicas._populate_data(u'our_solution/4800_16.csv',u'base_solution/4800_16.csv'); _4800Event_16Replicas._calculate_statistics()
    generate_plot_for_duration(_4800Event_4Replicas, _4800Event_8Replicas, _4800Event_12Replicas, _4800Event_16Replicas)
    #generate_plot_for_memory_footprint(_4800Event_4Replicas, _4800Event_8Replicas, _4800Event_12Replicas, _4800Event_16Replicas)
"""    


"""
    _2400Event_4Replicas = Storage(); _2400Event_4Replicas._populate_data(u'our_solution/2400_4.csv',u'base_solution/2400_4.csv'); _2400Event_4Replicas._calculate_statistics()
    _2400Event_8Replicas = Storage(); _2400Event_8Replicas._populate_data(u'our_solution/2400_8.csv',u'base_solution/2400_8.csv'); _2400Event_8Replicas._calculate_statistics()
    _2400Event_12Replicas = Storage(); _2400Event_12Replicas._populate_data(u'our_solution/2400_12.csv',u'base_solution/2400_12.csv'); _2400Event_12Replicas._calculate_statistics()
    #_2400Event_16Replicas = Storage(); _2400Event_16Replicas._populate_data('2400_16_Without_ZK.csv',u'2400_16_With_ZK.csv'); _2400Event_16Replicas._calculate_statistics()
    #generate_plot_for_duration(_2400Event_4Replicas, _2400Event_8Replicas, _2400Event_12Replicas,"")
    generate_plot_for_memory_footprint(_2400Event_4Replicas, _2400Event_8Replicas, _2400Event_12Replicas,"")
"""

main()

# %%
