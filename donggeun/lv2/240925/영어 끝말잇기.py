def solution(n, words):
    word_set= set(words)
    word_dic= {_:0 for _ in word_set}
    word_dic[words[0]]+=1

    for i in range(1, len(words)):
        if(word_dic[words[i]]!=0 or words[i-1][-1]!=words[i][0]):
            return [(i%n)+1, (i//n)+1]
        else:
            word_dic[words[i]]+=1
    return [0, 0]

## main ##
n= 5
words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))
