class Student(object):
    def __init__(self,first_name, last_name, programme):
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
    def information(self):
        info = self.first_name + '.' + self.last_name + ' ' + self.programme
        return info



me = Student('Siming', 'Zhong', 'BMS')

print(me.information())