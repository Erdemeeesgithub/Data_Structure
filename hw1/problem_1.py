class Person:
    # TODO: Please write your code here
    def __init__(self, FirstName, LastName, age, hobbies):
        self.FirstName = FirstName
        self.LastName = LastName
        self.age = age
        self.hobbies = hobbies
        
    def introduce(self):
        if len(self.hobbies) == 1 :
            hobby_str = self.hobbies[0]
        elif len(self.hobbies) == 2: 
            hobby_str = self.hobbies[0] + " and " + self.hobbies[1]
        else:
            return None
            
        print(f'Hi, My name is {self.FirstName} {self.LastName}. And I like {hobby_str}')
    
    # def add_hobbies(self,other):
        """
        The function `add_hobbies` takes two objects as input and combines their hobbies into a single
        list.
        
        :param other: The `other` parameter in the `add_hobbies` function seems to represent another
        object or instance that also has a `hobbies` attribute. By adding the `hobbies` of the `self`
        object (the object on which the method is called) with the `hobbies` of
        """
    #     hobbies = self.hobbies + other.hobbies
    #     return hobbies

# Do not change or remove the code below this point
def main():
    # Instantiate the first person and display their introduction.
    p1 = Person("John", "Doe", 20, ["playing guitar"])
    print(p1.introduce())
    # Expected Output:
    # Hi, my name is John Doe. I like playing guitar.

    # Instantiate the second person and display their introduction.
    p2 = Person("Peter", "Wang", 24, ["driving cars", "jogging"])
    print(p2.introduce())
    # Expected Output:
    # Hi, my name is Peter Wang. I like driving cars and jogging.

    # Test adding hobbies to the second person.
    p2.add_hobbies(["jogging", "diving"])
    print(p2.introduce())
    # Expected Output:
    # Hi, my name is Peter Wang. I like driving cars, jogging, and diving.

    # Additional test: Instantiate a third person.
    p3 = Person("Alice", "Smith", 30, ["reading", "swimming"])
    print(p3.introduce())
    # You may test additional scenarios by adding more hobbies.
    p3.add_hobbies(["swimming", "cycling", "reading"])
    print(p3.introduce())


if __name__ == "__main__":
    main()
