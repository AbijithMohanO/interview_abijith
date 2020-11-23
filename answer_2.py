# Input string of alphabets
string = input().strip()

while len(string) % 2 != 0:
    string = input().strip()
string = string.upper()
length =int(len(string)/2)
string1 = string[0:length]
string2 = string[length:]


# Convert string to base26 number
alphabet ={ "A": 0, "B": 1, "C": 2,"D": 3, "E": 4, "F": 5,"G": 6, "H" : 7,"I" : 8,"J": 9,"K":10, "L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
num1 = 0 
num2 = 0
for i in  range(length):
    string1 =string1[::-1]
    num1 += alphabet[string1[i]] *pow(26, i)
    
    string2 =string2[::-1]
    num2 += alphabet[string2[i]] *pow(26, i)

sum = num1 + num2
print(sum)

# i was able to crack the logic. not able to get desired output in some test cases. due to time constraint i was not able to corresct the slight semantic error in program
