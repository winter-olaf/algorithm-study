age = 220 - int(input())
heartbeat, result = [], [0]*6
while True:
	if input() != "":
		heartbeat.append(int(input()))
	else:
		break
for i in heartbeat:
	print(i/age)
	if (i/age)*100 < 60:
		result[0]+=1
	elif (i/age)*100 >= 60 and (i/age)*100 < 68:
		result[1]+=1
	elif (i/age)*100 >= 68 and (i/age)*100 < 75:
		result[2]+=1
	elif (i/age)*100 >= 75 and (i/age)*100 < 80:
		result[3]+=1
	elif (i/age)*100 >= 80 and (i/age)*100 < 90:
		result[4]+=1
	else:
		result[5]+=1
result = result[::-1]
for i in range(len(result)):
	if i == 5:
		print(result[i])
	else:
		print(i, end=' ')