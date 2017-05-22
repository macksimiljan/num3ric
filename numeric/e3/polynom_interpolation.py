class PolynomInterpolation(object):

    def __init__(self, stuetzstellen):
        self.stuetzstellen = stuetzstellen
        self.formula_newton = ''
        self.formula_lagrange = ''

    def polynom_newton(self, x):
        y = self.dividierte_differenz(0, 0)
        self.formula_newton = str(y)
        for j in range(1, len(self.stuetzstellen)):
            div_differenz = self.dividierte_differenz(0, j)
            self.formula_newton += ' + ' + str(div_differenz)
            produkt = 1
            for k in range(j):
                produkt *= (x - self.stuetzstellen[k][0])
                self.formula_newton += '*(x-' + str(self.stuetzstellen[k][0]) + ')'
            y += div_differenz * produkt
        return y

    def polynom_lagrange(self, x):
        y = 0
        for j in range(len(self.stuetzstellen)):
            l = self.lagrange_koeffizient(j, x)
            y += l * self.stuetzstellen[j][1]
            self.formula_lagrange += ' * ' + str(self.stuetzstellen[j][1]) + ' + '
        self.formula_lagrange = self.formula_lagrange[ : -3]
        return y

    def lagrange_koeffizient(self, j, x):
        l = 1
        for i in range(len(self.stuetzstellen)):
            if i != j:
                numerator = x - self.stuetzstellen[i][0]
                denominator = self.stuetzstellen[j][0] - self.stuetzstellen[i][0]
                l *= numerator / denominator
                self.formula_lagrange += '(x-' + str(self.stuetzstellen[i][0]) + ')/' + str(self.stuetzstellen[j][0] - self.stuetzstellen[i][0]) + '*'
        self.formula_lagrange = self.formula_lagrange[ : -1]
        return l

    def dividierte_differenz(self, i, k):
        if k == 0:
            return self.stuetzstellen[i][1]
        else:
            numerator = self.dividierte_differenz(i + 1, k - 1) - self.dividierte_differenz(i, k - 1)
            denominator = self.stuetzstellen[i + k][0] - self.stuetzstellen[i][0]
            return numerator / denominator