from entity.Experiment import Experiment


class ExperimentCluster:
     def __init__(self,**kwargs):
         self._number_of_replicas = kwargs.get(u'replicas')
         self._number_of_events = kwargs.get(u'events')
         self._dataframe = kwargs.get(u'dataframe')
         self._experiments = []

         for exp in range(1,4):
             df = self._dataframe[ (self._dataframe[u'Experiment'] == exp ) ]
             experiment = Experiment(experiment_id=exp, dataframe=df)
             self._experiments.append(experiment)
         


         
         