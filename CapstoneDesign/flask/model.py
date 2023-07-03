import pickle
import os
import sklearn

class LinearRegression():
    model = None

    def __init__(self):
        pki_path = os.path.join(os.path.dirname(__file__), 'pickle', 'test.pkl')
        self.model = pickle.load(open(pki_path, 'rb'))
    
    def predict(self, hour):
        result = self.model.predict([[hour]])
        return result
