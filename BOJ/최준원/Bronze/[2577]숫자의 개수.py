<<<<<<< HEAD
# # 런타임 에러
# import numpy as np
# import collections
# import sys
# arr = []
# final = [0]*10
# for x in range(3):
#     arr.append(int(sys.stdin.readline()))

# # numpy 모듈을 사용하여 간단하게 list의 multiply 연산
# result = np.prod(arr)
# # res array에 결과값을 자리별로 분할한 뒤 문자형으로 변환해서 저장
# # numpy를 for문으로 가져올 때 int(result)가 되지 않음. 
# # -> TypeError: 'numpy.int32' object isn't iterable
# res = [x for x in str(result)]
# container = collections.Counter(res)

# # container.items() 함수를 사용해서 final array의 값에 저장
# for k,v in container.items():
#     final[int(k)] += v

# for i in final:
#     print(i)


# prod 연산이 시간을 오래 잡아먹는다고 판단, 간단한 for 문으로 선회
# 예상이 맞는 듯.
import sys
=======
# numpy error in desktop
import numpy as np
>>>>>>> e0e2350eac048f70d5e8268866858e729cedaf5b
import collections
arr = []
final = [0]*10
for x in range(3):
    arr.append(int(sys.stdin.readline()))
result = 1
for i in arr:
    result *= i
res = [x for x in str(result)]
container = collections.Counter(res)
for k, v in container.items():
    final[int(k)] += v
for i in final:
    print(i)