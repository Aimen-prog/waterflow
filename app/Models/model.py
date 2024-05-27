import pickle
import numpy as np

class Modelr:
    def __init__(self, model_path):
        #loading the trained model
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, features):
        # features = np array
        features = np.array(features).reshape(1, -1)
        prediction = self.model.predict(features)
        return prediction.tolist()
    
