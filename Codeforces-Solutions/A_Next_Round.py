def ans():
    a,b= map(int, input().split())
    score=list(map(int,input().split()))

    cut=score[b-1]
    count=0
    for i in score:
        if i>=cut and i>0:
            count+=1



ans()
