def solution(bridge_length, weight, truck_weights):
    time = 0
    roading_truck = [0 for i in range(bridge_length)]
    while(True):
        if truck_weights == []:
            break
        if sum(roading_truck) + truck_weights[0] <= weight :
            roading_truck.append(truck_weights[0])
            del truck_weights[0]
            roading_truck.pop(0)
            time += 1

        else:
            if roading_truck[0] != 0 and sum(roading_truck[1:]) + truck_weights[0] <= weight:
                roading_truck.pop(0)
                roading_truck.append(truck_weights[0])
                del truck_weights[0]
            else:
                roading_truck.pop(0)
                roading_truck.append(0)
            time += 1
    answer = time + bridge_length

    return answer

print(solution(	2, 10, [7, 4, 5, 6]))