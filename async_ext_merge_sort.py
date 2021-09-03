import asyncio
import time
import os


async def sort(arr):
    await merge_sort(arr)


async def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        await merge_sort(L)
        await merge_sort(R)
        await merge(arr, L, R)


async def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


async def read_file_sort(filename, combined_list):
    # print(filename + " start!")
    # await asyncio.sleep(1)
    f = open("input/" + filename, "r")
    num_list = [int(line) for line in f.readlines()]
    await sort(num_list)
    combined_list += num_list
    f.close()
    # print(filename + " end!")


async def main():
    root_path = os.getcwd()
    file_path = root_path + '/input'
    combined_list = []
    jobs = []
    for filename in os.listdir(file_path):
        job = asyncio.create_task(read_file_sort(filename, combined_list))
        jobs.append(job)
    await asyncio.gather(*jobs)
    await sort(combined_list)
    out_file = open("output/async_out_file.txt", "w")
    for i in combined_list:
        out_file.write(str(i) + '\n')
    out_file.close()


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
