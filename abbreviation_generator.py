letterScores = {}
remaining = {}
 
def generateIndex(words):
    wordIndexes = []
    for word in words:
        for i in range(len(word)):
            wordIndexes.append([word[i],i])
    return wordIndexes
 
def readValues():
    with open('values.txt', 'r') as f:
        letter = [line.rstrip().split(' ') for line in f.readlines()]
        for score in letter:
            letterScores[score[0].upper()] = int(score[2]) if score[1]==''  else int(score[1])
 
def splitName(name):
    words = []
    word = ''
    for i in range(len(name)):
        if name[i]=="'":
            i+=1
        elif name[i].isalpha():
            word += name[i]
        else:
            if word:
                words.append(word.upper())
            word = ''
    if word:
        words.append(word.upper())
        return words
 
 
 
def generateAbbreviations(name):
    for name in names:
        words = splitName(name)        
        indexedNames = generateIndex(words)
        for i in range(1,len(indexedNames)-1):
            secondLetterTotal = 0
            thirdLetterTotal = 0
            for j in range(i+1,len(indexedNames)):
                abbreviation = indexedNames[0][0]+indexedNames[i][0]+indexedNames[j][0]            
                if(indexedNames[i][1]==0):
                    secondLetterTotal= 0
                elif i == len(indexedNames) - 1 or (i + 1 < len(indexedNames) and indexedNames[i+1][1] == 0):
                    if indexedNames[i][0] == "E":
                        secondLetterTotal=  20
                    else:
                        secondLetterTotal=  5
                else:  
                    secondLetterTotal=  indexedNames[i][1]+letterScores[indexedNames[i][0]]
                if(indexedNames[j][1]==0):
                    thirdLetterTotal= 0
                elif j == len(indexedNames) - 1 or (j + 1 < len(indexedNames) and indexedNames[j+1][1] == 0):
                    if indexedNames[j][0] == "E":
                        thirdLetterTotal= 20
                    else:
                        thirdLetterTotal= 5
                else:  
                    thirdLetterTotal= indexedNames[j][1]+letterScores[indexedNames[j][0]]
                if abbreviation not in remaining:
                    remaining[abbreviation] =[name, secondLetterTotal+thirdLetterTotal,1]
                elif remaining[abbreviation][1]>=secondLetterTotal+thirdLetterTotal and remaining[abbreviation][0]==name:
                    remaining[abbreviation][1]=secondLetterTotal+thirdLetterTotal
                    remaining[abbreviation][2]+=1
                elif remaining[abbreviation][1]!=secondLetterTotal+thirdLetterTotal and remaining[abbreviation][0]!=name:
                    remaining[abbreviation][2]+=1
   
   
 
def readFile(fileName):
    try:
        with open(fileName, 'r') as file:
            names = [line.rstrip() for line in file.readlines()]
            return names
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
        return []
 
def writeToFile(fileName, names,sorted_items):
    try:
        with open(fileName, 'w') as file:
            for i in names:
                for j in sorted_items:
                    if i==j[1][0]:
                        file.write(f"{i}\n{j[0]}\n")
                        break
    except Exception as e:
        print(f"Error writing to file '{fileName}': {e}")
 
if __name__ == "__main__":
    names = readFile('trees.txt')
    readValues()
    generateAbbreviations(names)
    remaining = {key: value for key, value in remaining.items() if value[2] <= 1}
    sorted_items = sorted(remaining.items(), key=lambda x: x[1][1])
    writeToFile('abbreviations.txt', names, sorted_items)
