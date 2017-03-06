# DNA function counts and prints out number of nucleotides (A,C,G,T) in a DNA String

# ie for input "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#output 20 12 17 21

def DNA():
    inputFile = input("Please enter a .txt file:")
    DNA_String = open(inputFile)
    DNA_String = DNA_String.read()
    DNA_String = DNA_String.upper()
    num_A = 0
    num_C = 0
    num_G = 0
    num_T = 0
    #counts number of each letter in the string
    for char in DNA_String:
        if char == "A":
            num_A += 1
        elif char == "C":
            num_C += 1
        elif char == "G":
            num_G += 1
        elif char == "T":
            num_T += 1
    print(num_A, num_C, num_G, num_T)
