__author__ = 'chenye'

from itertools import  permutations

def aspiration_house(preference, assigned_house):
    i = 0
    while i < len(preference):
        if not assigned_house[preference[i]]:
            return preference[i]
        else:
            i +=1


def find_index(lookup_subject, preference):
    i = 0
    while i < len(preference):
        if isinstance(preference[i], tuple):
            if lookup_subject in preference[i]:
                return i
            else:
                i += 1
        else:
            if lookup_subject == preference[i]:
                return i
            else:
                i += 1
    return i

def reverse_assignment(assignment):
    reverse_assign = {}
    for person in assignment:
        houses = assignment[person]
        if isinstance(houses, tuple):
            for house in houses:
                reverse_assign[house] = person
        else:
            reverse_assign[houses] = person
    return reverse_assign

'''
Assuming preferences follows this schematics
{'A' : ['h1', ('h2', 'h3')], ...}
'''
def check_stable_matches(preferences, assignment):
    rev_assignment = reverse_assignment(assignment)
    for person in assignment:
        preference = preferences[person]
        house_assigned = assignment[person]
        house_preference = find_index(house_assigned, preference)

        if house_preference == len(preference):
            return False # Unacceptable assignment

        for i in range(house_preference):
            for house in preference[i]:
                current_owner = rev_assignment[house]
                current_preference_house = find_index(current_owner, preferences[house])
                person_preference_house = find_index(person, preferences[house])
                if person_preference_house < current_preference_house:
                    return False

    return True

def testReverse_Assignment():
    h1 = 'h1'
    h2 = 'h2'
    h3 = 'h3'

    p1 = 'Alice'
    p2 = 'Bob'

    assignment = {p1: h1, p2: (h2, h3)}
    rev_assignment = reverse_assignment(assignment)

    print 'Test reverse_assignment function'
    print '\t Original assignment:', assignment
    print '\t Reversed:', rev_assignment
    assert (rev_assignment[h1] == p1)
    assert (rev_assignment[h2] == p2)
    assert (rev_assignment[h3] == p2)

def test_check_stable_matches1():
    h1 = 'A'
    h2 = 'B'
    h3 = 'C'

    p1 = 's1'
    p2 = 's2'
    p3 = 's3'

    preferences = {p1: [h2, h1, h3],
                   p2: [h1, h2, h3],
                   p3: [h1, h2, h3],

                   h1: [(p1, p2, p3)],
                   h2: [p2, p1, p3],
                   h3: [p3, p1, p2]
    }
    stable_matches = []

    count = 0
    for per in permutations([h1, h2, h3]):
        count += 1
        assignment = {p1: per[0], p2: per[1], p3: per[2]}
        if check_stable_matches(preferences, assignment):
            stable_matches.append(assignment)

    print 'Test 01 check_stable_matches function'
    print '\t All stable matches are ', stable_matches
    assert (len(stable_matches) == 3)
    assert (count == 6)

def test_check_stable_matches2():
    h1 = 'A'
    h2 = 'B'
    h3 = 'C'

    p1 = 's1'
    p2 = 's2'
    p3 = 's3'

    preferences = {p1: [h2, h1, h3],
                   p2: [h1, h2, h3],
                   p3: [h1, h2, h3],

                   h1: [(p1, p2, p3)],
                   h2: [p2, p1, p3],
                   h3: [p3, p1, p2]
    }

    assignment = {p1 : 'D', p2: h1, p3: (h2, h3)}

    print 'Test 02 check_stable_matches function'
    assert(not check_stable_matches(preferences, assignment))

def test_find_index():
    h1 = 'A'
    h2 = 'B'
    h3 = 'C'
    h4 = 'D'
    h5 = 'E'
    h6 = 'F'

    preference = [h1, (h2, h3), (h4), h5]
    assert (find_index(h1, preference) == 0)
    assert (find_index(h2, preference) == 1)
    assert (find_index(h3, preference) == 1)
    assert (find_index(h4, preference) == 2)
    assert (find_index(h5, preference) == 3)
    assert (find_index(h6, preference) == len(preference))
    print 'Test find_index succeeds'

test_find_index()