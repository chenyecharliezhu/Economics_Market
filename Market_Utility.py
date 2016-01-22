__author__ = 'chenye'

def aspiration_house(preference, assigned_house):
    i = 0
    while i < len(preference):
        if not assigned_house[preference[i]]:
            return preference[i]
        else:
            i +=1
