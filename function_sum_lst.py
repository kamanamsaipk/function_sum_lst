def sum_list():
   size = int(input("enter the total no of elemnets: "))
   lst = []
   for i in range(size):
      lst_elements = int(input("enter the each element: "))
      lst.append(lst_elements)
   print(lst)
   sum_of_elements = sum(lst)
   print("sum of elements is :  ",sum_of_elements)
sum_list()