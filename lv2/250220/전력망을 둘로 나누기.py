def solution(n, wires):
    min = 100
    num = 0
    for i in range(len(wires)):
        array = wires[:]
        disconnect = array.pop(i)
        if seperateWires(disconnect, array) < min:
            min = seperateWires(disconnect, array)
    return min

def seperateWires(disconnect, wires):
    wire_1 = [str(disconnect[0])]
    wire_2 = [str(disconnect[1])]
    array = wires[:]
    while array != []:
        wire = array.pop(0)
        if str(wire[0]) in wire_1:
            wire_1.append(str(wire[0]))
            wire_1.append(str(wire[1]))
        elif str(wire[1]) in wire_1:
            wire_1.append(str(wire[1]))
            wire_1.append(str(wire[0]))
        elif str(wire[1]) not in wire_2 and str(wire[0]) not in wire_2:
            array.append(wire)
            continue
        else:
            wire_2.append(str(wire[0]))
            wire_2.append(str(wire[1]))
    wire_1 = list(set(wire_1))
    wire_2 = list(set(wire_2))
    
    return abs(len(wire_1) - len(wire_2))

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))