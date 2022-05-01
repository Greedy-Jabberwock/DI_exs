border = '\n----------------------------------------------------\n'
print(border)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)

    def change_name(self, new_name):
        old_name = self.name
        self.name = new_name
        print(f'{old_name} is {self.name} now.')

first_person = Person("John", 36)
first_person.show_details()  # Output: "Hello my name is John"
first_person.change_name('Victor')

# ------------------------------------------------------------------------
print(border)

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        # Analyse the line below
        print(self) # It will print the addres of Computer class in RAM, because instanse of class will not be initialized. There is no __init__() method.


mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")
