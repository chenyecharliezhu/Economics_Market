__author__ = 'chenye'

from collections import deque


'''
Deferred Acceptance
    Marriage Problem
'''

def DA(male, female, preferences):
    def propose(m, g, temporary_pairing, preferences_g):
        current_m = temporary_pairing[g]

        if current_m is not None:
            current_index = preferences_g.index(current_m)
        else:
            current_index = len(preferences_g)

        try:
            m_index = preferences_g.index(m)
        except ValueError:
            m_index = len(preferences_g)

        if m_index < current_index:
            temporary_pairing[g] = m
            return current_m
        else:
            return m

    temporary_pairing = {f: None for f in female}
    proposal_tracking = {m: -1 for m in male}
    need_to_propose = deque(male)

    while need_to_propose:
        m = need_to_propose.popleft()
        last_proposed = proposal_tracking[m]
        if last_proposed < len(preferences[m]) - 1:
            g = preferences[m][last_proposed + 1]
            proposal_tracking[m] = last_proposed + 1
            result = propose(m, g, temporary_pairing, preferences[g])
            if result:
                need_to_propose.append(result)
        else:
            temporary_pairing[m] = None

    return temporary_pairing

def testDA1():
    m1 = "m1"
    m2 = "m2"
    m3 = "m3"

    w1 = "w1"
    w2 = "w2"
    w3 = "w3"

    men = [m1, m2, m3]
    women = [w1, w2, w3]

    preferences = {m1: [w1, w2, w3],
                   m2: [w3, w2, w1],
                   m3: [w3, w1, w2],

                   w1: [m2, m3, m1],
                   w2: [m2, m3, m1],
                   w3: [m2, m1, m3]}
    assignment = DA(men, women, preferences)
    print "Test Case 1 :", assignment


def testDA2():
    m1 = "m1"
    m2 = "m2"
    m3 = "m3"
    m4 = "m4"

    w1 = "w1"
    w2 = "w2"
    w3 = "w3"
    w4 = "w4"

    men = [m1, m2, m3, m4]
    women = [w1, w2, w3, w4]

    preferences = {m1: [w2, w4, w3, w1],
                   m2: [w2, w1, w3, w4],
                   m3: [w2, w3, w4, w1],
                   m4: [w4, w2, w1, w3],

                   w1: [m1, m3, m4, m2],
                   w2: [m4, m2, m1, m3],
                   w3: [m2, m4, m3, m1],
                   w4: [m1, m3, m4, m2]}
    assignment = DA(men, women, preferences)
    print "Test Case 2 :", assignment

testDA1()
testDA2()





