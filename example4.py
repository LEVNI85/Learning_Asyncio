#Gather and TaskGroups to run several tasks/coroutines together as a group

import asyncio
import time

async def func(x):
    await asyncio.sleep(x)
    return x

async def main():
    tsk1 = asyncio.create_task(func(1))
    tsk2 = asyncio.create_task(func(2))
    res1 = await tsk1
    res2 = await tsk2
    print(f"Task1 and Task2 done: {[res1, res2]}")

    coroutines = [func(i) for i in range(1,3)]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(f"Coroutine gather done: {results}")

    tasks = [asyncio.create_task(func(i)) for i in range(1,3)]
    results1 = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Tasks gather Done: {results1}")

    async with asyncio.TaskGroup() as tg:
        results3 = [tg.create_task(func(i)) for i in range(1,3)]

    print(f"Tas Group done: {[i.result() for i in results3]}")


if __name__ == "__main__":
    t1 = time.perf_counter()

    result = asyncio.run(main())
    print(result)

    t2 = time.perf_counter()

    print(f"Finished in {t2-t1:.2f} seconds")