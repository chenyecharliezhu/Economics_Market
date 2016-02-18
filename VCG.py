__author__ = 'chenye'

def VCG(bids, clicks):
    assert (len(bids) > len(clicks))
    assert (clicks == sorted(clicks, reverse=True))

    extended_clicks = clicks + [0]
    sorted_bids = [(bid, i) for i, bid in enumerate(bids)]
    sorted_bids.sort(reverse=True)

    assignment = []
    price = []

    rolling_price = 0
    K = len(clicks)

    for k in range(K,0,-1):
        rolling_price += sorted_bids[k][0] * (extended_clicks[k - 1] - extended_clicks[k])
        price.append(float(rolling_price) / float(clicks[k - 1]))
        assignment.append(sorted_bids[k-1][1])

    assignment.reverse()
    price.reverse()
    return assignment, price

def test():
    values = [4, 10, 2]
    bids = values
    clicks = [200, 100]

    print VCG(bids, clicks)

test()