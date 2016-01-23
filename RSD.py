__author__ = 'chenye'

from itertools import  permutations
from Market_Utility import aspiration_house

'''
Random Serial Dictatorship
'''
def RSD(persons, houses, preferences):

    statistics_count = {p: {h: 0 for h in houses} for p in persons}

    housing_assignments = {}
    for per in permutations(persons):
        assigned_houses = {h: False for h in houses}
        assignment = {p: None for p in persons}
        for current_person in per:
            house_wanted = aspiration_house(preferences[current_person], assigned_houses)
            assigned_houses[house_wanted] = True
            assignment[current_person] = house_wanted
            statistics_count[current_person][house_wanted] += 1
        housing_assignments[per] = assignment

    return statistics_count, housing_assignments

def testRSD():
    md = 'MD'
    gt = 'GT'
    m = 'Macro'
    i = 'Intro'

    L = 'Levin'
    T = 'Taylor'
    N = 'Niderle'
    K = 'Klenow'

    classes = (md, gt, m, i)
    economists = (L, T, N, K)
    preferences ={L: [md, gt, m, i], T: [m, i, md, gt], N: [m, gt, i, md], K: [md, gt, i, m]}
    statistics, class_assignments = RSD(economists, classes, preferences)
    print class_assignments[(L, T, N, K)]
    print statistics

testRSD()