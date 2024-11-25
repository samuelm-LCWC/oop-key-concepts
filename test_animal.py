from animal import Animal, Cat, Dog
import pytest

def test_animal():
    new_animal = Animal(name="Fido", species="Dog", age=4, adopted=False)
    assert new_animal.get_name() == "Fido"
    assert new_animal.get_species() == "Dog"
    assert new_animal.get_age() == 4 
    assert new_animal.get_adopted() == False

def test_animal_setters():
    new_animal = Animal(name="Fido", species="Dog", age=4, adopted=False)
    new_animal.set_name("Felix")
    new_animal.set_species("Cat")
    new_animal.set_age(5)
    new_animal.set_adopted(True)
    assert new_animal.get_name() == "Felix"
    assert new_animal.get_species() == "Cat"
    assert new_animal.get_age() == 5
    assert new_animal.get_adopted() == True

def test_dog():
    new_dog = Dog(name="Fido", species="Dog", age=4, breed="Cocker Spaniel", adopted=False)
    assert new_dog.get_name() == "Fido"
    assert new_dog.get_age() == 4
    assert new_dog.get_species() == "Dog"
    assert new_dog.get_adopted() == False

def test_cat():
    new_cat = Cat(name="Felix", species="Cat", age=5, indoor_only=False, adopted=True)
    assert new_cat.get_name() == "Felix"
    assert new_cat.get_species() == "Cat"
    assert new_cat.get_age() == 5
    assert new_cat.get_indoor_only() == False
    assert new_cat.get_adopted() == True

def test_str():
    new_dog = Dog(name="Fido", species="Dog", age=4, breed="Cocker Spaniel", adopted=False)
    new_cat = Cat(name="Felix", species="Cat", age=5, indoor_only=False, adopted=True)
    assert new_dog.__str__() == "Name: Fido\nSpecies: Dog\nBreed: Cocker Spaniel\nAge: 4\nAdopted status: False"
    assert new_cat.__str__() == "Name: Felix\nSpecies: Cat\nAge: 5\nIndoor only status: False\nAdopted status: True"

def test_sounds():
    new_dog = Dog(name="Fido", species="Dog", age=4, breed="Cocker Spaniel", adopted=False)
    new_cat = Cat(name="Felix", species="Cat", age=5, indoor_only=False, adopted=True)
    new_animal = Animal(name="Fred", species="Fish", age=2, adopted=False)
    assert new_animal.make_sound() == "This animal makes a sound"
    assert new_dog.make_sound() == "Woof!"
    assert new_cat.make_sound() == "Meow!"
