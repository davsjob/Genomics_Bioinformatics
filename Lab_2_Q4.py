#Q4 David Sjöberg

import sys
import re

def geneinfo(inputfile):
    
    #Opens and read the file
    with open(inputfile, 'r') as input_f:  
        #Lists of names and sequences
        names = []
        sequences = []
        
        #The regex searchpatterns used
        genename = re.compile("(?<=gene=)([^]]+)\.*")
        sequence = re.compile("^[^>].+")
        
        #Iterates over file
        for line in input_f:
            #Search for both name and sequence
            name = re.search(genename, line)
            seqstring = re.search(sequence,line)
            if name: #Adds name to list if match
                names.append(name.group(1))
            if seqstring: #Adds sequence to list if match
                sequences.append(seqstring.group(0))

        #Creates two dictionaries, one with name and sequence, and the second with names and the sequence lenght
        info = {names[i] : sequences[i] for i in range(len(names))}
        nameslen = {i : len(info[i]) for i in info}

        #Prints the output
        print(f'Total number of sequences are: \n', len(sequences))      
        print(f'The genes in the file are: \n', [key for key in info])
        print(f'Gene-name and its lenght are: \n', nameslen)
        
#Makes the input a userinput from commandline      
inputfile = sys.argv[1]
geneinfo(inputfile)