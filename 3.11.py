# from typing import List
#
# d/ef bubble_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         print(i)
#         for j in range(len_numbers - 1 -i):
#                 if numbers[j+1] < numbers[j]:
#                     numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#     return numbers
#
#
#
#
#
# if __name__ == '__main__':
#     nums = [1,33,4,55,5,6]
#     print(bubble_sort(nums))
#
#


# from typing import List
#
# def select_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         # print(i)
#         min_idx = i
#         for j in range(i+1, len_numbers):
#             if numbers[min_idx] > numbers[j]:
#                 numbers[min_idx], numbers[j] = numbers[j], numbers[min_idx]
#     return numbers
#
# if __name__ == '__main__':
#     nums = [21,3,34,36]
#     print(select_sort(nums))




#
#
#
# /
#
# # from typing import List
# #
# #
# #
# # def insertion_sort(numbers: List[int]) -> List[int]:
# #     len_numbers = len(numbers)
# #     for i in range(1, len_numbers):
# #         temp = numbers[i]
# #         j = i - 1
# #         while j >= 0 and numbers[j] > temp:
# #             numbers[j+1] = numbers[j]
# #
# #             j -= 1
# #         numbers[j+1] = temp
# #
# #     return numbers
# #
# #
# # if __name__ == '__main__':
# #     nums = [1,4,87,45,9]
# #     print(insertion_sort(nums))
#
#
#
#
#
#
#
# from typing import List
#
#
#
# def insertion_sort(numbers: List[int]) -> List[int]:
#
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp = numbers[i]
#         j = i - 1
#         while j >= 0 and numbers[j] > temp:
#             numbers[j+1] = numbers[j]
#
#             j -= 1
#
#             numbers[j+1] = temp
#
#             print()
#
#
#
# for i in range(1, len_numbers):
#     j = i -1
#
#     temp = number[i]
#
#     j >= 0 and number[j] > temp:
#         number[j+1] = number[j]
#
#         j -= 1
#
#         number[j+1] = temp
#
#
#
#
#
# if __name__ == '__main__':
#     nums = [1,3,4,9,4,4,8]
#     print(insertion_sort(nums))










#
#
#
# from typing import List
#
#
#
# def partition_sort(numbers: List[int], low: int, high: int) -> int:
#     i = low - 1
#     pivot = numbers[high]
#     for j in range(low, high):
#         if number[j] <= pivot:
#             i += 1
#
#             numbers[i], number[j] = number[j], number[i]
#
#
#     numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
#     return i+1
#
#
#
#
#
#
# def quick_sort(numbers: List[int]) -> List[int]:
#     def _quick_sort(numbers: List[int], low: int, high: int) -> None:
#         if low < high:
#             partition_index = partition_sort(numbers, low, high)
#
#             _quick_sort(numbers, low, partition_index-1)
#             _quick_sort(numbers, partition_index+1, high)
#
#     _quick_sort(numbers, 0, len(numbers)-1)
#     return numbers
#
#
#     partition_sort(numbers, low, high)
#
# if __name__ == '__main__':
#
#


#
#
#
# # from typing import List, Iterator, Tuple
# #
# # def find_pair(pairs: List[int, int]) -> Iterator[Tuple[int, int]]:
# #
# #     cache = {}
# #     for pair in pairs:
# #         first, second = pair[0], pair[1]
# #         value = cache.get(second)
# #         if not value:
# #             cache[first] = second
# #
# #         elif value == first:
# #             yield pair
#
# from collections import Counter
#
# # import operator
# # from typing import Tuple
# #
# # def count_chars_v1(strings: str) -> Tuple[str, int]:
# #     strings = strings.lower()
# #     # l = []
# #     # for char in strings:
# #     #     if not char.isspace():
# #     #
# #     #         l.append((char, strings.count(char)))
# #
# #     l = [(c, strings.count(c)) for c in strings if not c.isspace()]
# #
# #     return max(l, key=operator.itemgetter(1))
# #
# #
# # def count_chars_v2(strings: str) -> Tuple[str, int]:
# #     strings = strings.lower()
# #     d = {}
# #     for char in strings:
# #         if not char.isspace():
# #             d[char] = d.get(char, 0) + 1
# #
# #
# # if __name__ == '__main__':
# #     s = 'This is a pen This is a apple '
# #     print(count_chars_v2(s))
#
# import time
#
# from functools import lru_cache
#
#
#
#
# def memoize(f):
#     cache = {}
#     def __wrapper(n):
#         if n not in cache():
#             r = f(n)
#         return r
#     return __wrapper
#
#
#
#
# @memoize
# def test(n):
#     print('test')
#
#
#
# @lru_cache()
# def long_func(num: int) -> int:
#     r = 0
#     for i in range(10000000):
#         r += num * i
#     return r
#
# if __name__ == '__main__':
#     for i in range(10):
#         print(long_func(i))
#
#     start = time.time()
#
#     for i in range(10):
#         print(long_func(i))
#
#     print(time.time() - start)
#
# from collections import Counter
# from typing import List
# def min_count_remove(x: List[int], y: List[int]) -> None:
# #     count_x = {}
# #     count_y = {}
# # for i in x:
# #     count_x[i] = count_x.get(i, 0) + 1
# # for i in y:
# #     count_y[i] = count_y.get(i, 0) + 1
#
#     counter_x = Counter(x)
#     counter_y = Counter(y)
#
#
#     for key_x, value_x in counter_x.items():
#         value_y = counter_y.get(key_x)
#         if value_y:
#             if value_x < value_y:
#                 x[:] = [i for i in x if i != key_x]
#             elif value_x > value_y:
#                 y[:] = [i for i in y if i != key_x]
#
#
#
#
#
# if __name__ == '__main__':
#     x = [1,2,2,2,334,4,4,5]
#     y = [1,2,23,34,14,45,54]
#     min_count_remove(x, y)
#     print(x)
#     print(y)





# l = [1,3,4]
# print([str(i)])

# from typing import List
#
#
#
# def list_to_int(numbers: List[int]) -> int:
#     sum_numbers = 0
#     for i, num in enumerate(reversed(numbers)):
#         sum_numbers += num * (10**i)
#     return sum_numbers
#
# def remove_zero(numbers: List[int]) -> None:
#     if numbers and numbers[0] == 0:
#         numbers.pop(0)
#         remove_zero(numbers)
#
# def list_to_int_plut_one(numbers: List[int]) -> int:
#     i = len(numbers) - 1
#     numbers[i] += 1
#     while 0 < i:
#         if numbers[i] != 10:
#             remove_zero(numbers)
#             break
#         numbers[i] = 0
#         numbers[i-1] += 1
#
#         i -= 1
#     else:
#
#         if numbers[0] == 10:
#             numbers[0] = 1
#             numbers.append(0)
#
#
#     return numbers
#
# if __name__ == '__main__':
#     print(list_to_int_plut_one([8,9,9]))
#

#
# from typing import List
# import operator
#
# def snake_string_v1(chars: str) -> List[List[str]]:
#     result = [[], [], []]
#     result_index = {0, 1, 2}
#     insert_index = 1
#
#     for i, s in enumerate(chars):
#         if i  % 4 == 1:
#             insert_index = 0
#         elif i % 2 == 0:
#             insert_index = 1
#         elif i % 4 == 3:
#             insert_index = 2
#         result[insert_index].append(s)
#         for rest_index in result_index - {insert_index}:
#             result[rest_index].append(' ')
#
#     return result
#
#
#
#
# def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
#     result = [[] for _ in range(depth)]
#     result_indexes = {i for i in range(depth)}
#     insert_index = int(depth / 2)
#
#     op = operator.neg
#
#     # def pos(i):
#     #     return i + 1
#
#     pos = lambda i: i + 1
#
#
#
#     # def neg(i):
#     #     return i - 1
#     neg = lambda i: i - 1
#
#     op = neg
#
#     for s in chars:
#         result[insert_index].append(s)
#         for rest_index in result_indexes - {insert_index}:
#             result[rest_index].append(' ')
#         if insert_index <= 0:
#             op = pos
#         if insert_index >= depth - 1:
#             op = neg
#
#         insert_index = op(insert_index)
#     return result






#
# if __name__ == '__main__':
#
#     # l = []
#     # for j in range(5):
#     #     for i in range(10):
#     #         l.append(i)
#     numbers = [str(i) for j in range(5) for i in range(7)]
#     strings = ''.join(numbers)
#     for line in snake_string_v1(strings):
#
#         print(''.join(line))
#
#     import string
#
#     alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
#     strings =''.join(alphabet)
#     for line in snake_string_v2(strings, 7):
#
#             print(''.join(line))



#
#
# from typing import List
#
# def get_max_sequence_sum(numbers: List[int], operator=max) -> int:
#     result_sequence, sum_sequence = 0, 0
#     for num in numbers:
#         temp_sum_sequence = sum_sequence + num
#         # if num < temp_sum_sequence:
#         #     sum_sequence = temp_sum_sequence
#         #
#         # else:
#         #     sum_sequence = num
#         sum_sequence = operator(num, sum_sequence + num)
#
#
#
#
#         # if result_sequence < sum_sequence:
#         #     result_sequence = sum_sequence
#         result_sequence = operator(result_sequence, sum_sequence)
#
#     return result_sequence
#
#
# def find_max_circular_sequence_sum(numbers: List[int], operator=max) -> int:
#     max_sequence_sum = get_max_min_sequence_sum(numbers)
#     # invert_numbers = []
#     # all_sum = 0
#     # for num in numbers:
#     #     all_sum += num
#     #     invert_numbers.append(-num)
#
#     max_wrap_sequence = sum(numbers) - get_max_min_sequence_sum(numbers, operator=min)
#
#
#
#
#
# if __name__ == '__main__':
#     print(get_max_sequence_sum([1,-3,4,-11,4,98,-2]))
#






# print(list(dict.fromkeys(l)))
# print(list(dict.fromkeys(l)))
# print(n for i, n in enumerate(l) if n not

#
# from typing import List
#
#
# def delete_duplicate_v1(numbers: List[int]) -> None:
#     tmp = []
#     for num in numbers:
#         if num not in tmp:
#             tmp.append(num)
#     numbers[:] = tmp
#
# def delete_duplicate_v2(numbers: List[int]) -> None:
#     tmp = [numbers[0]]
#     i, len_num = 0, len(numbers) - 1
#     while i < len_num:
#         if numbers[i] != numbers[i+1]:
#             tmp.append(numbers[i+1])
#         i += 1
#     numbers[:] = tmp
#
#
# def delete_duplicate_v3(numbers: List[int]) -> None:
#
#     i= 0
#     while i < len(numbers) - 1:
#         if numbers[i] == numbers[i+1]:
#             numbers.remove(numbers[i])
#             i -= 1
#
#         i += 1
#
# def delete_duplicate_v4(numbers: List[int]) -> None:
#     i = len(numbers) -1
#
#     while i > 0:
#         if numbers[i] == numbers[i-1]:
#             numbers.pop(i)
#
#         i -= 1
#
#
# if __name__ == '__main__':
#     l = [1, 3, 3, 4, 3, 4, 4, 5, 5, 5, 6, 9]
#     delete_duplicate_v1(l)
#     print(l)
#
#     l = [1, 3, 3, 4, 3, 4, 4, 5, 5, 5, 6, 9]
#     delete_duplicate_v2(l)
#     print(l)
#
#     l = [1, 3, 3, 4, 3, 4, 4, 5, 5, 5, 6, 9]
#     delete_duplicate_v4(l)
#     print(l)
#     l = [1, 3, 3, 4, 3, 4, 4, 5, 5, 5, 6, 9]
#     delete_duplicate_v3(l)
#     print(l)

#
# from itertools import permutations
#
# for r in permutations([1,2,3]):
#     print(r)


#
#
# from typing import List, Iterator, Generator
#
# def all_perms(elements: List[int]) -> Iterator[List[int]]:
#
#     result = []
#     if len(elements) <= 1:
#
#         yield elements
#     else:
#
#
#
#         for perm in all_perms(elements[1:]):
#
#
#             for i in range(len(elements)):
#                 yield perm[:i] + elements[0:1] + perm[i:]
#
#
# if __name__ == '__main__':
#
#     for p in all_perms([1,2,3]):
#         print(p)



#
#
# def is_palindrome(strings: str) -> bool:
#     len_strings = len(strings)
#     if not len_strings:
#         return False
#     if len_strings == 1:
#         return True
#         'a'
#         'b'
#
#     start, end = 0, len_strings - 1
#     while start < end:
#         if strings[start] != strings[end]:
#             return False
#
#         start += 1
#         end -= 1
#     return True
#
# if __name__ == '__main__':
#     print(is_palindrome('racecar'))


# def find_palindorome(strings: str, left: int, right: int):
#     result = []
#     while 0 <= left and right <= len(strings) - 1:
#         if strings[left] != strings[right]:
#             break
#         result.append(strings[left: right+1])
#         left -= 1
#         right += 1
#     return result
#
#
#
# def find_all_palindrome(strings: str):
#     result = []
#     len_strings = len(strings)
#     if not len_strings:
#         return result
#     if len_strings == 1:
#         result.append(strings)
#
#     for i in range(1, len_strings-1):
#         yield from find_palindorome(strings, i-1, i+1)]
#         yield from find_palindorome(strings, i-1, i)]
#
#     return result
#
#
# if __name__ == '__main__':
#     print(find_palindorome('cabac', 1, 3))



#
#
# import logging
#
# import threading
# import time
#
#
# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')
#
# def worker1(d, lock):
#     logging.debug('start')
#     with lock:
#         i = d['x']
#         d['x'] = i + 1
#         logging.debug(d)
#         # logging.debug(x)
#         with lock:
#             d['x'] = i + 1
#
#
# def worker2(d, lock):
#     logging.debug('start')
#     lock.acquire()
#     i = d['x']
#     d['x'] = i + 1
#     time.sleep(5)
#     lock.release()
#     logging.debug('end')
#
#
# if __name__ == '__main__':
#     d = {'x': 0}
#     lock = threading.RLock()
#     t1 = threading.Thread( target = worker1, args=(d, lock))
#     t2 = threading.Thread( target = worker1, args=(d, lock))
#     t1.start()
#     t2.start()
#
#
#     #
#     # threads = []
#     #
#     #
#     # for _ in range(5):
#     # #
#     # #
#     #     t = threading.Thread(target=worker1())
#     #     # t2 = threading.Thread(target=worker2())
#     #     t.setDaemon(True)
#     #     # t2.setDaemon(True)
#     #     t.start()
#     #     # t2.start()
#     #     threads.append(t)
#     #
#     # print(threading.enumerate())
#     # for threads in threding.enumerate():
#     #     if threads is threading.currentThread():
#     #         print(thread)
#     #         continue
#     #     threads.join()
#


#
#
# import logging
# import multiprocessing
# import threading
# import time
#
#
# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')
#
# def worker1(queue):
#     item = queue.get()
#     if item is None:
#         break
#     logging.debug(item)
# logging.debug('end')
#
#
#
#     logging.debug('start')
#     queue.put(100)
#     queue.put(200)
#     with lock:
#         logging.debug(d)
#         # logging.debug(x)
#         with lock:
#
#
# def worker2(queue):
#     logging.debug('start')
#     time.sleep(5)
#     print(queue.get())
#     print(queue.get())
#     logging.debug('end')
#
#
# if __name__ == '__main__':
#     for i in range(10000):
#         queue.put(i)
#     [t.join() for t in ts]
#
#     d = {'x': 0}
#     lock = threading.RLock()
#     t1 = threading.Thread( target = worker1, args=(d, lock))
#     t2 = threading.Thread( target = worker1, args=(d, lock))
#     t1.start()
#     t2.start()


#
# import logging
# import multiprocessing
# import threading
# import time
#
#
# logging.basicConfig(
#     level=logging.DEBUG, format='%(threadName)s: %(message)s')
#
# def worker1(i):
#     logging.debug('start')
#     logging.debug(i)
#
#     logging.debug('end')
#     return i * 2
#
#
# #
# #
# # def worker2(i):
# #     logging.debug('start')
# #     logging.debug(i)
# #     logging.debug('end')
#
#
# if __name__ == '__main__':
#
#
#     # t1 = multiprocessing.Process(target=worker1, args=(i,))
#     # t1.daemon = True
#     # t2 = multiprocessing.Process(target=worker2, args=(i,))
#     # t1.start()
#     # t2.start()
#     # t1.join()
#
#     with multiprocessing.Pool(5) as p:
#
#
#         r = p.imap(worker1, [100, 200])
#         logging.debug('executed apply')
#         logging.debug([i for i in r])



#
# import logging
#
# import multiprocessing
#
# import time
#
#
# logging.basicConfig(
#     level=logging.DEBUG, format='%(processName)s: %(message)s')
#
# def f(conn):
#     conn.send('start')
#     time.sleep(5)
#     conn.close('end')
#
# if __name__ == '__main__':
#     parent_conn, child_conn = multiprocessing.Pipe()
#     p = multiprocessing.Process(target=f, args=(parent_conn, ))
#     p.start()
#     logging.debug(child_conn.recv())







import logging

import multiprocessing

import time


logging.basicConfig(
    level=logging.DEBUG, format='%(processName)s: %(message)s')

def worker1(l, d, n):
    l.reverse()
    d['x'] += 1
    n.y += 1



if __name__ == '__main__':

    with multiprocessing.Manager() as manager:
        l = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        l.append(1)
        l.append(2)
        l.append(3)
        d['x'] = 0
        n.y = 0

        p1 = multiprocessing.Process(target=worker1, args=(l,d,n))
        p1.start()
        p1.join()






    # num = multiprocessing.Value('f', 0.0)
    # arr = multiprocessing.Array('i', [1,2,3,4,5])
    #
    # p = multiprocessing.Process(target=f, args=(num,arr))
    # p.start()
    # p.join()
    # logging.debug(num.value)
    # logging.debug(arr[:])
    #
    #





