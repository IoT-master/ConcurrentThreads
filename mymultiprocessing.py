import os
import time
from multiprocessing import Process, current_process

def square(number):
    result = number ** 2
    process_name = current_process().name
    print(f"Process Name: {process_name} and Process ID: {os.getpid()}")
    print(f"{number} squared is {result}")

if __name__=="__main__":
    start = time.perf_counter()
    processes = []
    numbers = range(100)

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    finish = time.perf_counter()
    print(f"Time of Execution took {round(finish-start, 2)} second(s)")