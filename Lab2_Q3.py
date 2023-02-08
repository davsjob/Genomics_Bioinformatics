#Lab2_Q3 David Sjöberg

import sys

def reversecompliment(inputfile, outputfile):

    with open(inputfile, 'r') as input_f, open(outputfile, 'w') as output_f:
        compliments = { "A":"T", "G":"C", "T":"A", "C":"G"} #Dict with complementary values
        seq = ""
        rev = ""
        for line in input_f: #Writes header
            if line.startswith(">"): #Checks if header
                if rev: #writes complementary code and resets
                    output_f.write(rev[::-1] + "\n") 
                    seq = ""
                    rev = ""
                output_f.write(line) #Writes header first
            else:
                seq += line.strip() #Takes away linebreaks
                for i in seq:
                    if i in compliments:
                        rev += compliments[i] #adds complementary base

#Inputs and outputs from commandline
input = sys.argv[1]
output = sys.argv[2]

#Runs it
reversecompliment(input, output)
