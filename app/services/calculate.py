import asyncio
import time


async def calc_square(number: int, delay: float) -> dict:
    start = time.perf_counter()

    await asyncio.sleep(delay)

    square = number ** 2
    end = time.perf_counter() - start

    return {
        "number": number,
        "square": square,
        "delay": delay,
        "time": round(end, 2)
    }


async def calc_all(numbers: list[int], delays: list[float]) -> dict:
    start = time.perf_counter()

    results = await asyncio.gather(
        *[
            calc_square(number, delay)
            for number, delay in zip(numbers, delays)
        ]
    )

    end = time.perf_counter() - start
    sequential_time = sum(delays)

    return {
        "results": results,
        "total_time": round(end, 2),
        "parallel_faster_than_sequential": end < sequential_time,
    }
