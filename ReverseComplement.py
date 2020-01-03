def Reverse(Pattern):
    Reverse_Pattern = ''.join(reversed(Pattern))
    return Reverse_Pattern

def Complement(Pattern):
    Complements = {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C',
    }
    complement = ""
    for char in Pattern:
        complement += Complements.get(char)
    return complement

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern