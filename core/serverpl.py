from helper.NRZ import NRZtobits

def serverpl(NRZstream):
    bits = NRZtobits(NRZstream)
    return bits