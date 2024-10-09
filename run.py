from dataclasses import dataclass
from typing import Dict


@dataclass
class Plant:

    name: str
    plant_type: str
    color: str

    def display(self, location: Dict[int, int]):
        print(
            f"Растение: {self.name} Тип: {self.plant_type} Цвет: {self.color} Местоположение: {location}"
        )


if __name__ == "__main__":
    plant = Plant("Папоротник", "Травянистое", "Зеленый")
    plant.display({10, 20})
