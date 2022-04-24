from joblib import load


class Model:

    def __init__(self, columns):
        self.model = load("assets/modelo.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result

    def calculate_r2(self, x, y):
        r2 = self.model.score(x, y)
        return r2
