from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import seaborn as sns

np.seterr(divide='ignore', invalid='ignore')

class Model:

    def __init__(self):
        #Create a Gaussian Classifier
        self.gnb = GaussianNB()
        print("model initiallized")

    def train(self, data):
        df = pd.DataFrame(data)
        sns.pairplot(df)
        self.gnb.fit(df[['cod', 'coa', 'speed']], df['action'])
        print("trained for data: \n", df[['cod', 'coa', 'speed', 'action']])

    def predict(self, cod, coa, speed):

        # print('predicting action... ')

        try :
            predicted_action = self.gnb.predict([[cod, coa, speed]])
            # print('predicted action: ', predicted_action)
            return predicted_action[0]
        except Exception as e: 
            # print(e)
            return 0
