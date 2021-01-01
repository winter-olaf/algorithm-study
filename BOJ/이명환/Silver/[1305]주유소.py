import sys

N = int(sys.stdin.readline())
distance = list(map(int,(sys.stdin.readline().split())))
oil_price = list(map(int,(sys.stdin.readline().split())))
oil_price.pop()

start = 0
result =0
end = len(oil_price) - 1
k = 0

result += distance[start] * oil_price[start]

while(start<end and start +k+1 <=end):
    if(oil_price[start] < oil_price[start+k+1]):
        result += distance[start+k+1]*oil_price[start]
        k +=1
    else:
        result+= distance[start+k+1]*oil_price[start+k+1]
        start = start + k +1
        k= 0

print(result)