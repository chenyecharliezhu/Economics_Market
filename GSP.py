__author__ = 'chenye'

def lowest_clearing_price(values, clicks):
    assert (len(values) > len(clicks))
    assert (clicks == sorted(clicks, reverse=True))
    assignment = []
    price = []

    sorted_values = [(value, i) for i, value in enumerate(values)]
    sorted_values.sort(reverse=True)
    K = len(clicks)

    p_last = float(sorted_values[K][0])
    price.append(p_last)
    assignment.append(sorted_values[K-1][1])

    for k in range(K-1,0,-1):
        p_last = sorted_values[k][0] -(sorted_values[k][0] - p_last) * float(clicks[k]) / float(clicks[k-1])
        price.append(p_last)
        assignment.append(sorted_values[k-1][1])

    assignment.reverse()
    price.reverse()
    return assignment, price

def highest_clearing_price(values, clicks):
    assert (len(values) > len(clicks))
    assert (clicks == sorted(clicks, reverse=True))
    assignment = []
    price = []

    sorted_values = [(value, i) for i, value in enumerate(values)]
    sorted_values.sort(reverse=True)
    K = len(clicks) - 1

    p_last = float(sorted_values[K][0])
    price.append(p_last)
    assignment.append(sorted_values[K][1])

    for k in range(K , 0,-1):
        p_last = sorted_values[k - 1][0] -(sorted_values[k - 1][0] - p_last) * float(clicks[k]) / float(clicks[k-1])
        price.append(p_last)
        assignment.append(sorted_values[k-1][1])

    assignment.reverse()
    price.reverse()
    return assignment, price

def test():
    values = [8, 6, 4, 2]
    clicks = [300, 200, 100]
    print lowest_clearing_price(values, clicks)
    print highest_clearing_price(values, clicks)

test()