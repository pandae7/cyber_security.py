import math
import numpy as np
def main():
    myMessage= 'meanrradsklcakhs'
    myKey = 4
    A = decryptMessage(myKey, myMessage)
   
    # print("The plain text is")
    print(A)


def decryptMessage(key, message):
    numOfRows = math.ceil(len(message) / key)
    numOfColumns = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # plaintext = [''] * numOfColumns
    col = 0
    row = 0
    A = np.zeros([numOfRows,numOfColumns],dtype=int)
    # A = []
    # for x in enumerate(message)
    #     A.append(ord(x))
    
    diagonal = 0
    column = 0
    for x in message:
       A[row][col] = ord(x)
       row -= 1
       col += 1
       if (row == -1) or (col >= numOfColumns) :
           diagonal += 1
           row = diagonal
           col = 0
           if (diagonal == numOfRows):
               diagonal -=1
               row = diagonal
               column += 1
               col = column
               if (row == numOfRows - 1 and col >= numOfColumns - numOfShadedBoxes):
                   row -= 1
                   col += 1
    plaintext = ''

    for x in range(numOfRows):
        for y in range(numOfColumns):
            plaintext = plaintext + chr(A[x][y])
    
    
    return plaintext.strip()



              
             

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