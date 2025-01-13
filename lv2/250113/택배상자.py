def solution(order):
    container = [i+1 for i in range(len(order))]
    sub_container = []
    order = order

    result = 0

    while order:
        if order[0] == container[0]:
            order.pop(0)
            container.pop(0)
            result += 1
        elif sub_container and order[0] == sub_container[-1]:
            sub_container.pop(-1)
            order.pop(0)
            result += 1
        elif sub_container and order[0] != container[0] and order[0] != sub_container[-1]:
            sub_container.append(container.pop(0))
        elif container == [] and order[0] != sub_container[-1]:
            break
        elif container == [] and order[0] == sub_container[-1]:
            sub_container.pop(-1)
            order.pop(0)
            result += 1
            
    return result


print(solution([4, 3, 1, 2, 5]))