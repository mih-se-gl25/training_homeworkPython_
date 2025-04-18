class BaseAnimal:
    """docstring for BaseAnimal."""
    def __init__(self, name,hungry,color):
        self.name = name
        self.hungry = hungry
        self.color = color
    
    def hello(self):
        return f"{self.name}"
    
    def trick(self):
        return f"{self.color}"
    
    def feed(self):
        return f"{self.hungry}"

    
a = BaseAnimal("bob","meat","red")
print(a.color)