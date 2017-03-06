
#takes in multiple dataset DNA strings and outputs the name of the DataString with the highest GC contents and its respective GC content

def GC():
    nameDNAString = []
    listDNAStrings = []
    DNAStringRespectiveGC = []

    inputFile = input("Please enter a .txt file")
    wholeDNAString = open(inputFile)
    #counts number of lines in the file
    lines_in_file = wholeDNAString.readlines()
    numberOfLines = len(lines_in_file)
    #for each line in the file, figures out if the line is a name of a DNA string or an actual DNA String
    for number in range (numberOfLines):
        current_line=lines_in_file[number]
        #method that sees if a line starts with a ">" character to denote a DNA name
        if current_line.startswith(">"):
            next_line_number=number+1
            DNAString = ""
            current_line=current_line[1:]
            nameDNAString.append((current_line.rstrip("\n")))


            while next_line_number<=(numberOfLines-1) and (lines_in_file[next_line_number]).count(">") ==0:
                #if a DNA strings extends for more than one line will combine DNA strings under the same name as one string
                DNAString+=((lines_in_file[next_line_number]).strip("\n"))
                next_line_number=next_line_number+1
            listDNAStrings.append(DNAString)

    number_DNA_strings=len(listDNAStrings)
    #looks at each DNA string and calculates how many "G"s or "C"s are in the file and then divides that total by the length
    #of the string for the GC content
    for i in range(number_DNA_strings):
        GCCount=0
        current_DNA_String= listDNAStrings[i]
        current_DNA_String=list(current_DNA_String)
        length_DNA_String=len(current_DNA_String)
        for char in range(length_DNA_String):
            if current_DNA_String[char] == "G" or current_DNA_String[char]== "C":
                GCCount += 1
        GCPercent = GCCount / length_DNA_String
        DNAStringRespectiveGC.append(GCPercent)
    #returns the index of the the string with the highest GC content in the GClist
    maximum = DNAStringRespectiveGC.index(max(DNAStringRespectiveGC))
    print(nameDNAString[maximum])
    #uses index to find name of DNA string
    actualPercentage = DNAStringRespectiveGC[maximum] * 100
    print(actualPercentage)
    
    
"""    
sample dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

sample output:
Rosalind_0808
60.919540

"""
