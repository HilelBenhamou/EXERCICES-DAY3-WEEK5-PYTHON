import sys

class Currency:
    def __init__(self,value,label):
        self.value=value
        self.label=label

    def __repr__(self):
        return {'value':self.value, 'label':self.label}

    def __str__(self):
        return 'Person(value=' + str(self.value) + ', label=' + self.label + ')'

    def addition(self,value2,another_currency):
        if self.label==another_currency:
            return self.value+value2
        else:
            raise Exception(f'You cannot add {self.label} with {another_currency}')

    def soutract(self,value2,another_currency):
        if self.label==another_currency:
            return self.value-value2

        else:
            print(f'You cannot soustract {self.label} with {another_currency}')

    def multiply(self,value2,another_currency):
        if self.label==another_currency:
            return self.value*value2

        else:
            print(f'You cannot multiply {self.label} with {another_currency}')

    def divide(self,value2,another_currency):
        if self.label==another_currency:
            return self.value/value2

        else:
            print(f'You cannot divide {self.label} with {another_currency}')

if __name__=="__main__":
    euros=Currency(25.5, "€")
    dollar=Currency(30, '$')
    livres=Currency(50, '£')

    print(euros.addition(25,'$'))
    print(livres.divide(50,'$'))