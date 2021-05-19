class Student(object):
    def __init__(self,first_name, last_name, programme): #define this class
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
    def information(self): #define a function in this class to print students' information
        info = self.first_name + '.' + self.last_name + ' ' + self.programme
        return info



me = Student('Siming', 'Zhong', 'BMS') #input a student

print(me.information())
