# Reverses the given DNA String, then replaces each letter with its complementary letter.
# A/T and G/C are compliments of one another

#sample input:AAAACCCGGT
#sample output:ACCGGGTTTT


def REVC():
    inputFile = input("Please enter a .txt file:")
    DNA_String = open(inputFile)
    DNA_String = DNA_String.read()
    DNA_String = DNA_String.upper()

    # Slicing code that reverses the whole string
    ReverseDNA_String = DNA_String[::-1]
    ReverseDNA_String = list(ReverseDNA_String)
    length = len(ReverseDNA_String)
    #replaces each character in the list with its complimentary letter
    for i in range(length):
        if ReverseDNA_String[i] == "A":
            ReverseDNA_String[i] = "T"
        elif ReverseDNA_String[i] == "C":
            ReverseDNA_String[i] = "G"
        elif ReverseDNA_String[i] == "T":
            ReverseDNA_String[i] = "A"
        elif ReverseDNA_String[i] == "G":
            ReverseDNA_String[i] = "C"
    #turns the list back into a string
    reverseCompliment = "".join(ReverseDNA_String)
    print(reverseCompliment)
