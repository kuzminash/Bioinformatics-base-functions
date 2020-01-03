def PatternMatching(Pattern, Genome):
    n = len(Genome)
    k = len(Pattern)
    positions = []
    for position in range(n-k+1):
        if Genome[position:position+k] == Pattern:
            positions.append(position)
    return positions