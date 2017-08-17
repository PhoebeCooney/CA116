import func_bsearch

def sum_range(a, low, high):
   low = func_bsearch.bsearch(a, low)
   no = 0
   while low < len(a) and a[low] < high:
      no = no +int(a[low])
      low = low + 1
   return no

def main():
   print sum_range([2,3,6,6,7,8], 3, 7)    # 15
   print sum_range([2,3,6,6,7,8], 3, 8)    # 22
   print sum_range([2,3,6,6,7,8], -10, 3)  # 2
   print sum_range([2,3,6,6,7,8], 7, 20)   # 15
   print sum_range([2,3,6,6,7,8], 10, 20)  # 0

if __name__ == "__main__":
   main()
