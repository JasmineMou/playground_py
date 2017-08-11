from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import math
import time

### Functions ###
def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n // p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# manual chunk
def chunked_worker(nums,func):
    """ Factorize a list of numbers, returning a num:factors mapping.
    """
    return {n: func(n) for n in nums}

def process_pool_chunked(nums, nprocs, func):
    # Manually divide the task to chunks of equal length, submitting each chunk to the pool.

    chunksize = int(math.ceil(len(nums) / float(nprocs)))
    futures = []

    with ProcessPoolExecutor() as executor:
        for i in range(nprocs):
            chunk = nums[(chunksize * i) : (chunksize * (i + 1))]
            futures.append(executor.submit(chunked_worker, chunk, func))

    resultdict = {}
    for f in as_completed(futures):
        resultdict.update(f.result())
    return resultdict

def thread_pool_chunked(nums, nthreads, func):
    chunksize = int(math.ceil(len(nums) / float(nthreads)))
    futures = []

    with ThreadPoolExecutor(max_workers=nthreads) as executor:
        for i in range(nthreads):
            chunk = nums[(chunksize * i) : (chunksize * (i + 1))]
            futures.append(executor.submit(chunked_worker, chunk, func))
	
	resultdict = {}
    for f in as_completed(futures):
        resultdict.update(f.result())
    return resultdict


# auto chunk
def process_pool_mapped(nums, nprocs, func):
    # Let the executor divide the work among processes by using 'map'.
    with ProcessPoolExecutor(max_workers=nprocs) as executor:
        return {num:factors for num, factors in zip(nums, executor.map(func, nums))}

def thread_pool_mapped(nums, nthreads, func):
	with ThreadPoolExecutor(max_workers=nthreads) as executor:
		return {num:factors for num, factors in zip(nums, executor.map(func, nums))}


### Tests ###
# nums = range(1,101)
nums = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]
n = 30
# func = factorize_naive
func = is_prime

# without the concurrent, baseline
start_time = time.time()
a = chunked_worker(nums, func)
interval = time.time() - start_time

# with the concurrent
start_time2 = time.time()
a2 = process_pool_chunked(nums,n,func)
interval2 = time.time() - start_time2

start_time3 = time.time()
a3 = process_pool_mapped(nums,n,func)
interval3 = time.time() - start_time3

start_time4 = time.time()
a4 = thread_pool_chunked(nums, n, func)
interval4 = time.time() - start_time4

start_time5 = time.time()
a5 = thread_pool_mapped(nums, n, func)
interval5 = time.time() - start_time5


### Results ### 
assert(cmp(a,a2)==0 & cmp(a,a3)==0)
# print(a,a2,a3)
print(interval, interval2, interval3)
print(interval2<interval or interval3 < interval) 

## nums = range(1,100), n = 5, func = factorize_naive,
## original is the best & map outperforms chunked
## int < int3 < int2 
## (0.00019621849060058594, 0.06235384941101074, 0.05350804328918457)

## nums = range(1,1000), n = 5, func = factorize_naive,
## original is the best & chunk outperforms map
## int < int2 < int3
## (0.003192901611328125, 0.06420302391052246, 0.4476139545440674)

## nums = [primes_or_not], n = 100, func = is_prime,
## (result is not stable)
## map is the best & chunk outperforms orginal
## int3 < int2 < int
## (4.9344987869262695, 4.889400005340576, 4.70719313621521)
## original is the best & chunk outperforms map
## int < int2 < int3
## (4.798500061035156, 5.343875885009766, 5.465551137924194)

## nums = [primes_or_not], n = 5, func = is_prime,
## chunk is the best & map outperforms original
## int2 < int3 < int
## (4.905217885971069, 3.8706088066101074, 4.4592859745025635)

assert(cmp(a2,a4)==0 & cmp(a3,a5)==0)
print(interval2, interval4)
print(interval3, interval5)

## nums = [primes_or_not], n = 100, func = is_prime,
## 
## int3 < int5
## (5.128652095794678, 8.400548219680786)









