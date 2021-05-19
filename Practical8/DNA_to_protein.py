import re
seq = 'ATGCGACTACGATCGAGGGCC' #input DNA sequence
#write genetic code table
genetic_code_table = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
         'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
         'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
         'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
         'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
         'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
         'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
         'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
         'TAT':'Y','TAC':'Y','TAA':'O','TAG':'U',
         'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
         'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
         'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
         'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
         'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
         'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
         'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
DNA_codons = re.findall('...',seq)#extract the DNA codons from the sequence
print('The protein sequence is ', end='')
for i in range(len(DNA_codons)): #translate the DNA codons into proteins
    print(genetic_code_table[DNA_codons[i]], end = '')
print('.')
