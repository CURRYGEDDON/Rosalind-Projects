# RNA function replaces all occurrences of the letter T in a given DNA string with the letter U
# to create new RNA string

#sample input: GATGGAACTTGACTACGTAAATT
#sample output: GAUGGAACUUGACUACGUAAAUU




def RNA():
    inputFile = input("Please enter a .txt file:")
    DNA_String = open(inputFile)
    DNA_String = DNA_String.read()
    DNA_String = DNA_String.upper()
    DNA_String = list(DNA_String)
    length = len(DNA_String)
    #replace T with U if the character being indexed in the string is a T
    for i in range(length):
        if DNA_String[i] == "T":
            DNA_String[i] = "U"
    # turns the DNA list into a RNA string
    RNA_String = "".join(DNA_String)
    print(RNA_String)
