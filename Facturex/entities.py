

class Customer:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.surname = kwargs['surname']
        self.nif = kwargs['nif']
        self.price = kwargs['price']
        self.number_of_sessions = kwargs['number_of_sessions']


