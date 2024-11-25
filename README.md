# Key Concepts of Object Oriented Programming
## This task will allow you to practice implementing encapsulation, inheritance and polymorphism

You are going to create a simple program to monitor a tracker for an animal shelter

Your instructions are as follows:

1. Create a base class called Animal, and give it the following private attributes
    * `name` (str)
    * `species` (str)
    * `age` (int)
    * `adopted` (bool)
    Create getter and setter methods for each of these to ensure data protection and controlled access

2. Create two subclasses of animal called Dog and Cat with the following additions:
    * The Dog class inherits from Animal and has an additional private attribute - `breed`(str)
    * The Cat class inherits from Animal and has an additional private attribute - `indoor_only` (bool)
    Again create suitable getters and setters for these

    Override the `__str__` method in each subclass - refer to the test cases in the test file to figure out the formatting of the output

3. Add a `make_sound` method to the Animal class which __returns__ the generic message `"This animal makes a sound" `

    Override this method in both subclasses, so that for Dog it returns `"Woof!` and for Cat it returns `"Meow!"`

Ensure that all test cases pass on submission