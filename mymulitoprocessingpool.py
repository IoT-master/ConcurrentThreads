import time
from multiprocessing import Pool
import os
def sum_square(number):
    s = 0
    for i in range(number):
        s += i**2
    return s
if __name__=='__main__':
    print(os.cpu_count())
    numbers = range(5)
    p = Pool()
    result = p.map(sum_square, numbers)
    print(result)
    p.close()
    p.join()