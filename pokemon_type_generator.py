# this program matches one or two Pokemon types with an animal stored in a list

import random

type_list = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground',
             'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dark', 'Dragon', 'Steel', 'Fairy']


def open_and_trim():
    animal_list = []
    file = open('animals')
    line_list = file.readlines()
    for line in line_list:
        animal = []
        line = line.strip()
        line = line.split(' ')
        animal.append(line)
        for group in animal:
            animal_list.append(group)
    return animal_list


animal_list = open_and_trim()


def get_animal_number():
    num = random.randint(1, 119)
    return num


def get_animal(num):
    '''
    Returns the name of the animal
    '''
    animal_list = open_and_trim()
    return animal_list[num - 1][0]


def get_classification(num):
    '''
    Returns the classification of the animal
    '''
    animal_list = open_and_trim()
    return animal_list[num - 1][1]


def random_type():
    num = random.randint(1, 18)
    return type_list[num - 1]


def get_type(classification):
    prob_of_two = random.randint(1, 10)
    if prob_of_two == 2:
        primary = random_type()
        while (classification == 'mammal' or 'bird' or 'reptile' or 'fish') and primary == 'Bug':
            primary = random_type()
        secondary = random_type()
        while (classification == 'mammal' or 'bird' or 'reptile' or 'fish') and primary == 'Bug':
            secondary = random_type()
        while primary == secondary:
            primary = random_type()
            while (classification == 'mammal' or 'bird' or 'reptile' or 'fish') and primary == 'Bug':
                primary = random_type()
            secondary = random_type()
            while (classification == 'mammal' or 'bird' or 'reptile' or 'fish') and primary == 'Bug':
                secondary = random_type()
        types = primary + '/' + secondary
        return types
    else:
        type = random_type()
        while (classification == 'mammal' or 'bird' or 'reptile' or 'fish') and type == 'Bug':
            type = random_type()
        return type


def main():
    num = get_animal_number()
    animal = get_animal(num)
    classification = get_classification(num)
    type = get_type(classification)
    type_pairing = type + ' ' + animal
    print()
    print('A randomly generated animal/type pairing is: ' + type_pairing)


main()
