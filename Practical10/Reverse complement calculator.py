DNA_seq = 'atGCGACTACGATCGAgggCC' #input DNA sequence


def reverse_complement_calculator(origin_seq): #define reverse complement calculator function
    inter_seq1 = origin_seq.upper() #change all the letters into upper letters
    inter_seq2 = []
    complement_table = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'} #input dictionary(complement table)
    for i in range(len(inter_seq1)):
        inter_seq2 += list(complement_table[inter_seq1[i]])
    inter_seq2.reverse() #reverse the list
    final_seq = ''.join(inter_seq2) #combine the lists
    print(final_seq)
    return

reverse_complement_calculator(DNA_seq) #run this function
