import pandas as pd
from entity.ExperimentCluster import ExperimentCluster


def main():
    df = pd.read_csv(u'data/100Msg.csv')

    _4ReplicaSet_100Events_OurSoln = ExperimentCluster(replicas=4,events=100,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'our') ])
    _4ReplicaSet_100Events_BaseSoln = ExperimentCluster(replicas=4,events=100,dataframe=df[ (df[u'ReplicaSet'] == 4) & (df[u'Solution'] == u'base') ])

    print(u'Duration0: {}'.format(_4ReplicaSet_100Events_OurSoln._experiments[0]._duration_of_new_smoc))
    print(u'Duration1: {}'.format(_4ReplicaSet_100Events_OurSoln._experiments[1]._duration_of_new_smoc))
    print(u'Duration2: {}'.format(_4ReplicaSet_100Events_OurSoln._experiments[2]._duration_of_new_smoc))


    print(u'Duration3: {}'.format(_4ReplicaSet_100Events_BaseSoln._experiments[0]._duration_of_new_smoc))
    print(u'Duration4: {}'.format(_4ReplicaSet_100Events_BaseSoln._experiments[1]._duration_of_new_smoc))
    print(u'Duration5: {}'.format(_4ReplicaSet_100Events_BaseSoln._experiments[2]._duration_of_new_smoc))

    
    #print(u'Statistics = {}'.format(df_4ReplicaSet_OurSoln_1stExp[u'DeltaMemoryUsageInKbFromTop'].describe()))
    #print(u'Mean = {}'.format(df_4ReplicaSet_OurSoln_1stExp[u'DeltaMemoryUsageInKbFromTop'].mean()))







main()