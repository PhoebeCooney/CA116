#import func_reverse

def swap(a, i ,j):
   tmp = a[j]
   a[j] = a[i]
   a[i] = tmp

def reverse(a):
   i = 0
   while i < len(a)/2:
      swap (a, i, len(a) - i - 1)
      i += 1

a = [4, 3, 1, 2]

def main():
   swap(a, 2, 3)
   print a    # [4, 3, 2, 1]

   reverse(a)
   print a    # [1, 2, 3, 4]

if __name__ == "__main__":
   main()
