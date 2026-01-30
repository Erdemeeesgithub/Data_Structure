class Person:
    # TODO: Please write your code here
    def __init__(self, first_name, last_name, age, hobbies):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age
        self.hobbies = list(hobbies)
        
    def introduce(self):
        if len(self.hobbies) == 1:
            hobby_str = self.hobbies[0]
        elif len(self.hobbies) == 2:
            hobby_str = self.hobbies[0] + " and " + self.hobbies[1]
        else:
            hobby_str = ", ".join(self.hobbies[:-1]) + ", and " + self.hobbies[-1]

        return f"Hi, my name is {self.first_name} {self.last_name}. I like {hobby_str}."
    
    def add_hobbies(self, new_hobbies):
        for hobby in new_hobbies:
            if hobby not in self.hobbies:
                self.hobbies.append(hobby)

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
