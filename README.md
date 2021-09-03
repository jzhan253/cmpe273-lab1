# Lab 1
Use any kind of [External Sorting](https://en.wikipedia.org/wiki/External_sorting) algorithm to sort all numbers from input/unsorted_*.txt files and save the sorted result into output/sorted.txt file amd async_sorted.txt file.
# Analysis
with modern cpu's computing power, sorting lists and write the result to files takes very little time. Thus, the asynchronous concurrent tasks performance advantages brought by asyncio was not very obivous while comparing it with synchronous computing. With or without async, both sorting/writing tasks were done within 0.1 seconds, and the synchronous version was evern a little faster. My guess was because of using async api cause some little extra time. 
To present the advantages brought by the asyncio, I inserted "time.sleep(1)" and "await asyncio.sleep(1)" into the synchronous and asynchronous function to increase the computing time. And synchronous method takes over 10 seconds(1 second after 1 second) to finish the job, however, asynchronous method takes only about 1 second(10 1-second jobs works concurrently) to finish the job.  



# Requirements

Implement your solution with or without [Asyncio](https://docs.python.org/3/library/asyncio.html).

* ext_merge_sort.py
* async_ext_merge_sort.py (uses Asyncio)

Finally, measure each execution time via

```sh
time python3 ext_merge_sort.py
time python3 async_ext_merge_sort.py
```

Save the output of each run in time.txt and async_time.txt.

Commit your changes into your public Github repository (cmpe273-lab1) and your final commit should have:

1. ext_merge_sort.py
2. async_ext_merge_sort.py
3. all unsorted_*.txt files
4. all sorted_.txt files
4. time.txt and async_time.txt



