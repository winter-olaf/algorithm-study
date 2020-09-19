n = int(input())
if n in [1,3]:
    result = -1
elif (n%5)%2==0:
    result = n//5 + (n%5)//2
else:
    result = ((n//5)-1) + ((n%5+5)//2)
print(result)
# 5로 나누어지지 않는 경우 : 1,2,3,4이다. 그런데 1,3의 경우는 2로도 나눌 수가 없으니 거슬러 줄 수 없는 돈이다! 따라서 -1을 출력한다.

# 5 이상의 숫자는 모두 거슬러 줄 수 있다. 홀수라면 5로 나누었을 때 나머지가 짝수가 되고, 짝수라면 당연히 거슬러 줄 수 있기 때문이다.

# 즉, 5원보다 적고 2의 배수가 아닌 경우만 -1을 출력해 주면 된다.

# 8원을 예로 들면, 5원으로 나누었을 때 몫이 1이고 나머지가 3이다. 따라서 2로 나누었을 때 나머지가 0이 아니므로, 5원이 거스름돈에 포함되지 못한다는 것을 알 수 있다. 따라서 이런 경우에는 5원의 개수를 1개 빼주고, 입력받은 값을 5로 나눈 나머지에 5를 하나 더한 뒤 그것을 2로 나눈 몫을 구하면 된다.

# 13원을 예로 들어 보자. 5원 두개를 쓰면 못나눈다! 그래서 우선 5원 두개로 나누면 몫2, 나머지 3에서 => 몫1, 나머지 3+5 = 8로 한 뒤 2로 나누어 5원 1개, 2원 4개를 쓰면 된다는 결과를 알 수 있다.