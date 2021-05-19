import os
import re
import itertools

os.chdir("C:\\Users\嘤嘤怪的一朵玫瑰花\IBI1_2020-21\Practical8") #change work directory


#input genetic code table
genetic_code_table = {
         'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
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

sequence = '' #define sequence
seq_name = '' #define seq_name
with open('unknown_function.fa', 'r') as fin, open('unknown_proteins.fa', 'w') as fout:  #read the original file and write a new file
    for line in fin: #find the line start with '>', which is the line contains gene name
        if line.startswith('>'):
            seq_name = line
            while True:
                line = next(fin) #go to the next line
                if not line.startswith('>'): #find the sequence line
                    DNA_codons = re.findall('...', line) #extract DNA codons from the sequence
                    protein = ''
                    proteins = []
                    for i in range(len(DNA_codons)): #translate the DNA codons into proteins
                        protein += genetic_code_table[DNA_codons[i]]
                    proteins.append(protein)

                else:
                    break
            fout.write('\n' + str(seq_name)) #write gene name in the file
            fout.write('\n' + str(proteins)) #write protein sequence in the file