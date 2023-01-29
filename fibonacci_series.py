#this is programm to print fibonacci series upto nterms.
#nterms = positive integer


class Fibonacci(object):
    def fibonacci_ser(self, nterms):
        self.nterms = nterms
        n1, n2 = 0, 1
        count = 0

        #check if provided nterms is positive int
        if self.nterms <=0:
            print("Please enter a positive number")
            return 0
        elif self.nterms == 1:
            print("fibonacci series upto", self.nterms, ":")
            print(n1)
            return 0
        else:
            print("Fibonacci series : ")
            while count < self.nterms:
                print(n1)
                nth_num = n1+n2
                #update next values
                n1 = n2
                n2 = nth_num
                count = count + 1

fib_obj = Fibonacci()
fib_obj.fibonacci_ser(10)
