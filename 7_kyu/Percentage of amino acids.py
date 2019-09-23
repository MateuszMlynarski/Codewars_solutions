def aa_percentage(protein, aminoacids=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    return round(sum([protein.count(aminoacid) for aminoacid in aminoacids]) * 100 / len(protein))

#best practice
# def aa_percentage(seq, residues=["A", "I", "L", "M", "F", "W", "Y", "V"]):
#   return round(sum(seq.count(r) for r in residues)/len(seq)*100)