from random import randint


class Building:
    def __init__(self, address, inhabitants=None):
        self.address = address
        self.inhabitants = [] if inhabitants is None else inhabitants

    def __repr__(self):
        return f'Building on {self.address}. Inhabitants amount - {len(self.inhabitants)}'


class Human:
    def __init__(self, name, age, building=None):
        self.name = name
        self.age = age
        self.building = building

    def move(self, building: Building):
        # (+)rather than doing this check you can add annotation to building like building: Building
        building.inhabitants.append(self)


class City:
    def __init__(self, name, buildings=None):
        self.name = name
        self.buildings = [] if buildings is None else buildings

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
        print(f'In {self.name} there are {buildings_count} buildings.\n'
              f'Average age of citizens is {average} age.')


def main():
    rostov = City('Rostov')
    address = 'Apple Str.'
    for _ in range(15):
        rostov.construct(address)

    for building in rostov.buildings:
        for _ in range(randint(2, 10)):
            building.inhabitants.append(Human('Some name', randint(12, 90)))

    rostov.info(address)


main()
