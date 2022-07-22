class user():
    def __init__(self,name,contact_details):
        self.name=name
        self.contact_deatils=contact_details
    
    def get_name(self):
        return f'This brand is {self.name}'

    def get_contact_details(self):
        return f'This brand is {self.name}'

class student(user):
    def __init__(self,name,contact_details,classe,roll_no):
        
        super().__init__(name,contact_details)
        self.classe=classe
        self.roll_no=roll_no


    def get_classe(self):
        return f'This brand is {self.classe}'
    
    def get_roll_no(self):
        return f'This brand is {self.roll_no}'
        
class Teacher(user):
    def __init__(self,name,contact_details,subject,salary):
        
        super().__init__(name,contact_details)
        self.subject=subject
        self.salary=salary


    def get_subject(self):
        return f'This brand is {self.subject}'
    
    def get_salary(self):
        return f'This brand is {self.salary}'

class Bus(user):
    def __init__(self,name,contact_details,bus_color,bus_name):
        
        super().__init__(name,contact_details)
        self.bus_color=bus_color
        self.contact_deatils=contact_details


    def get_bus_color(self):
        return f'This brand is {self.bus_color}'
    
    def get_bus_name(self):
        return f'This brand is {self.bus_name}'

detail=Teacher('mohit','6367790103','Physics','50000')
print(detail.get_name)
print(detail.get_contact_details)
print(detail.get_subject)
print(detail.get_salary)

        