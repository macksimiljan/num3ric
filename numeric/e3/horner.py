from numpy import full, nan as NaN, uint64
from re import sub as regexp_replace


class Horner(object):

    def __init__(self, polynominal_coefficients):
        self.__polynominal_coefficients = polynominal_coefficients
        self.__number_coefficients = len(polynominal_coefficients)
        self.complete_horner_schema = True
        self.matrix = full([0, 0], NaN)

    def calculate_value_by_taylor(self, x, evaluation_point, maximum_order):
        taylor_coefficients = self.taylor_coefficients(evaluation_point, maximum_order)
        value = 0
        for n in range(len(taylor_coefficients)):
            value += taylor_coefficients[n] * (x - evaluation_point) ** n
        return value

    def taylor_series_to_string(self, evaluation_point, maximum_order):
        taylor_coefficients = self.taylor_coefficients(evaluation_point, maximum_order)
        string = ''
        for n in range(len(taylor_coefficients)):
            string += ' + {:.2f}*(x-{:.2f})^{:.2f}'.format(taylor_coefficients[n], evaluation_point, n)
        string = string[2 : ]
        string = regexp_replace(r'\*\(x-\d+\.\d*\)\^0\.00', '', string)
        string = regexp_replace(r' 1\.00\*', ' ', string)
        string = regexp_replace(r'\.00', '', string)
        return string


    def taylor_coefficients(self, evaluation_point, maximum_order):
        self.calculate_horner_schema(evaluation_point, maximum_order)
        coefficients = []
        for row in range(2, self.matrix.shape[0], 2):
            col = int(self.matrix.shape[1] - row / 2)
            coefficient = self.matrix[row, col]
            coefficients.append(coefficient)
        return coefficients

    def calculate_horner_schema(self, evaluation_point, maximum_order, complete=True):
        self.complete_horner_schema = complete
        maximum_order = self.__maximum_order_to_validate_order(maximum_order)
        self.__initialize_matrix(maximum_order)
        self.__initialize_first_row()
        self.__initialize_first_column()
        self.__fill_matrix(evaluation_point)
        return self.matrix

    def __maximum_order_to_validate_order(self, maximum_order):
        if maximum_order < 0:
            maximum_order = 0
        elif maximum_order > self.__number_coefficients - 1:
            maximum_order = self.__number_coefficients - 1
        return maximum_order

    def __initialize_matrix(self, maximum_order):
        number_rows = 1 + 2 * (maximum_order + 1)
        number_cols = self.__number_coefficients
        self.matrix = full([number_rows, number_cols], NaN)

    def __initialize_first_row(self):
        reversed_coefficients = self.__polynominal_coefficients[: : -1]
        self.matrix[0, :] = reversed_coefficients

    def __initialize_first_column(self):
        row = 2
        while row < self.matrix.shape[0]:
            self.matrix[row, 0] = self.matrix[0, 0]
            row += 2

    def __fill_matrix(self, x):
        for current_col in range(1, self.matrix.shape[1]):
            for current_row in range(1, self.matrix.shape[0]):
                if current_col <= self.matrix.shape[1] - abs(current_row / 2):
                    self.__determine_cell(x, current_row, current_col)

    def __col_length(self, current_col):
        maximum_length = self.matrix.shape[0]
        return maximum_length - 2 * current_col

    def __determine_cell(self, x, current_row, current_col):
        if self.__is_even(current_row):
            self.__calculate_cell_even_row(current_row, current_col)
        else:
            self.__calculate_cell_odd_row(x, current_row, current_col)

    def __calculate_cell_even_row(self, row, col):
        self.matrix[row, col] = self.matrix[row - 1, col] + self.matrix[row - 2, col]

    def __calculate_cell_odd_row(self, x, row, col):
        self.matrix[row, col] = self.matrix[row + 1, col - 1] * x

    @staticmethod
    def __is_even(natural_number):
        return natural_number % 2 == 0