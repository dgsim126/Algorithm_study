from collections import deque

def solution(order):
    main_queue = deque()
    sub_stack = []
    index = 0

    for i in range(1, len(order)+1):
        main_queue.append(i)


    while(len(main_queue)!=0 or len(sub_stack)!=0):
        if(len(main_queue)!=0 and main_queue[0] == order[index]):
            main_queue.popleft()
            index+= 1
        elif(len(sub_stack)!=0 and sub_stack[-1] == order[index]):
            sub_stack.pop()
            index += 1
        elif(len(main_queue)!=0):
            sub_stack.append(main_queue.popleft())
        else:
            break

    return index


## main ##
order= [4, 3, 1, 2, 5]
print(solution(order))