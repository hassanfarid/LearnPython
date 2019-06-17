class TransformClass:
    def __init__(self):
        print("Transformation begins")
    def add_power(self, data):
        for i,v in enumerate(data):
            data[i] = v*v
        return data