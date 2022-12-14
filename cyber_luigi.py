import luigi
import mmap
import wordninja
import math
import os
import numpy as np
import pandas as pd
from string import ascii_lowercase as lc, ascii_uppercase as uc

if not os.path.exists("decryptions"):
    os.makedirs("decryptions")



def rot_encode(n):
    reference = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(reference)

def rot_decode(n):
    return rot_encode(-n)

def Modrot_decode(alphabet,n):
    # uc = alphabet.upper()
    nc = alphabet
    reference = str.maketrans(nc[n:] + nc[:n],lc)
    return lambda s: s.translate(reference)

# def Modrot_decode(alphabet,n):
#     return Modrot_encode(alphabet,-n)

def Verify(word):
    flag = 0
    with open("dict","r") as d:
        words = d.readlines()
        # print(words)
        if word in [x.strip() for x in words]:
            flag = 1
    return flag

def PercentMatch(Sentence):
    A = Sentence.strip().split()
    word_match = 0
    for word in A:
        word_match += Verify(word)
    return int(word_match/len(A) * 100)


def ColumnTransposition(fileobject,encrypted_code):
    length = len(encrypted_code.strip())
    for x in range(2,int(length/2)):
        # res = ';'.join(test_str[i:i + int(length/x)] for i in range(0, len(test_str), int(length/x)))
        Columns = math.ceil(len(encrypted_code) / x)
        Rows = x
        TotalGridBoxes = (Columns * Rows) - len(encrypted_code)
        plaintext = [''] * Columns
        col = 0
        row = 0
        for symbol in encrypted_code:
            plaintext[col] += symbol
            col += 1
            if (col == Columns) or (col == Columns - 1 and row >= Rows - TotalGridBoxes):
                col = 0 
                row += 1 
            message = ''.join(plaintext)
        sentence = ' '.join(wordninja.split(message.upper()))
        fileobject.writelines([sentence,",",str(x),",",str(PercentMatch(sentence.lower())),",","T",",","\t"])
        fileobject.write("\n")

def ReverseDiagonalTransposition(key,encrypted_code):
    numOfRows = math.ceil(len(encrypted_code) / key)
    numOfColumns = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(encrypted_code)
    # plaintext = [''] * numOfColumns
    col = 0
    row = 0
    A = np.zeros([numOfRows,numOfColumns],dtype=int)
    # A = []
    # for x in enumerate(message)
    #     A.append(ord(x))
    
    diagonal = 0
    column = 0
    for x in encrypted_code:
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


# class ModRot(luigi.Task):
#     def run(self):
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#         with open('TechnicalWords.txt','r') as t:
#             lines = t.readlines()
#         with open('ModRot_alphabets.txt','a+') as a:
#             for line in lines:
#                 line = line.strip() + alphabet
#                 line = "".join(dict.fromxs(line))
#                 a.write(line)
#                 a.write("\n")
#         a.close()
#         t.close()
#     def output(self):
#         return luigi.Localtarget('ModRot_alphabets.txt')




class DecryptCode(luigi.Task):
    encrypted_code = luigi.Parameter()
    line_no = luigi.Parameter()

    # def requires(self):
    #     return ModRot
    
    def run(self):
        with open('decryptions/'+'LineNo_'+str(self.line_no)+'.txt', 'a+') as file1:
            length_of_encryption = len(self.encrypted_code)
            for x in range(1,26):
                sentence = rot_decode(x)(self.encrypted_code)
                sentence = ' '.join(wordninja.split(sentence.upper()))
                file1.writelines([sentence,",",str(x),",",str(PercentMatch(sentence.lower())),",","C",",","\t"])
                file1.write("\n")
            with open('TechnicalWords.txt','r') as helper:
                help = helper.readlines()
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                for line in help:
                    Modified_alphabet = line.strip() + alphabet
                    Modified_alphabet = "".join(dict.fromkeys(Modified_alphabet))
                    for i in [x for x in range(-13,14) if x != 0]:
                        sentence = Modrot_decode(Modified_alphabet,i)(self.encrypted_code)
                        sentence = ' '.join(wordninja.split(sentence.upper()))
                        file1.writelines([sentence,",",str(i),",",str(PercentMatch(sentence.lower())),",","M",",",line.strip()]) 
                        file1.write("\n")
            helper.close()
            ColumnTransposition(file1,self.encrypted_code)  
            for x in range(2,length_of_encryption):
                sentence = ReverseDiagonalTransposition(x,self.encrypted_code)
                sentence = ' '.join(wordninja.split(sentence.upper()))
                file1.writelines([sentence,",",str(-x),",",str(PercentMatch(sentence.lower())),",","D",",","\t"])
                file1.write("\n")

    def output(self):
        return luigi.LocalTarget('decryptions/'+'LineNo_'+str(self.line_no)+'.txt')


class Finalization(luigi.Task):

    encrypted_code = luigi.Parameter()
    line_no = luigi.Parameter()

    def requires(self):
        return DecryptCode(self.encrypted_code, self.line_no)
    
    def run(self):
        with open('decryptions/'+'LineNo_'+str(self.line_no)+'.txt','r') as r:
            k = r.readlines()
            A = [line.strip().split(',') for line in k]
            df = pd.DataFrame(np.matrix(A),columns=['Code','x','PercentMatch','CipherType','ModRot_x'])
            df['PercentMatch'] = df['PercentMatch'].astype(int)
            df1=df[['Code','CipherType','x','ModRot_x']][df.PercentMatch == df['PercentMatch'].max()]
            df1.to_csv('encrypted_code.txt', header=False, index=False, sep=',', mode='a+')

        # with self.output().open('a+') as a:
        #     df1.to_csv('encrypted_code.txt', header=False, index=False, sep=',', mode='a+')

    def output(self):
        return luigi.LocalTarget('taskfinished.txt')            


if __name__ == '__main__':
    luigi.run()