T = int(input())
rev_num = 0

while(T>0):
    N = int(input())
    while(N>0):
        rev_num = (rev_num*10)+(N%10)
        N = N//10
    print(rev_num)
    rev_num=0
    T -= 1