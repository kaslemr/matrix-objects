class Matrix(Vector):
    pass

class Vector:

    def __init__(self, value):
        self.value = value
        self.counter = 0
        self.empty_list = []
        return

    def __str__(self):
        return "{}".format(self.value)

    def magnitude(self):
        self.total = 0
        for x in self.value:
            self.total += x**2
        return self.total**0.5

    def shape_checker(self):
        for x in self.value:
            self.counter += 1
        self.empty_list.append(self.counter)
        self.empty_list = tuple(self.empty_list)
        return self.empty_list

    def vector_scalar_mult(self, value_scalar):
        return [x * value_scalar for x in self.value]

     
