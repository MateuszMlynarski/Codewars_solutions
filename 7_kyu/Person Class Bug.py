class Person():

    def __init__(self, first_name, last_name, age):
        self.full_name = '{} {}'.format(first_name, last_name)
        self.age=age