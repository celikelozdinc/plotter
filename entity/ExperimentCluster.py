from entity.Experiment import Experiment
import pandas as pd

class ExperimentCluster:
    def __init__(self,**kwargs):
        self._number_of_replicas = kwargs.get(u'replicas')
        self._number_of_events = kwargs.get(u'events')
        self._dataframe = kwargs.get(u'dataframe')
        self._experiments = []; self._number_of_experiments = 3
        self._whole_memory_footprint = pd.DataFrame() ; self._mean_memory_footprint = 0 ; self._std_memory_footprint = 0
        self._whole_restore_duration = pd.DataFrame() ; self._mean_restore_duration = 0 ; self._std_restore_duration = 0

        # store whole experiments performed for the replica #
        for exp in range(1,(self._number_of_experiments +1)):
            df = self._dataframe[ (self._dataframe[u'Experiment'] == exp ) ]
            experiment = Experiment(experiment_id=exp, dataframe=df)
            # Read all memory footprint dataframe #
            self._whole_memory_footprint = pd.concat([self._whole_memory_footprint,experiment._memoryFootprint_dataframe],ignore_index=True)
            # Read all restore duration dataframe #
            self._whole_restore_duration = pd.concat([self._whole_restore_duration,experiment._duration_dataframe],ignore_index=True)
            self._experiments.append(experiment)

        # Calculate statistics for experiments #
        # Mean of memory footprint
        self._mean_memory_footprint = self._whole_memory_footprint.mean().values[0]
        self._std_memory_footprint = self._whole_memory_footprint.std().values[0]
        # Mean of restore duration
        self._mean_restore_duration = self._whole_restore_duration.mean().values[0]
        self._std_restore_duration = self._whole_restore_duration.std().values[0]
        print(u'...STATISTICS OF EXPERIMENT...')
        print(u'Mean of memory footprint ---> {}'.format(self._mean_memory_footprint))
        print(u'Std of memory footprint ---> {}'.format(self._std_memory_footprint))
        print(u'Mean of restore duration ---> {}'.format(self._mean_restore_duration))
        print(u'Std of restore duration ---> {}'.format(self._std_restore_duration))

        

        
          
         


         
         