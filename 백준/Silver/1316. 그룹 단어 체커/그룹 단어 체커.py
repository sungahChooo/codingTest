#단어 개수 입력받음
N=int(input())

#단어 안에 알파벳이 나오고 다른 알파벳이 나오고 그 다음에 또 나오면 안됨
count=0
words=[]
for i in range(N):
    word=input()
    words.append(word)

# print(words)
count=N
seen_letters=[]
for _ in words:
    seen_letters=[]
    for i in range(len(_)-1):
        seen_letters.append(_[i])
        if _[i]!=_[i+1] and _[i+1] in seen_letters:
            count-=1
            break
        else:
            continue
print(count)
