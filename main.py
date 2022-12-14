import os
import codecs
import numpy as np
from string import ascii_lowercase as lc, ascii_uppercase as uc
import mmap
import wordninja


with open("input.txt","r") as f:
    lines = f.readlines()

# def rot_alpha(n):
#     reference = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
#     return lambda s: s.translate(reference)

# def Verify(word):
#     with open("dict","r") as d:
#         b = word.encode() #check percentage of matching words in a dictionary python
#         s = mmap.mmap(d.fileno(), 0, access=mmap.ACCESS_READ)
#         if s.find(b) != -1:
#             flag = True
#     return flag

def main(lines):
    A = [line.strip().split() for line in lines]
    # print(np.matrix(A))
    for line_no in range(len(A)):
        encrypted_code = ''.join(A[line_no])
        output = os.popen("python -m luigi --module cyber_luigi Finalization --encrypted-code "+encrypted_code+" --line-no " + str(line_no) + " --local-scheduler").read()

    # print(A[0])
    # for word in A[0]:
    #     print(rot_alpha(13)(word))




f.close()
if __name__ == '__main__':
   main(lines)
