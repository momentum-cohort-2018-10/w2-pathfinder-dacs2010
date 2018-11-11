new_list = [6,-5,3]
abs_list = []
# print(min(abs(new_list)))
# for i in new_list:
#     abs_list.append(abs(i))
#     print(min(abs_list))

# find minium after checking the absolute value of each item in list
print(min(new_list, key = abs))