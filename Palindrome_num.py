#This is the programm to check if given number is palindrome or not

class Palindrome(object):
    """take input number and check for palindrome or not
       returns 0 if number is palindrome
       return 1 if number is not palindrome
    """
    def palindrome_num(self):
        in_num = input("Enter number : ")
        in_num = str(in_num)
        if in_num == in_num[::-1]:
            print("Given number is Palindrome")
            return 0
        print("Given number is not Palindrome")
        return 1

Palindrome_obj = Palindrome()
Palindrome_obj.palindrome_num()