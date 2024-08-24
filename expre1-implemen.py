# WAP to check if two lists are identical 
list1 = [1, 2, 4, 3, 5]
list2 = [1, 4,3 , 7, 5]
print("The first list is : " ,list1)
print("The second list is : ",list2)
list1.sort()
list2.sort()
print("After sorting the list")
print(list1)
print(list2)
if list1 == list2:
    print("The lists are identical!!")
else:
    print("The lists are not identical!!")



# WAP to check all the common element in a list
lst = [1, 2, 3, 4, 5, 3, 2, 4, 6, 7, 8, 2]
common_ele = []
for e in lst:
    if lst.count(e) > 1 and e not in common_ele:
        common_ele.append(e)
print("Common elements: ", common_ele)









# def common_mem(a, b):
#     a_set = set(a)
#     b_set = set(b)
#     if (a_set & b_set):
#         print(a_set & b_set)
#     else:
#         print("No common elements") 
# a = [1, 2, 3, 6, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# common_mem(a, b)