from dataclasses import dataclass
from animal import Animal


@dataclass
class AnimalFactory:

    animals = {}

    def get_animal(self, species: str, habitat: str):
        key = (species, habitat)

        if key not in self.animals:
            self.animals[key] = Animal(species, habitat)
            print(f"Создано новое животное: {species}")
        return self.animals[key]


if __name__ == "__main__":
    animal_factory = AnimalFactory()
    print(animal_factory.get_animal("Лев", "Саванна"))
    print(animal_factory.animals)
