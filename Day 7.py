inpputFile = open("input/input_day7", "r")

def isABBA(string):
    for i in range(len(string)-3):
        if string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]:
            return True
    return False

def isABA(string):
    list = []
    for i in range(len(string)-2):
        if string[i] == string[i+2] and string[i] != string[i+1]:
            list.append(string[i:i+3])
    return list

def supportsTLS(line):
    for i in range(len(line)):
        if line[i][0] == "[" and isABBA(line[i]):
            return False

    for i in range(len(line)):
        if line[i][0] != "[" and isABBA(line[i]):
            return True

def supportsSSL(line):
    aba = []
    bab = []

    for i in range(len(line)):
        if line[i][0] == "[" and isABA(line[i]) != []:
            bab += isABA(line[i])
        elif line[i][0] != "[" and isABA(line[i]) != []:
            aba += isABA(line[i])

numTLS = 0
numSSL = 0

for line in inpputFile:
    line = line.replace("[", " [").replace("]", "] ").split()

    if supportsTLS(line):
        numTLS += 1

    if supportsSSL(line):
        numSSL += 1

print(numSSL)

inpputFile.close()
