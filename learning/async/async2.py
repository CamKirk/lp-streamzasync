import asyncio
import time
import random

async def count():
    print("uno")
    # await print("tres")
    await asyncio.sleep(random.randint(1,6))
    print("dos")
    await asyncio.sleep(random.randint(1,3))
    print("cuatro")

async def main():
    await asyncio.gather(count(), count(), count())


s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print(f"{__file__} ran in {elapsed} seconds")