from numpy import full, nan as NaN
from re import sub as regexp_replace


class Horner(object):

    def __init__(self, polynominal_coefficients):
        self.__polynominal_coefficients = polynominal_coefficients
        self.__number_coefficients = len(polynominal_coefficients)
        self.matrix = full([0, 0], NaN)

    def calculate_value_by_taylor(self, x, evaluation_point, maximum_order):
        taylor_coefficients = self.taylor_coefficients(evaluation_point, maximum_order)
        value = 0
        for n in range(len(taylor_coefficients)):
            value += taylor_coefficients[n] * (x - evaluation_point) ** (self.__number_coefficients - n - 1)
        return value

    def taylor_series_to_string(self, evaluation_point, maximum_order):
        taylor_coefficients = self.taylor_coefficients(evaluation_point, maximum_order)
        string = ''
        for n in range(len(taylor_coefficients)):
            string += ' + {:.2f}*(x-{:.2f})^{:.2f}'.format(taylor_coefficients[n], evaluation_point, self.__number_coefficients - n - 1)
        string = string[2 : ]
        string = regexp_replace(r'\*\(x-\d+\.\d*\)\^0\.00', '', string)
        string = regexp_replace(r' 1\.00\*', ' ', string)
        string = regexp_replace(r'\.00', '', string)
        return string


    def taylor_coefficients(self, evaluation_point, maximum_order):
        self.calculate_horner_schema(evaluation_point, maximum_order)
        coefficients = []
        for col in range(self.matrix.shape[1]):
            coefficient = self.matrix[self.__col_length(col) - 1, col]
            coefficients.append(coefficient)
        return coefficients

    def calculate_horner_schema(self, evaluation_point, maximum_order):
        maximum_order = self.__maximum_order_to_validate_order(maximum_order)
        self.__initialize_matrix(maximum_order)
        self.__initialize_first_row(maximum_order)
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
        number_rows = 2 * self.__number_coefficients + 1
        number_cols = maximum_order + 1
        self.matrix = full([number_rows, number_cols], NaN)

    def __initialize_first_row(self, maximum_order):
        reversed_coefficients = self.__polynominal_coefficients[: : -1]
        self.matrix[0, :] = reversed_coefficients[0 : maximum_order+1]

    def __initialize_first_column(self):
        row_indices = [2 * i for i in range(self.__number_coefficients + 1)]
        for index in row_indices:
            self.matrix[index, 0] = self.matrix[0, 0]

    def __fill_matrix(self, x):
        for current_col in range(1, self.matrix.shape[1]):
            for current_row in range(1, self.__col_length(current_col)):
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