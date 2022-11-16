class Soda():

    # Class initializer
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, cost, soda_type_id):
        self.id = id
        self.cost = cost
        self.soda_type = soda_type_id