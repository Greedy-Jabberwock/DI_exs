from random import randint


class Organism:
    def __init__(self, can_mutate=True):
        self.dna = DNA()
        self.generation = 0
        self.can_mutate = can_mutate

    def print_organism(self):
        self.dna.print_dna()

    def mutate(self):
        self.dna.mutate()

    def get_gens_string(self):
        gens_string = ''
        for chromosome in self.dna.dna:
            for gen in chromosome.chromosome:
                gens_string += f'{gen.gen}'
        return gens_string

    def check_mutation(self):
        if self.get_gens_string() != len(self.get_gens_string()):
            return True
        return False

    def count_generations_amount(self):
        if self.get_gens_string() != len(self.get_gens_string()):
            self.generation += 1
            self.mutate()
            print(f'{self.generation} generation')
        else:
            print('*******************************************')
            print('Can\'t mutate anymore.')
            print(f'Gens: {self.get_gens_string()}')
            print(f'It takes {self.generation} generations.')
            print('*******************************************')


class DNA:
    def __init__(self):
        self.dna = [Chromosome() for _ in range(10)]

    def print_dna(self):
        header = '\t=================== DNA ===================='
        border = '\t============================================'
        print(header)
        for chromosome in self.dna:
            print(chromosome.print_chromosome())
        print(border)

    def mutate(self):
        for i in range(0, randint(0, len(self.dna))):
            # rand_index = randint(0, randint(0, len(self.dna)))
            self.dna[i].mutate()


class Chromosome:
    def __init__(self):
        self.chromosome = [Gen() for _ in range(10)]

    def print_chromosome(self):
        border = '------------------------------------'
        ch_str = ''
        for _ in self.chromosome:
            ch_str += f'{_.gen}'
        return f'\t\t{border}\n\t\t\t\t\t{ch_str}\n\t\t{border}'

    def mutate(self):
        gens = self.chromosome
        for i in range(randint(0, len(gens)-1)):
            # rand_index = randint(0, len(gens)-1)
            gens[i].mutate()


class Gen:
    def __init__(self):
        self.gen = randint(0, 1)

    def mutate(self):
        if randint(0, 1):
            if self.gen:
                self.gen -= 1
            else:
                self.gen += 1


org1 = Organism()
org2 = Organism()
org3 = Organism()

org1.print_organism()
org2.print_organism()
org3.print_organism()

while org1.check_mutation() or org2.check_mutation() or org3.check_mutation():

    org1.count_generations_amount()
    org2.count_generations_amount()
    org3.count_generations_amount()

    if org1.generation == 3_000_000 or org2.generation == 3_000_000 or org3.generation == 3_000_000:
        break
