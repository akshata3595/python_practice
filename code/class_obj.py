class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter String:")

    def print_String(self):
        print("Convert as upper():", self.str1.upper())
        print("Convert as lower():", self.str1.lower())
        print("Convert as capitalize():", self.str1.capitalize())
        print("Convert as swapcase():", self.str1.swapcase())
        print("Get Range Slicing:", self.str1[2:5])

str1 = IOString()
str1.get_String()
str1.print_String()
