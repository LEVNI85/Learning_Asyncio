#simple example of synchronous code
import time

def func(x):
    print(f"Do with {x}")
    time.sleep(x)
    print(f"Done with {x}")

    return x

def main():
    res1 = func(1)
    print("Func 1 completed!")

    res2 = func(2)
    print("Func 2 completed!")

    return [res1, res2]


t1 = time.perf_counter()

results = main()
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")
