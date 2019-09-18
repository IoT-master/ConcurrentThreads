import asyncio
import random
import time

start = time.perf_counter()

async def myCoroutine(id):
    process_time = random.randint(1,5)
    await asyncio.sleep(process_time)
    print(f"Corountine: {id} has successfully completed after {process_time} second(s)")

async def main():
    task = []
    for i in range(10):
        task.append(asyncio.ensure_future(myCoroutine(i)))

    await asyncio.gather(*task)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

finish = time.perf_counter()
print(f"Tasks Completed in {round(finish-start, 2)} second(s)")