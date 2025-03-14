# gpt
import numpy

def solution(arr1, arr2):
    result = numpy.array(arr1) @ numpy.array(arr2)
    return result.tolist()