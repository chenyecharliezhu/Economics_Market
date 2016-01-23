__author__ = 'chenye'

from Market_Utility import aspiration_house
from random import sample

'''
Top Trading Cycle
'''
def TTC(persons, houses, owner, preference):

    assignment = {p: None for p in persons}
    assigned_house = {h: False for h in houses}
    not_assigned = set(persons)

    while len(not_assigned) != 0:
        desire = {}
        for person in not_assigned:
            desire[person] = aspiration_house(preference[person], assigned_house)
        sequence = []
        cycle_found = False
        current_person = sample(not_assigned, 1)[0]
        while not cycle_found:
            sequence.append(current_person)
            current_house = desire[current_person]
            sequence.append(current_house)
            current_person = owner[current_house]
            if current_person in sequence:
                cycle_found = True

        cycle_pointer = sequence.index(current_person)
        while cycle_pointer < len(sequence):
            assignment[sequence[cycle_pointer]] = sequence[cycle_pointer + 1]
            not_assigned.remove(sequence[cycle_pointer])
            assigned_house[sequence[cycle_pointer + 1]] = True
            cycle_pointer += 2
    return assignment


def testTTC():
    p1 = 'Madeline'
    p2 = 'Ben'
    p3 = 'Noah'
    p4 = 'Parents'

    h1 = 1
    h2 = 2
    h3 = 3
    h4 = 4

    persons = (p1, p2, p3, p4)
    houses = (h1, h2, h3, h4)
    owner = {h1: p1,h2: p2, h3: p3, h4: p4}
    preference = {p1: [h2, h1, h3, h4], p2: [h4, h3, h1, h2], p3: [h4, h1, h3, h2], p4: [h2, h1, h4, h3]}

    print TTC(persons, houses, owner, preference)

testTTC()