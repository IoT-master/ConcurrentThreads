import time
import concurrent.futures
import requests

start = time.perf_counter()

def run_me(seconds):
    print(f'Thread for {seconds} second(s) started')
    time.sleep(seconds)
    print(f'Thread stopped after {seconds} second(s)')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_me, [1,2,3,4])

finish = time.perf_counter()

print(f'Script took {round(finish-start,2)} second(s) to execute')