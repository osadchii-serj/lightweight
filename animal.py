from dataclasses import dataclass
from typing import Dict

@dataclass
class Animal:

    species: str
    habitat: str

    def display(self, location: Dict[int, int]):
        print(
            f"Животное: {self.species} Среда обитания: {self.habitat} Местоположение: {location}"
        )


if __name__ == "__main__":
    lion = Animal("Лев", "Саванна")
    lion.display({10, 20})
