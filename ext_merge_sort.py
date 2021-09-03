import time
import os
import asyncio


def sort(arr):
    merge_sort(arr)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr, L, R)


def merge(arr, L, R):
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


def read_file_sort(filename, combined_list):
    # print(filename + " start!")
    # time.sleep(1)
    f = open("input/" + filename, "r")
    num_list = [int(line) for line in f.readlines()]
    sort(num_list)
    combined_list += num_list
    f.close()
    # print(filename + " end!")


def main():
    root_path = os.getcwd()
    file_path = root_path + '\input'
    combined_list = []
    for filename in os.listdir(file_path):
        read_file_sort(filename, combined_list)
    sort(combined_list)
    out_file = open("output/async_out_file.txt", "w")
    for i in combined_list:
        out_file.write(str(i) + '\n')
    out_file.close()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)
