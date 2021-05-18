import os
import re

os.chdir("C:\\Users\嘤嘤怪的一朵玫瑰花\IBI1_2020-21\Practical8")

sequence = ''
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as fin, open('unknown_function.fa', 'w') as fout:
    for line in fin:
        if line.startswith('>') and re.search('unknown function', line):
            new_name = re.findall(r'gene:(\S+)', line)
            while True:
                line = next(fin)
                if not line.startswith('>'):
                    sequence += line.replace('\n', '')
                else:
                    break
            length = len(sequence)
            fout.write('\n' + '>>' + str(new_name) + '             ' + str(length))
            fout.write('\n' + str(sequence))