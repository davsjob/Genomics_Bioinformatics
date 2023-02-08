#Q2 David Sjöberg

import sys

def convertsequential(input, output):
    with open(input, 'r') as input_f, open(output, 'w') as output_f: #choses input and output files
        seq = "" #sequence stored as a string
        for line in input_f: #interates over lines
            if line.startswith(">"): #checks if if its a header
                if seq: #if seq contains anything
                    output_f.write(seq + "\n") #writes sequence
                    seq = ""
                output_f.write(line) #writes header 
            else:
                seq += line.strip() #removes linebreaks from fasta files
        if seq:
            output_f.write(seq + "\n") #writes sequence

input = sys.argv[1]
output = sys.argv[2]
convertsequential(input, output)
