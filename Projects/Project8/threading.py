# Title: Project 8 - Using Threading
# Name: Bennett Hamilton
# Date: 11/24/23
# Description: receive multiple ranges of numbers, add numbers in each range together, 
#              print total sums, print sum of the total sums

import threading

def sum_range():
    # function to add up a range of numbers
    
    

def main():
    # runs all threads
    # example input
    ranges = [
        [10, 20],
        [1, 5],
        [70, 80],
        [27, 92],
        [0, 16]
    ]

    num_ranges = len(ranges)
    results = [0] * num_ranges  # empty array to store results
    threads = []                # empty array to append threads to

    # launch threads per each range
    # ref: https://www.geeksforgeeks.org/enumerate-in-python/
    for i, (start, end) in enumerate(ranges):
        thread = threading.Thread(target=sum_range, args=(i, start, end, results))
        threads.append(thread)
        thread.start()

    # close threads once all done
    for thread in threads:
        thread.join()

    # print results
    print(results)
    total_sum = sum(results)
    print(total_sum)

if __name__ == "__main__":
    main()