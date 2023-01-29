#This is the programm to find out first unique number in given list

class Unique(object):
    def __init__(self, my_list):
        self.my_list = my_list

    def getUniqueNum(self):
        #check length of given list
        if len(self.my_list) == 0:
            print("empty list")
            return 0
        elif len(self.my_list) == 1:
            print("Unique number in the list is : ", self.my_list[0])
        else:
            for i in self.my_list:
                if self.my_list.count(i) == 1:
                    print("First unique number is :",i)
                    return 0
        print("Unique number not found in given list")
        return 0

Uniq_obj = Unique('7,7,1,1,2,3,3')
Uniq_obj.getUniqueNum()