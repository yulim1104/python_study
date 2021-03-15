#1이 될 때까지
n, k = map(int, input().split())
count = 0

while n != 1:
    if n%k == 0 :
        n = n//k
        count += 1
    else :
        n -= 1
        count += 1

print(count)

#숫자 카드 게임
# n,m=map(int,input().split())
# max=0
# for i in range(n):
#     data=list(map(int,input().split()))
#     if(max<min(data)):
#         max=min(data)
#
# print(max)


#큰 수의 법칙
# n,m,k=map(int,input().split()) #n,m,k 입력 받기
# data=list(map(int,input().split())) #data 리스트 입력 받기
#
# data.sort() #data 정렬하기
# answer=(m//(k+1))*(k*data[n-1]+data[n-2])+(m%(k+1))*data[n-1]
#
# print(answer)