from animal_factory import AnimalFactory
from plant_factory import PlantFactory


if __name__ == "__main__":
    tiger = AnimalFactory()
    tiger.get_animal("Тигр", "Лес")
    print(tiger.animals)
    lion = AnimalFactory()
    lion.get_animal("Лев", "Саванна")
    print(lion.animals)
    lion2 = AnimalFactory()
    lion2.get_animal("Лев", "Саванна")
    print(lion2.animals)

    cactus = PlantFactory()
    cactus.get_plant("Папоротник", "Травянистое", "Зеленый")
    print(cactus.plants)
    cactus2 = PlantFactory()
    cactus2.get_plant("Папоротник", "Травянистое", "Зеленый")
    print(cactus2.plants)
