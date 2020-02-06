class Experiment:

    def __init__(self,**kwargs):
        self._experiment_id = kwargs.get(u'experiment_id')
        self._experiment_dataframe = kwargs.get(u'dataframe')
        
        self._duration_dataframe = self._experiment_dataframe[u'RestoreDurationInSec']
        self._duration_of_new_smoc = self._duration_dataframe.tail(1).values[0]

        self._memoryFootprint_dataframe = self._experiment_dataframe[u'DeltaMemoryUsageInKbFromTop']
        self._memoryFootprint_of_replica = self._memoryFootprint_dataframe.sum()
