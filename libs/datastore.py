

class DataStore:

    data = None

    @classmethod
    def init(cls):
        cls.data = []

    @classmethod
    def insert(cls, val):
        cls.data.append(val)

    @classmethod
    def list_all(cls):
        return cls.data
