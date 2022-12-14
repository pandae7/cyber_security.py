import mmap
def main():
    sentence = "lol ahsbcj might"
    # print(sentence.lower())
    print(PercentMatch(sentence.lower()))

# def Verify(word):
#     flag = 0
#     with open("dict","r") as d:
#         b = word.encode() #check percentage of matching words in a dictionary python
#         s = mmap.mmap(d.fileno(), 0, access=mmap.ACCESS_READ)
#         if s.find(b) != -1:
#             flag = 1
#     return flag

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
    print(len(A))
    word_match = 0
    for word in A:
        print(Verify(word))
        word_match += Verify(word)
    return int(word_match/len(A) * 100)


# if __name__ == '__main__':
#    main()