#Finding maximum and minimum number from the array/list

L1 = [58, 93, 12, 84, 62, 32, 10, 110, 0, 1]

class MinMax(object):
    def __init__(self, my_list):
        self.my_list = my_list

    def get_max_num(self):
        max_num = self.my_list[0]
        for i, num in enumerate(self.my_list):
            if self.my_list[i] > max_num:
                max_num = self.my_list[i]
        return max_num

    def get_min_num(self):
        min_num = self.my_list[0]
        for i , num in enumerate(self.my_list):
            if self.my_list[i] < min_num:
                min_num = self.my_list[i]
        return min_num

MinMaxObject = MinMax(L1)
maximum = MinMaxObject.get_max_num()
print("Maximum number is : {}" .format(maximum))
minimum = MinMaxObject.get_min_num()
print("Minimum number is : {}" .format(minimum))


