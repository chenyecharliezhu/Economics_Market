__author__ = 'chenye'

from Market_Utility import  aspiration_house
from itertools import permutations

'''
Top Priority Line
'''
def TPL(persons, houses, owner, preferences):

    statistics_count = {p: {h: 0 for h in houses} for p in persons}

    current_tenants = set(owner[h] for h in owner.keys())

    housing_assignments = {}
    permutations_list = permutations(persons)
    for per in permutations_list:
        assigned_houses = {h: False for h in houses}
        assignment = {p: None for p in persons}
        order = list(per)
        while len(order) > 0:
            current_person = order[0]
            house_wanted = aspiration_house(preferences[current_person], assigned_houses)
            cycle_found = False

            if current_person in current_tenants:
                cycle_person = current_person
                cycle_house = house_wanted
                sequence = [cycle_person, cycle_house]
                while assignment[cycle_person] is None \
                        and cycle_house in owner.keys() \
                        and owner[cycle_house] not in sequence:
                    cycle_person = owner[cycle_house]
                    cycle_house = aspiration_house(preferences[cycle_person], assigned_houses)
                    sequence.append(cycle_person)
                    sequence.append(cycle_house)

                if cycle_house in owner.keys(): # Cycle
                    cycle_pointer = sequence.index(owner[cycle_house])
                    while cycle_pointer < len(sequence):
                        assignment[sequence[cycle_pointer]] = sequence[cycle_pointer + 1]
                        assigned_houses[sequence[cycle_pointer + 1]] = True
                        order.remove(sequence[cycle_pointer])
                        cycle_pointer += 2
                    cycle_found = True

            if not cycle_found:
                if house_wanted not in owner \
                        or assignment[owner[house_wanted]] is not None \
                        or owner[house_wanted] == current_person:
                    assignment[current_person] = house_wanted
                    assigned_houses[house_wanted] = True
                    order.remove(current_person)
                else:
                    existing_tenant = owner[house_wanted]
                    order.remove(existing_tenant)
                    order.insert(0, existing_tenant)

        housing_assignments[per] = assignment
        for p in assignment:
            statistics_count[p][assignment[p]] += 1

    return statistics_count, housing_assignments


def testTPL01():
    p1 = 1
    p2 = 2
    p3 = 3

    h1 = 'A'
    h2 = 'B'
    h3 = 'C'

    persons = (p1, p2, p3)
    houses = (h1, h2, h3)
    owner = {h1: p3}
    preferences = {p1: [h1, h2, h3], p2: [h1, h3, h2], p3: [h2, h3, h1]}

    statistics_count, housing_assignments = TPL(persons, houses, owner, preferences)

    specific_case = housing_assignments[(p1, p2, p3)]
    assert(specific_case[p1] == h1)
    assert(specific_case[p2] == h3)
    assert(specific_case[p3] == h2)

    print "Test Case 1 : ", specific_case

def testTPL02():
    p1 = 'Gwen'
    p2 = 'Michael'
    p3 = 'Barack'
    p4 = 'Sarah'

    h1 = 'NY Apartment'
    h2 = 'Miami Mansion'
    h3 = 'White House'
    h4 = 'Igloo'

    persons = (p1, p2, p3, p4)
    houses = (h1, h2, h3, h4)
    owner = {h3: p3}
    preferences = {p1: [h2, h1, h3, h4], p2: [h2, h3, h1, h4], p3: [h1, h2, h3, h4], p4: [h3, h2, h1, h4]}
    statistics_count, housing_assignments = TPL(persons, houses, owner, preferences)

    specific_case = housing_assignments[(p1, p2, p3, p4)]
    assert (specific_case[p1] == h2)
    assert (specific_case[p2] == h3)
    assert (specific_case[p3] == h1)
    assert (specific_case[p4] == h4)

    print "Test Case 2 :", specific_case

def testTPL03():
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
    preferences = {p1: [h2, h1, h3, h4], p2: [h4, h3, h1, h2], p3: [h4, h1, h3, h2], p4: [h2, h1, h4, h3]}
    statistics_count, housing_assignments = TPL(persons, houses, owner, preferences)

    specific_case = housing_assignments[(p1, p2, p3, p4)]
    assert (specific_case[p1] == h1)
    assert (specific_case[p2] == h4)
    assert (specific_case[p3] == h3)
    assert (specific_case[p4] == h2)

    print "Test Case 3 :", specific_case

def testTPL04():
    p1 = 'Gwen'
    p2 = 'Michael'
    p3 = 'Barack'
    p4 = 'Sarah'

    h1 = 'NY Apartment'
    h2 = 'Miami Mansion'
    h3 = 'White House'
    h4 = 'Igloo'

    persons = (p1, p2, p3, p4)
    houses = (h1, h2, h3, h4)
    owner = {h3: p3}
    preferences = {p1: [h2, h1, h3, h4], p2: [h2, h3, h1, h4], p3: [h3, h2, h1, h4], p4: [h3, h2, h1, h4]}
    statistics_count, housing_assignments = TPL(persons, houses, owner, preferences)

    specific_case = housing_assignments[(p1, p2, p3, p4)]
    assert (specific_case[p1] == h2)
    assert (specific_case[p2] == h1)
    assert (specific_case[p3] == h3)
    assert (specific_case[p4] == h4)

    print "Test Case 4 :", specific_case

testTPL01()
testTPL02()
testTPL03()
testTPL04()