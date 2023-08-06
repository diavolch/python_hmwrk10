# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
#
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("I'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = color

    def fly(self):
        print('Oooooh, meat...')


class AnimalFactory:
    def create_animal(self, animal, *args, **kwargs):
        if animal.lower() == 'fish':
            return Fish(*args, **kwargs)
        elif animal.lower() == 'dog':
            return Dog(*args, **kwargs)
        elif animal.lower() == 'raven':
            return Raven(*args, **kwargs)
        else:
            raise ValueError('Invalid type of animal')


factory = AnimalFactory()

fish = factory.create_animal('fish', 'Nemo', 3, 'grey', 'bul-bul')
dog = factory.create_animal('dog', 'Spark', 2, 'pitbull', 'barkl!')
raven = factory.create_animal('raven', 'Voron', 5, 'black', 'karrr!')

print(fish.name)
print(dog.voice)
raven.fly()