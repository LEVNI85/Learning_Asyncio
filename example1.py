#Awaitable Tasks without benefits of Asynchronous programming

import asyncio
import time

async def func(x):
    print(f"Do with {x}")
    await asyncio.sleep(x)
    print(f"Done with {x}")

    return x

async def main():
    res1 = await func(1)
    print("Func 1 completed!")

    res2 = await func(2)
    print("Func 2 completed!")

    return [res1, res2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")
