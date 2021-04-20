#import libaries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
import seaborn as sns
import re

sns.set(style="whitegrid")



class formulaOneData:

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def data_sets(self):

        #import the DATASETS
        results = pd.read_csv(self.BASE_PATH + '/datasets/results.csv')
        circuits = pd.read_csv(self.BASE_PATH  + '/datasets/circuits.csv')
        races = pd.read_csv(self.BASE_PATH  + '/datasets/races.csv')


        #Merge the Datasets on inner
        cir_race_set = pd.merge(circuits,races, how='inner', on='circuitId')
        data = pd.merge(cir_race_set,results, how='inner', on='raceId')



        #Drop Columns not needed
        data = data.drop(['lat', 'lng', 'round', 'grid', 'url_x', 'statusId', 'driverId', 'constructorId',
                          'number', 'grid', 'alt', 'positionText', 'positionOrder', 'points',
                          'fastestLap', 'rank', 'milliseconds', 'resultId','url_y'],
                         axis=1)

        #Gets the first place times from the first position and turn into a float
        data = data.loc[data['position'] == "1"]
        data['fastestLapSpeed'] = data['fastestLapSpeed'].replace('\\N', np.nan)
        data['fastestLapSpeed'] = data['fastestLapSpeed'].astype(float)
        data['Dates'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
        data['Year'] = pd.to_datetime(data['year'], format='%Y')



        #Series to Model
        test_series = data[['circuitId','raceId','Year', 'laps', 'fastestLapSpeed', 'Dates', 'country']]
        print(test_series.dtypes)
        print(test_series.describe())
        print(test_series)


        '''Distribution Plot'''
        #sns.distplot(test_series['fastestLapSpeed'], bins=30)

        '''Jointplot'''
        # sns.jointplot(x='laps', y='fastestLapSpeed', data=test_series, kind="hex")
        # sns.jointplot(x='laps', y='fastestLapSpeed', data=test_series, kind="reg")

        '''Pair Plot'''
        #sns.pairplot(test_series, hue='country', palette='coolwarm')

        '''Rugplot'''
        #sns.rugplot(test_series['fastestLapSpeed'])

        '''Barplot Categorical'''
        sns.barplot(x='country',y='fastestLapSpeed', data=test_series)

        plt.xticks(rotation=70)
        plt.tight_layout()
        plt.show()








if __name__ == "__main__":
    f1 = formulaOneData()
    f1.data_sets()
