#normal method to get square of number

my_list = [1,2,3,4,5,6,7,8,9,10]
sq_list = []
for num in my_list:
    sq_list.append(num * num)
print(sq_list)

#This code uses list comprehension

square_list = [num * num for num in my_list]
print(square_list)

#Using lambda and map function

square_list1 = map((lambda num : num * num), my_list)
print(list(square_list1))

#Even numbers using lambda and filter function

even_list = filter((lambda num: num % 2 == 0), my_list)
print(list(even_list))

#Odd numbers using lambda and filter function
odd_list = filter((lambda num : num % 2 != 0), my_list)
print(list(odd_list))

print("This is added to check SCM polling jenkins")

