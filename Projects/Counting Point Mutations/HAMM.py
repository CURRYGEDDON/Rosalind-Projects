
# HAMM function compares each letter between two DNA Strings,
# if a letter does not match between strings, then there is a mutation
def HAMM():
    inputFile = input("Please enter a .txt file:")
    DNA_String = open(inputFile)
    #first line in file is DNA_String1 and second line in file is DNA string 2
    DNA_String1 = DNA_String.readline()
    DNA_String2 = DNA_String.readline()
    DNA_String1 = list(DNA_String1)
    DNA_String2 = list(DNA_String2)
    length_DNA1 = len(DNA_String1)
    length_DNA2 = len(DNA_String2)
    minimum = min(length_DNA1, length_DNA2)
    maximum = max(length_DNA1, length_DNA2)
    mutations = 0

# compares each letter between the strings, if the letters don't match mutations is increased by 1
    for i in range(minimum):
        if DNA_String1[i] != DNA_String2[i]:
            mutations += 1
# if one DNA String is bigger than another, will add any excess letter to mutation number
    mutations = mutations + (maximum - minimum)
    print(mutations
    
    
    """
    sample input:
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    
    sample output:
    7
    
   """
