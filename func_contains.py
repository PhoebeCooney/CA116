import func_bsearch

def contains(a, q):
   p = func_bsearch.bsearch(a, q)

   return p < len(a) and a[p] == q

def main():
   print contains([2,3,6,6,7,8], 1)  # False
   print contains([2,3,6,6,7,8], 2)  # True
   print contains([2,3,6,6,7,8], 6)  # True
   print contains([2,3,6,6,7,8], 8)  # True
   print contains([2,3,6,6,7,8], 9)  # False
   print contains([2,3,6,6,7,8], 4)  # False

if __name__ == "__main__":
   main()
