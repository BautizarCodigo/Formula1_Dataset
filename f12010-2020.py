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
        print(data['Year'])

        #print(data['Year'])
        #print(type(data['Year']))


        test_series= data[['circuitId','raceId','Year', 'laps', 'fastestLapSpeed', 'Dates']]
        #print(test_series)


        #print(data.dtypes)
        #print(type(data['fastestLapTime'].iloc[1]))

        x = test_series['fastestLapSpeed']
        y = test_series['Year']

        sns.jointplot(x,y, )

        #print(test_series['Year'])



        #Boxplot Chart
        #sns.boxplot(x=data["fastestLapSpeed"])

        #Scatter Chart
        #sns.scatterplot(data=data, x="circuitId", y="fastestLapSpeed", hue='circuitId')

        #
        # sns.catplot(data=data, kind="bar",
        #     x="circuitId", y="fastestLapSpeed", palette="dark", alpha=.6, height=6
        # )

        plt.show()






if __name__ == "__main__":
    f1 = formulaOneData()
    f1.data_sets()
