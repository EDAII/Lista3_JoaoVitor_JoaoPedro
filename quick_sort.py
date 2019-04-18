<<<<<<< HEAD
def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    quick_sort([])
    []

    quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


if __name__ == '__main__':

    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( quick_sort(unsorted) )
=======
import random

class Quick(object):
    def particao(self, a, ini, fim):
        pivo = a[fim-1]
        start = ini
        end = ini
        for i in range(ini,fim):
            if a[i] > pivo:
                end += 1
            else:
                end += 1       
                start += 1
                aux = a[start-1]
                a[start-1] = a[i]
                a[i] = aux
        return start-1
        
    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.randparticao(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp+1,fim)
        return a
        
    def randparticao(self,a,ini,fim):
        rand = random.randrange(ini,fim)
        aux = a[fim-1]
        a[fim-1] = a[rand]
        a[rand] = aux
        return self.particao(a,ini,fim)
>>>>>>> 05fcb665c387e4798adc2642b72b8590c5ea626f
