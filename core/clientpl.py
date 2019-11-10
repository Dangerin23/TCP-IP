from helper.NRZ import bitstoNRZ

def clientpl(frames):
    NRZstream = ""

    # Create a NRZ-I signal from bits
    for frame in frames:
        frame = bitstoNRZ(frame)
        NRZstream += frame

    return NRZstream
