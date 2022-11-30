#First check-in
class Employee(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        print("Name of employee is %s" %self.name)

    def getSurName(self):
        print("Surname of employee is %s" %self.surname)

    def getFullName(self):
        fullName = self.name + " " +self.surname
        print("Fullname of employee is %s" %fullName)

    def getEmailId(self):
        emailId = self.name.lower()+"."+self.surname.lower()+"@xyz.com"
        print("Email id of %s is %s" %(self.name, emailId))

Employee_1 = Employee("Manisha","Shirke")
Employee_1.getName()
Employee_1.getSurName()
Employee_1.getFullName()
Employee_1.getEmailId()




