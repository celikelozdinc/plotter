class Experiment:

    def __init__(self,**kwargs):
        self._experiment_id = kwargs.get(u'experiment_id')
        self._experiment_dataframe = kwargs.get(u'dataframe')
        
        # Calculate duration of the new smoc inside the replica #
        self._duration_dataframe = self._experiment_dataframe[u'RestoreDurationInSec']
        self._duration_of_new_smoc = self._duration_dataframe.tail(1).values[0]

        # Calculate sum of memory footprint inside the replica # 
        self._memoryFootprint_dataframe = self._experiment_dataframe[u'DeltaMemoryUsageInKbFromTop']
        self._memoryFootprint_of_replica = self._memoryFootprint_dataframe.sum()
