import func_selection_sort
a = [1, 2, 3, 1, 2, 3]

def find_smallest_position(a,i):
   p = i 
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j += 1
   return p

def swap(a, i, j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def selection_sort(a):
   i = 0
   while i < len(a):
      p = find_smallest_position(a,i)
      swap (a, i, p)
      i += 1

def main():
   selection_sort(a)
   print a       # [1, 1, 2, 2, 3, 3]

if __name__ == "__main__":
   main()
