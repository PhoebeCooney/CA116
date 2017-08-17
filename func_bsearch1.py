def bsearch(a, q):
   low = 0
   high = len(a)

   while low < high:
      mid = (low + high) / 2
      assert low <= mid < high

      if a [mid] < q:
         low = mid + 1
         assert low == 0 or a[low - 1] < a
      else:
         high = mid
         assert q <= a[high]
   return low

def main():
   print bsearch([2,3,6,6,7,8], 1)  # 0
   print bsearch([2,3,6,6,7,8], 2)  # 0
   print bsearch([2,3,6,6,7,8], 6)  # 2
   print bsearch([2,3,6,6,7,8], 8)  # 5
   print bsearch([2,3,6,6,7,8], 9)  # 6
   print bsearch([2,3,6,6,7,8], 4)  # 2 

if __name__ == "__main__":
   main()
