DNA_seq = 'atGCGACTACGATCGAgggCC'


def reverse_complement_calculator(origin_seq):
    inter_seq1 = origin_seq.upper()
    inter_seq2 = []
    complement_table = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    for i in range(len(inter_seq1)):
        inter_seq2 += list(complement_table[inter_seq1[i]])
    inter_seq2.reverse()
    final_seq = ''.join(inter_seq2)
    print(final_seq)
    return

reverse_complement_calculator(DNA_seq)