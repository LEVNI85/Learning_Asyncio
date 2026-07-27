#Awaitable Tasks introduced

import asyncio
import time

async def func(x):
    print(f"Do with {x}")
    await asyncio.sleep(x)
    print(f"Done with {x}")

    return x

async def main():
    tsk1 = asyncio.create_task(func(1))
    tsk2 = asyncio.create_task(func(2))

    res1 = await tsk1
    print("Func 1 completed!")

    res2 = await tsk2
    print("Func 2 completed!")

    return [res1, res2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")
