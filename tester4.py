import math
import numpy as np
def main():
    myMessage = 'uhnoycgirrsyafppt'
    # myMessage = 'anledkmrcashrak'
    myKey = 5
    A = decryptMessage(myKey, myMessage)
   
    # print("The plain text is")
    print(A)


def decryptMessage(key, message):
    length = len(message)
    numOfRows = math.ceil(len(message) / key)
    numOfColumns = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # plaintext = [''] * numOfColumns
    A = np.zeros([numOfRows,numOfColumns],dtype=int)
    col = 0
    row = numOfRows - 1
    diagonal = numOfRows - 1
    column = 0
    A[0][numOfColumns-1] = ord(message[length-1:])
    for x in message[:-1]: 
       A[row][col] = ord(x)
       row += 1
       col += 1
       if (row > numOfRows - 1):
            diagonal -= 1
            row = diagonal
            col = 0
            if (diagonal == -1):
                    row = 0
                    column += 1
                    col = column
       if (row > numOfRows-1 and col >= numOfColumns - numOfShadedBoxes):
            row = 0
            if (column == 0):
                column += 1   
                col = column
            else:
                col = column
                column += 1
       print(row,col,diagonal,column)

    return A

    # plaintext = ''
    # for x in range(numOfRows):
    #     for y in range(numOfColumns):
    #         plaintext = plaintext + chr(A[x][y])
    # return plaintext.strip()
    
    

if __name__ == '__main__':
   main()
