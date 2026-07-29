#wrapping synchronous functions into futures objects (making them awaitable)
#and running them in threads(asyncio.to_thread)/processes(ProcessPoolExecutor)

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def func(x):
    print(f"Do with {x}", flush=True)
    time.sleep(x)
    print(f"Done with {x}", flush=True)
    
    return x

async def main():
    tsk1 = asyncio.create_task(asyncio.to_thread(func, 1))
    tsk2 = asyncio.create_task(asyncio.to_thread(func, 2))

    res1 = await tsk1
    print("Func 1 completed!")
    
    res2 = await tsk2
    print("Func 2 completed!")

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as exec:
        tsk1 = loop.run_in_executor(exec, func, 1)
        tsk2 = loop.run_in_executor(exec, func, 2)

        res1 = await tsk1
        print("Process 1 completed!")

        res2 = await tsk2
        print("Process 2 completed!")

    return [res1, res2]


if __name__ == "__main__":
    t1 = time.perf_counter()

    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()

    print(f"Finished in {t2-t1:.2f} seconds")
