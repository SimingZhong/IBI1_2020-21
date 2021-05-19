import os
import re

os.chdir("C:\\Users\嘤嘤怪的一朵玫瑰花\IBI1_2020-21\Practical8") #change working directory

sequence = '' #define sequence
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as fin, open('unknown_function.fa', 'w') as fout: #read the original file and write a new file
    for line in fin:
        if line.startswith('>') and re.search('unknown function', line): #find the line with unknown function
            new_name = re.findall(r'gene:(\S+)', line) #extract the gene name
            while True:
                line = next(fin) #go to the next line
                if not line.startswith('>'): #if this line is sequence line
                    sequence += line.replace('\n', '') #combine the sequence
                else:
                    break
            length = len(sequence) #calculate the length
            fout.write('\n' + '>>' + ''.join(new_name) + '             ' + str(length))
            fout.write('\n' + str(sequence))
