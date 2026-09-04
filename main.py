def my_print_num(n):
  if n==5:
    return
  my_print_num(n-1)
  
  print(n)
n=5
my_print_num(n) 