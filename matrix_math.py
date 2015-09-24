class Matrix(Vector):

    def __init__(self, value):
        self.value = value
        self.shape = []
        self.new_matrix = []
        return

    def __str__(self):
        return "{}".format(self.value)

    def matrix_shape(self):
        self.rows = sum((isinstance(x, list) for x in self.value))
        if self.rows == 0:
            self.shape.append(len(self.value))
            return self.shape
        else:
            self.shape.append(self.rows)
            for x in self.value:
                self.columns = sum(isinstance(a, int) for a in x)
            self.shape.append(self.columns)
            return self.shape

    def matrix_scalar(self, value_scalar):
        self.new_matrix = [[col * scalar for col in x] for x in self.value]
        return self.new_matrix


class Vector:

    def __init__(self, value):
        self.value = value
        self.counter = 0
        self.shape_checker_list = []
        self.dot_product_list = []
        self.add_list = []
        self.sub_list = []
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

    def __mul__(self, value_scalar):
        return [x * value_scalar for x in self.value]

    def dot(self, other):
        self.vector_shape_checker(other)
        self.counter = -1
        for x in self.value:
            self.counter += 1
            addition_num = other.value[self.counter]
            new_num = x * addition_num
            self.dot_product_list.append(new_num)
        return sum(self.dot_product_list)

    def __add__(self, other):
        self.vector_shape_checker(other)
        self.counter = -1
        for x in self.value:
            self.counter += 1
            addition_num = other.value[self.counter]
            new_num = x + addition_num
            self.add_list.append(new_num)
        return self.add_list

    def __sub__(self, other):
        self.vector_shape_checker(other)
        self.counter = -1
        for x in self.value:
            self.counter += 1
            addition_num = other.value[self.counter]
            new_num = x - addition_num
            self.sub_list.append(new_num)
        return self.sub_list
