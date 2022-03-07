# Mohamed Yasser Anwar Mahmoud AlKayd
# Nucleotide Composition Program

# - Start of the Program -

sequence = input("Enter DNA sequence: ")
 
allowed=['A','C','G','T'] #What is allowed
#not_allowed= all not in ['A','C','G','T']

V1=sequence.count('A')
V2=sequence.count('C')
V3=sequence.count('G')
V4=sequence.count('T') #Count the number of times each letter appears

for i in sequence:
    if i in allowed:
        print(V1,V2,V3,V4) #If it is in allowed, numbers will be written for each letter
        break
    if i not in allowed: #if not allowed, invalid will be written
        print("Invalid")
        break
    
# - End of the Program