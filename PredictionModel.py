from joblib import load
from outlremover import OutlierRemover

class Model:

    def __init__(self, columns):
        self.model = load("assets/modelo.pkl")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result

    def calculate_r2(self, x, y):
        r2 = self.model.score(x, y)
        return r2
