from Experiment import Experiment
import pandas as pd

class ExperimentCluster:
    def __init__(self,**kwargs):
        # 6 replicas means 6 replicas + 1 replica exist in cluster #
        self._number_of_replicas = kwargs.get("replicas") + 1
        self._number_of_events = kwargs.get("events")
        self._dataframe = kwargs.get("dataframe")
        self._experiments = []; self._number_of_experiments = 10
        self._all_memory_footprint = pd.DataFrame()
        self._mean_memory_footprint = 0 ; self._std_memory_footprint = 0 
        self._restore_durations = [] ; self._mean_restore_duration = 0 ; self._std_restore_duration = 0

        # store whole experiments performed for the replica #
        for exp in range(0,self._number_of_experiments):
            df = self._dataframe[ (self._dataframe["Experiment"] == (exp+1) ) ]
            #print("Dataframe of the experiment: {}".format(df))
            experiment = Experiment(experiment_id=exp, dataframe=df)
            # Read all memory footprint dataframe #
            self._all_memory_footprint = pd.concat([self._all_memory_footprint,experiment._memoryFootprint_dataframe],ignore_index=True)
            # Produce list in order to store durations of new smocs #
            self._restore_durations.append(experiment._duration_of_new_smoc)
            # Add new experiment to list
            self._experiments.append(experiment)

        # Produce df from list in order to store durations of new smocs #
        self._all_durations_of_new_smocs = pd.DataFrame(self._restore_durations)

        # Calculate statistics for experiments #
        
        # Mean of memory footprint
        self._mean_memory_footprint = self._all_memory_footprint.mean().values[0]
        self._std_memory_footprint = self._all_memory_footprint.std().values[0]
        
        # Mean of restore duration
        self._mean_restore_duration = self._all_durations_of_new_smocs.mean().values[0]
        self._std_restore_duration = self._all_durations_of_new_smocs.std().values[0]

        

        
          
         


         
         