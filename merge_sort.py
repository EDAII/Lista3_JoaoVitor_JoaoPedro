import random
import math
import timeit
import matplotlib.pyplot as plt

def mergeSort(array):
	if len(array) > 1:
		half = len(array) // 2
		lArray = array[:half]
		rArray = array[half:]

		mergeSort(lArray)
		mergeSort(rArray)

		lMark, rMark, position = 0, 0, 0

		while lMark < len(lArray) and rMark < len(rArray):
			if lArray[lMark] < rArray[rMark]:
				array[position] = lArray[lMark]
				lMark += 1
			else:
				array[position] = rArray[rMark]
				rMark += 1
			position += 1

		while lMark < len(lArray):
			array[position] = lArray[lMark]
			lMark += 1
			position += 1
		while rMark < len(rArray):
			array[position] = rArray[rMark]
			rMark += 1
			position += 1
