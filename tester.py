import math
def main():
    myMessage= 'teetabhsitrrissodesanotamgohok'
    myKey = 5
    plaintext = decryptMessage(myKey, myMessage)
   
    print("The plain text is")
    print(plaintext)


def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    print(len(plaintext))
    for symbol in message:
       plaintext[col] += symbol
       print(plaintext[col],col)
       col += 1
       if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
         col = 0 
         row += 1 
     
    return ''.join(plaintext)

# if __name__ == '__main__':
#    main()

# def decrypt(message, keyword):
#   matrix = createDecrMatrix(getKeywordSequence(keyword), message)

#   plaintext = ""
#   for r in range(len(matrix)):
#     for c in range (len(matrix[r])):
#       plaintext += matrix[r][c]
#   return plaintext


# def createDecrMatrix(keywordSequence, message):
#   width = len(keywordSequence)
#   height = len(message) / width
#   if height * width < len(message):
#     height += 1

#   matrix = createEmptyMatrix(width, height, len(message))

#   pos = 0
#   for num in range(len(keywordSequence)):
#     column = keywordSequence.index(num+1)

#     r = 0
#     while (r < len(matrix)) and (len(matrix[r]) > column):
#       matrix[r][column] = message[pos]
#       r += 1
#       pos += 1

#   return matrix


# def createEmptyMatrix(width, height, length):
#   matrix = []
#   totalAdded = 0
#   for r in range(height):
#     matrix.append([])
#     for c in range(width):
#       if totalAdded >= length:
#         return matrix
#       matrix[r].append('')
#       totalAdded += 1
#   return matrix


# def getKeywordSequence(keyword):
#   sequence = []
#   for pos, ch in enumerate(keyword):
#     previousLetters = keyword[:pos]
#     newNumber = 1
#     for previousPos, previousCh in enumerate(previousLetters):
#       if previousCh > ch:
#         sequence[previousPos] += 1
#       else:
#         newNumber += 1
#     sequence.append(newNumber)
#   return sequence 