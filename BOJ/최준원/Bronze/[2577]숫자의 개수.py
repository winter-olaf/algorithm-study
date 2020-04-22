import numpy as np
import collections
arr = []
for x in range(3):
    arr.append(int(input()))
# numpy 모듈을 사용하여 간단하게 list의 multiply 연산
result = np.prod(arr)

res = [x for x in str(result)]
container = collections.Counter(res)
for k,v in container.items():
    print(k,v)