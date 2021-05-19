from xml.dom.minidom import parse
import xml.dom.minidom
import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:\\Users\嘤嘤怪的一朵玫瑰花\IBI1_2020-21\Practical14")

DOMTree = xml.dom.minidom.parse("go_obo.xml") #build a domtree
root = DOMTree.documentElement #find the root in DOMTree
terms = root.getElementsByTagName("term") #define "terms" as all the term in root tree

def find_id(terms): #define a function to find the id in terms
    dict={} #create a dictionary to store all the id
    for term in terms: #to find the terms with is_a and all the id
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")] #define a list contains the content in "is_a"
        all_id = term.getElementsByTagName("id")[0].childNodes[0].data
        for ids in is_a:
            if ids in dict:
                dict[ids].append(all_id)
            else:
                dict[ids] = [all_id] #edit the dictionary
    return dict


def related(terms,biomolecule): #define a function to indentify the type of molecule and store the ids of one kind of molecule in one list
    gene = [] #define gene
    for term in terms:
        defstrs = term.getElementsByTagName("defstr")[0].childNodes[0].data #the name of biomolecule is shown in defstr
        id_specific = term.getElementsByTagName("id")[0].childNodes[0].data #find the ids of the specific molecule
        if not biomolecule.isupper():
            defstrs = defstrs.lower() #unify the format
        if biomolecule in defstrs:
            gene.append(id_specific) #add this id to the list of that specific molecule
    return set(gene) #delete repeadted ids


def extract_nodes(dict,ls): #define a function to extract the nodes
    all_nodes = []
    for i in ls:
        if i in dict:
            a = dict[i]
            all_nodes += a #store all the notes in a list
            all_nodes += extract_nodes(dict,a)
    return all_nodes


def num_childnodes(terms,biomolecule): #define a function to calculate all the childnodes
    dict = find_id(terms)
    b = related(terms,biomolecule)
    c = extract_nodes(dict,b) #extract all the childnotes
    num_childnodes= len(set(c)) #calculate the total number of childnotes
    return num_childnodes

DNA = num_childnodes(terms,"DNA") # count the number of different molecules (DNA, RNA, protein,oligosaccharide)
RNA = num_childnodes(terms,"RNA")
protein = num_childnodes(terms,"protein")
oligosaccharide = num_childnodes(terms,"oligosaccharide")

print("The number of childNodes of all DNA-related terms is:",DNA) #print the results
print("The number of childNodes of all RNA-related terms is:",RNA)
print("The number of childNodes of all protein-related terms is:",protein)
print("The number of childNodes of all oligosaccharide-related terms is:",oligosaccharide)


#draw a pie chart to show the results
labels = 'DNA', 'RNA', 'protein', 'oligosaccharide' #label the pie chart
sizes = [DNA, RNA, protein, oligosaccharide]
plt.title('The number of childNodes related with DNA, RNA, protein and oligosaccharide')
plt.pie(sizes,
        explode=(0, 0, 0, 0),
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
plt.show()