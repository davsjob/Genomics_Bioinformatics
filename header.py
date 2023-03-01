import sys
def findseq(infile, genename):
     #Opens file and reads it
    head = ">"+genename +" \n" 
    with open(infile, 'r') as input_f:
        #Creates desired output for header
        
        seq = input_f.readlines()
        for i, line in enumerate(seq):
            if line.startswith('>'):
                seq.pop(i)
    seq.insert(0,head)

    with open(infile, 'w') as input_w:
        #Writes it to output file
        seq = "".join(seq)
        
        input_w.write(seq)

#Takes input from commandline       
findseq(sys.argv[1], sys.argv[2])
