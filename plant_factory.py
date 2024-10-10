from dataclasses import dataclass

from plant import Plant


@dataclass
class PlantFactory:

    plants = {}

    def get_plant(self, name: str, plant_type: str, color: str):
        key = (name, plant_type, color)
        if key not in self.plants:
            self.plants[key] = Plant(name, plant_type, color)
            print(f"Создано новое растение: {name}")
        return self.plants[key]


if __name__ == "__main__":
    plant = PlantFactory()
    print(plant.get_plant("Папоротник", "Травянистое", "Зеленый"))
    print(plant.plants)
