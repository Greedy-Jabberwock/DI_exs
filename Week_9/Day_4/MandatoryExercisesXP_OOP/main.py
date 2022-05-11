from random import randint, choice


class Human:
    def __init__(self, name, age, building=None):
        self.name = name
        self.age = age
        self.building = building

    def move(self, building):
        if isinstance(building, Building):
            building.inhabitants.append(self)
        else:
            print('Wrong type of object to move!')


class Building:
    def __init__(self, address, inhabitants=[]):
        self.address = address
        self.inhabitants = inhabitants

    def __repr__(self):
        return f'Building on {self.address}. Inhabitants amount - {len(self.inhabitants)}'


class City:
    def __init__(self, name, buildings=[]):
        self.name = name
        self.buildings = buildings

    def construct(self, address):
        self.buildings.append(Building(address))

    def info(self, given_address):
        buildings_count = 0
        citizens_count = 0
        total_citizens_ages = 0
        for item in self.buildings:
            if item.address == given_address:
                buildings_count += 1
                for inhabitant in item.inhabitants:
                    citizens_count += 1
                    total_citizens_ages += inhabitant.age
        average = round(total_citizens_ages / citizens_count)
        print(f'In {self.name} there are {buildings_count} buildings\n'
              f'Average age of citizens is {average} age.')


def main():
    rostov = City('Rostov')
    address = 'Apple Str.'
    for _ in range(15):
        rostov.construct(address)

    for building in rostov.buildings:
        for _ in range(randint(2, 10)):
            building.inhabitants.append(Human('Some name', randint(12, 90)))

    for building in rostov.buildings:
        for citizen in building.inhabitants:
            print(citizen.age)

    rostov.info(address)


main()
