def add_tip(total, tip_percent):
    ''' Return the total amount of a meal including tip'''
    tip = tip_percent*total
    return total + tip
def hyp(leg1, leg2):
    leg3 = (leg1**2 + leg2**2)**0.5
    return leg3