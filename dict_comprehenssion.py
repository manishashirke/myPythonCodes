#This programm will convert two list into dictionary

List1 = [1,2,3,4,5,6]
List2 = ["Owee", "Sanvi", "Charlotte", "Victoria", "Eva", "Monica"]

my_dict = {num:name for (num, name) in zip(List1, List2)}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict[3] = "Leona"
print(my_dict)
