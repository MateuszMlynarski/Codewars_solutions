class List(object):
    def remove_(self, integer_list, values_list):
        self.integer_list = integer_list
        self.values_list = values_list
        return [i for i in self.integer_list if i not in self.values_list]