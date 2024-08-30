class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
        
    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")
            
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем фрукт как съедобный

# Создание объектов

flower = Flower("Роза")
fruit = Fruit("Яблоко")

mammal = Mammal("Кролик")
predator = Predator("Волк")

# Результат взаимодействия

print(f"{mammal.name}")
print(f"{predator.name}")

print(f"{mammal.alive}")
print(f"{predator.fed}")

mammal.eat(flower)
predator.eat(fruit)

print(f"{mammal.alive}")
print(f"{predator.fed}")
