#Singleton patterns ensures only one instance of class is created
#Use when control access to shared databases or file
#Use when provide access to global variable

class Singleton(object):
    instance = None

    def __init__(self):
        if Singleton.instance is None:
            Singleton.instance = self

    def get_instance():
        if Singleton.instance == None:
            Singleton()
        else :
            print("Singleton instance already exists")
        return Singleton.instance


s1 = Singleton.get_instance()
print(s1)
s2 = Singleton.get_instance()
print(s2)

if id(s1) == id(s2):
    print("Singleton works, both variables contains same instance id")
else:
    print("Singleton failed, multiple instances created")