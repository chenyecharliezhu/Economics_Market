__author__ = 'chenye'
'''
Two goods scenario
    budget_and_utilities = {person: [budget, u1, u2], ...}
'''
def price_clearing_two_goods(budget_and_utilities, supply):
    market_demand = {}
    committed_budget = [0, 0]
    budget_for_each_good = [0, 0]
    swaying_budget = 0

    for p in budget_and_utilities:
        budget, u1, u2 = budget_and_utilities[p]
        if u1 != 0 and u2 != 0:
            ratio = float(u1)/float(u2)
            market_demand[ratio] = market_demand.get(ratio, 0) + budget
            swaying_budget += budget
        elif u1 == 0 and u2 != 0:
            committed_budget[1] += budget
        elif u1 != 0 and u2 == 0:
            committed_budget[0] += budget
        else:
            print p, 'doesn\'t want to purchase either good :('

    critical_points = market_demand.keys()
    critical_points.sort()

    p1, p2 = price_discoveries(market_demand, supply, critical_points, committed_budget, swaying_budget)

    if p1 is None or p2 is None:
        return None
    else:
        n = 0
        person = []
        consumption_good = [0, 0]
        aggregate_budget = 0
        consumption = {}
        utility = {}
        for p in budget_and_utilities:
            budget, u1, u2 = budget_and_utilities[p]
            if float(u1)/float(u2) > float(p1)/float(p2):
                consumption[p] = [float(budget)/float(p1), 0]
                utility[p] = float(budget)/float(p1)*float(u1)
                consumption_good[0] += float(budget)/float(p1)
            elif float(u1)/float(u2) < float(p1)/float(p2):
                consumption[p] = [0, float(budget)/float(p2)]
                utility[p] = float(budget)/float(p2)*float(u2)
                consumption_good[1] += float(budget)/float(p2)
            else:
                n += 1
                person.append(p)
                aggregate_budget += budget
        if n > 0:
            consumption_left = [supply[0] - consumption_good[0], supply[1] - consumption_good[1]]
            for p in person:
                consumption[p] = [consumption_left[0] * float(budget) / float(aggregate_budget), \
                                  consumption_left[1] * float(budget) / float(aggregate_budget)]
                utility[p] = (consumption_left[0] * float(budget) / float(aggregate_budget)) * float(u1) + \
                             (consumption_left[1] * float(budget) / float(aggregate_budget)) * float(u2)

    return (p1, p2), consumption, utility

def price_discoveries(market_demand, supply, critical_points, committed_budget, swaying_budget):
    budget_for_each_good = [committed_budget[0] + swaying_budget, committed_budget[1]]
    total_budget = sum(budget_for_each_good)

    for i in range(len(critical_points)):
        if budget_for_each_good[0] != 0 and budget_for_each_good[1] != 0:
            p1 = float(budget_for_each_good[0]) / float(supply[0])
            p2 = float(budget_for_each_good[1]) / float(supply[1])
            if p1 / p2 < critical_points[i]:
                return p1, p2

        swaying_budget = market_demand[critical_points[i]]
        budget_for_each_good[0] -= swaying_budget
        p2 = float(total_budget) / float(supply[0] * critical_points[i] + supply[1])
        p1 = float(critical_points[i]) * p2
        x = supply[0] * p1 - budget_for_each_good[0]
        if x >= 0 and swaying_budget >= x:
            return p1, p2

        budget_for_each_good[1] += swaying_budget

    if budget_for_each_good[0] != 0 and budget_for_each_good[1] != 0:
        p1 = float(budget_for_each_good[0]) / float(supply[0])
        p2 = float(budget_for_each_good[1]) / float(supply[1])
        if p1 / p2 > critical_points[len(critical_points) - 1]:
            return p1, p2

    return None, None

def test01():
    p1 = '1'
    p2 = '2'
    p3 = '3'

    o1 = 'R'
    o2 = 'S'
    o3 = 'T'

    budget_and_utilities = {p1: [100, 120, 90],
                            p2: [100, 120, 60],
                            p3: [100, 120, 30]}
    supply = [1, 1]

    (price1, price2), consumption, utility = price_clearing_two_goods(budget_and_utilities, supply)
    assert (price1 == 200.0)
    assert (price2 == 100.0)
    assert (utility[p1] == 90.0 and consumption[p1][0] == 0 and consumption[p1][1] == 1)
    assert (utility[p2] == 60.0 and consumption[p2][0] == 0.5 and consumption[p2][1] == 0)
    assert (utility[p3] == 60.0 and consumption[p3][0] == 0.5 and consumption[p3][1] == 0)

def test02():
    p1 = '1'
    p2 = '2'
    p3 = '3'

    o1 = 'R'
    o2 = 'S'
    o3 = 'T'

    budget_and_utilities = {p1: [100, 120, 90],
                            p2: [200, 120, 60],
                            p3: [100, 120, 30]}
    supply = [1, 1]

    (price1, price2), consumption, utility = price_clearing_two_goods(budget_and_utilities, supply)
    assert (price1 == 800.0/3.0)
    assert (price2 == 400.0/3.0)
    assert (utility[p1] == 67.5 and consumption[p1][0] == 0 and consumption[p1][1] == 3.0/4.0)
    assert (utility[p2] == 90 and consumption[p2][0] == 5.0/8.0 and consumption[p2][1] == 1.0/4.0)
    assert (utility[p3] == 45 and consumption[p3][0] == 3.0/8.0 and consumption[p3][1] == 0)

test01()
test02()
